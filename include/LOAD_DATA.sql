COPY contract_offers.csv
FROM %(file_path)s DELIMITER ',' CSV HEADER;

COPY tupande_db .contract_payments.csv
FROM %(file_path)s DELIMITER ',' CSV HEADER;

COPY tupande_db .contracts.csv
FROM %(file_path)s DELIMITER ',' CSV HEADER;

COPY tupande_db .leads.csv
FROM %(file_path)s DELIMITER ',' CSV HEADER;