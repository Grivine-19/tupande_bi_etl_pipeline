<div align="center">
    <h1>🚀 Tupande BI ETL Pipeline</h1>
</div>

## Project Summary
The Tupande BI ETL Pipeline is a data pipeline project designed to extract, transform, and load data for business intelligence purposes. It automates the process of collecting data from a file system, performing transformations, and loading it into a PostgreSQL database. The project utilizes **Apache Airflow**, **PostgreSQL**, **Python**, and **Docker** to create a scalable and efficient ETL (Extract, Transform, Load) pipeline.

## Technologies and Tools Used
The Tupande BI ETL Pipeline leverages the following technologies and tools:

- <img src="https://seekicon.com/free-icon-download/airflow_1.svg" alt="Apache Airflow" width="50" height="50"> Apache Airflow: A platform for programmatically authoring, scheduling, and monitoring workflows.
- ![PostgreSQL](https://img.icons8.com/?size=1x&id=38561&format=png) PostgreSQL: A powerful open-source relational database management system.
- ![Python](https://img.icons8.com/color/48/000000/python.png) Python: A versatile programming language used for scripting and data processing.
- ![Docker](https://img.icons8.com/color/48/000000/docker.png) Docker: A containerization platform used for easy deployment and management of the project's components.

By combining these technologies, the project ensures efficient data processing, reliable task scheduling, and seamless integration with the PostgreSQL database.

## Prerequisites
To run the Tupande BI ETL Pipeline, ensure you have the following prerequisites installed:

- **Python**: Install Python 3.x 
- **Docker**: Install Docker Community Edition (CE) on your workstation. Depending on your OS, you may need to configure Docker to use at least 4.00 GB of memory for the Airflow containers to run properly.
- **Docker-compose**: Install Docker Compose v1.29.1 or newer on your workstation. Older versions of docker-compose do not support all the features required by the Airflow docker-compose.yaml file, so double check that your version meets the minimum version requirements.

Make sure to meet these prerequisites before setting up and running the Tupande BI ETL Pipeline.


## **Folder Structure**
```
📂 tupande_bi_etl_pipeline
   |
   |-- 📂 dags
   |    |
   |    |-- 📂 data
   |    |    |
   |    |    |-- 📄 contract_offers.csv
   |    |    |-- 📄 contract_payments.csv
   |    |    |-- 📄 contracts.csv
   |    |    |-- 📄 leads.csv
   |    |
   |    |-- 📄 tupande_etl.py
   |
   |-- 📂 logs
   |    |
   |    |-- 📂 scheduler
   |    |
   |    |-- 📂 dag_processor_manager
   |
   |-- 📂 plugins
   |
   |-- 📂 config
   |    |
   |    |-- 📄 airflow.cfg
   |
   |-- 📂 include
   |    |
   |    |-- 📄 CREATE_CONTRACT_DATA.sql
   |
   |-- 📄 .env
   |
   |-- 📄 docker-compose.yaml
   |
   |-- 📄 Makefile
   |
   |-- 📄 README.MD

```
<details>
<summary><strong>Folder Structure Description(click to expand)</strong></summary>

- 📂 **dags**: Contains the DAG files for the ETL pipeline.
    - 📂 **data**: Stores the data files used in the ETL process.
        - 📄 `contract_offers.csv`: File containing contract offer data.
        - 📄 `contract_payments.csv`: File containing contract payment data.
        - 📄 `contracts.csv`: File containing contract data.
        - 📄 `leads.csv`: File containing lead data.
    - 📄 `tupande_etl.py`: Python script implementing the ETL pipeline.

- 📂 **logs**: Stores logs generated during pipeline execution.
    - 📂 **scheduler**: Contains logs related to the Airflow scheduler.
    - 📂 **dag_processor_manager**: Contains logs related to the DAG processor manager.

- 📂 **plugins**: Holds custom plugins or modules used in the ETL pipeline.

- 📂 **config**: Contains configuration files for Airflow.
    - 📄 `airflow.cfg`: Airflow configuration file.

- 📂 **include**: Contains additional SQL or script files used in the ETL process.
    - 📄 `CREATE_CONTRACT_DATA.sql`: SQL script for creating contract data.

- 📄 `.env`: Environment file containing environment variables.

- 📄 `docker-compose.yaml`: Docker Compose file for containerized deployment.

- 📄 `Makefile`: Makefile with predefined tasks for managing the pipeline.

- 📄 `README.MD`: Readme file providing information and instructions about the ETL pipeline.

</details>

## Running the Tupande BI ETL Pipeline

Follow these steps to run the Tupande BI ETL Pipeline:

1. **Clone the Repository**: 

<img src="https://img.icons8.com/color/24/000000/git.png"/> Clone the repository to your local machine.

2. **Configure SMTP for Email Notifications and Reporting**:
- Locate the relevant files in the project folder structure described earlier(above).
- Set the appropriate parameters for SMTP configuration to enable email notifications and reporting.

3. **Create a .env File**:
- Create a `.env` file in the project root directory.
- Store sensitive variables, such as `DB_URL` and `AIRFLOW_CONN_SMTP_DEFAULT`, in the `.env` file.

4. **Run the Make Command**: 

<img src="https://img.icons8.com/color/24/000000/console.png"/> Run the make command `make start_etl_service` to fire up the pipeline.

5. **Sit back and Enjoy**:

🎉 The Tupande BI ETL Pipeline is now running! You can monitor the progress and check the generated reports and notifications.

---

🚀 Have a smooth data journey with Tupande BI! ✨

<img src="https://img.icons8.com/ios-filled/50/000000/rocket.png"/> **Happy data processing!** 🎉
