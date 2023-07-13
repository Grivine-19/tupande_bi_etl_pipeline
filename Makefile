create_permisible_directories: #On Linux, the service needs to know your host user id and needs to have group id set to 0. 
	mkdir -p ./dags ./logs ./plugins ./config ./include
	echo -e "AIRFLOW_UID=$(id -u)" > .env
	echo -e "AIRFLOW_CONN_SMTP_DEFAULT=smtp://example@outlook.com:password@smtp.office365.com:587" >> .env

start_etl_service:
	docker-compose up -d

stop_etl_service:
	docker compose down --volumes --remove-orphans

clear_directory:
	rm -rf ./dags ./logs ./plugins ./config ./include