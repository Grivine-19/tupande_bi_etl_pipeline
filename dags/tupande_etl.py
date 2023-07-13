from dotenv import load_dotenv
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email_operator import EmailOperator
from airflow.operators.postgres_operator import PostgresOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
from sqlalchemy import create_engine
import pandas as pd
import os
import csv

# Load environment variables from .env file
load_dotenv()

default_args = {
    'owner': 'Grivine',
    'depends_on_past': False,
    'start_date': days_ago(1),
    'email': ['grivineochieng@outlook.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'tupande_bi',
    default_args=default_args,
    owner_links = {"Grivine":"mailto:grivineochieng@outlook.com"},
    description='Load CSV files to PostgreSQL',
    schedule_interval=timedelta(days=1),
    template_searchpath=['/opt/airflow/include']
)

# Define the directory path and file names
dir_path = os.path.dirname(os.path.realpath(__file__))

file_names = ['contract_offers.csv','contract_payments.csv', 'contracts.csv', 'leads.csv']

# Create the engine 
engine = create_engine(os.getenv('DB_URL'))

# Task to check if all required files exist in specified folder or not
def check_files():
    missing_files = []
    for file_name in file_names:
        if not os.path.isfile(os.path.join(dir_path+'/data', file_name)):
            missing_files.append(file_name)
    if missing_files:
        raise ValueError(
            f"The following files are missing: {', '.join(missing_files)}")
    
    print("All required files exist.")

check_files_task = PythonOperator(
    task_id='check_files',
    python_callable=check_files,
    dag=dag,
)

# Task to check if all required columns are present in each file
def check_columns():
    missing_columns = {}
    for file_name in file_names:
        with open(os.path.join(dir_path+'/data', file_name), 'r') as f:
            reader = csv.DictReader(f)
            required_columns = set()
            if file_name == 'contract_offers.csv':
                required_columns = {'id', 'name', 'type', 'total_value'}
            elif file_name == 'contract_payments.csv':
                required_columns = {
                    'id', 'contract_reference', 'payment_date','type', 'amount_paid'}
            elif file_name == 'contracts.csv':
                required_columns = {'reference', 'status',
                                    'start_date', 'offer_id', 'lead_id', 'cumulative_amount_paid', 'nominal_contract_value'}
            elif file_name == 'leads.csv':
                required_columns = {
                    'id', 'status', 'contract_reference', 'state', 'county'}
            missing_cols = required_columns - set(reader.fieldnames)
            if missing_cols:
                missing_columns[file_name] = missing_cols
    if missing_columns:
        raise ValueError(
            f"The following columns are missing: {missing_columns}")
    print("All required columns exist.")

check_columns_task = PythonOperator(
    task_id='check_columns',
    python_callable=check_columns,
    dag=dag,
)

# Task to load data from CSV files to PostgreSQL
def load_data():
    for filename in file_names:
        # Read CSV file into a dataframe
        df = pd.read_csv(os.path.join(dir_path+'/data', filename))
        # Insert data into the table
        df.to_sql(filename.split('.')[0], engine, index=False, if_exists='replace')

load_data_task = PythonOperator(
    task_id='load_data',
    python_callable=load_data,
    dag=dag,
)

#Task to create contract data
def create_contract_data():
    engine.execute("REFRESH MATERIALIZED VIEW CONCURRENTLY contract_details")

create_contract_data_task = PythonOperator(
    task_id='create_contract_data',
    python_callable=create_contract_data,
    dag=dag,
)

#Task to send the data from contract_details in csv format via email
def send_contract_data():
    # Read data from the table
    df = pd.read_sql_table('contract_details', engine)
    # Convert dataframe to csv
    csv_data = df.to_csv(index=False)
    # Send email
    EmailOperator(
        task_id='send_contract_data_email',
        to='grivineochieng@outlook.com',
        subject='Contract Data',
        html_content=""" <h3>Tupande Contract Data Summary </h3> """,  # csv_data,
        files=[{'name': 'contract_data.csv', 'content': csv_data}],
        dag=dag,
    )

send_contract_data_task = PythonOperator(
    task_id='send_contract_data',
    python_callable=send_contract_data,
    dag=dag,
)

email_message = """
    Hi,
    
    The following files or columns are missing:
    
    {missing}
    
    Please check and resolve the issue.
    
    Thanks,
    Airflow
"""

# Task to send an email alert
def send_email(**context):
    missing_files = context.get('task_instance').xcom_pull(
        key='missing_files', task_ids='check_files')
    missing_columns = context.get('task_instance').xcom_pull(
        key='missing_columns', task_ids='check_columns')
    if missing_files or missing_columns:
        missing = ''
        if missing_files:
            missing += f"Missing files: {', '.join(missing_files)}\n"
        if missing_columns:
            missing += "Missing columns:\n"
            for file_name, cols in missing_columns.items():
                missing += f"{file_name}: {', '.join(cols)}\n"
        EmailOperator(
            task_id='send_email_1',
            to='grivineochieng@outlook.com',
            subject='Missing files or columns',
            html_content=email_message.format(missing=missing),
            dag=dag,
        ).execute(context=context)


send_email_task = PythonOperator(
    task_id='send_email',
    python_callable=send_email,
    provide_context=True,
    dag=dag,
)

# Define task dependencies
(check_files_task >> check_columns_task) >> load_data_task >> create_contract_data_task >> send_contract_data_task
(check_files_task >> send_email_task)
(check_columns_task >> send_email_task)
