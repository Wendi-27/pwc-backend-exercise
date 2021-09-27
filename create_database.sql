DROP TABLE IF EXISTS  companies;

CREATE TABLE companies (
    primary_id INTEGER PRIMARY KEY AUTOINCREMENT,
    id INTEGER NOT NULL,
    created_time TIMESTAMP  NOT NULL  DEFAULT current_timestamp,
    fake_company_name TEXT NOT NULL,
    description TEXT NOT NULL,
    tagline TEXT NOT NULL,
    company_email TEXT NOT NULL,
    business_number TEXT NOT NULL,
    restricted INTEGER NOT NULL CHECK (restricted IN (0, 1))
);