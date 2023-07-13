CREATE MATERIALIZED VIEW tupande_db.contract_details AS
SELECT
    c.reference AS contract_reference,
    c.status,
    CASE
        WHEN o.name ILIKE '%group%' THEN 'Group loan'
        WHEN o.name ILIKE '%individual%' THEN 'Individual loan'
        WHEN o.name ILIKE '%cash%' THEN 'Cash sale'
    END AS loan_type,
    c.start_date::date AS start_date,
    (c.start_date::date + INTERVAL '180 days')::date AS end_date,
    (c.start_date::date + INTERVAL '180 days' + CASE
        WHEN o.name ILIKE '%group%' THEN INTERVAL '30 days'
        WHEN o.name ILIKE '%individual%' THEN INTERVAL '60 days'
        WHEN o.name ILIKE '%cash%' THEN INTERVAL '30 days'
    END)::date AS maturity_date,
    c.nominal_contract_value,
    c.cumulative_amount_paid,
    l.state,
    l.county
FROM
    contracts c
    INNER JOIN contract_offers o ON c.offer_id = o.id
    INNER JOIN leads l ON c.lead_id = l.id; 

-- Create unique index on the contract_reference column to allow concurent refreshing of the material view.

CREATE UNIQUE INDEX idx_contract_details_contract_reference ON contract_details (contract_reference);