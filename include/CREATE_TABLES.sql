CREATE TABLE
    IF NOT EXISTS contract_offers (
        id VARCHAR(255) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        type VARCHAR(255) NOT NULL,
        total_value NUMERIC(19, 2) NOT NULL
    );

CREATE TABLE
    IF NOT EXISTS contract_payments (
        id VARCHAR(255) PRIMARY KEY,
        contract_reference VARCHAR(255) NOT NULL,
        payment_date DATE NOT NULL,
        type VARCHAR(255) NOT NULL,
        amount_paid NUMERIC(19, 2) NOT NULL
    );

CREATE TABLE
    IF NOT EXISTS contracts (
        reference VARCHAR(255) PRIMARY KEY,
        status VARCHAR(255) NOT NULL,
        start_date DATE NOT NULL,
        offer_id VARCHAR(255) NOT NULL,
        lead_id VARCHAR(255) NOT NULL,
        cumulative_amount_paid NUMERIC(19, 2) NOT NULL,
        nominal_contract_value NUMERIC(19, 2) NOT NULL
    );

CREATE TABLE
    IF NOT EXISTS leads (
        id VARCHAR(255) PRIMARY KEY,
        status VARCHAR(255) NOT NULL,
        contract_reference VARCHAR(255) NOT NULL,
        state VARCHAR(255) NOT NULL,
        county VARCHAR(255) NOT NULL
    ); 