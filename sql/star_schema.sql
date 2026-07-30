-- ======================================================
-- STAR SCHEMA
-- Mutual Fund Capstone Project
-- ======================================================

-- Drop Fact Tables
DROP TABLE IF EXISTS fact_nav;
DROP TABLE IF EXISTS fact_transactions;
DROP TABLE IF EXISTS fact_performance;
DROP TABLE IF EXISTS fact_aum;
DROP TABLE IF EXISTS fact_sip_inflows;
DROP TABLE IF EXISTS fact_category_inflows;
DROP TABLE IF EXISTS fact_folio_count;
DROP TABLE IF EXISTS fact_portfolio_holdings;
DROP TABLE IF EXISTS fact_benchmark;

-- Drop Dimension Tables
DROP TABLE IF EXISTS dim_date;
DROP TABLE IF EXISTS dim_fund;

-- ======================================================
-- DIMENSION TABLE : FUND
-- Source : clean_fund_master.csv
-- ======================================================

CREATE TABLE dim_fund (

    fund_id INTEGER PRIMARY KEY AUTOINCREMENT,

    amfi_code INTEGER UNIQUE,

    fund_house TEXT,

    scheme_name TEXT,

    category TEXT,

    sub_category TEXT,

    plan TEXT,

    benchmark TEXT,

    expense_ratio_pct REAL,

    exit_load_pct REAL,

    min_sip_amount REAL,

    min_lumpsum_amount REAL,

    fund_manager TEXT,

    risk_category TEXT
);

-- ======================================================
-- DIMENSION TABLE : DATE
-- ======================================================

CREATE TABLE dim_date (

    date_id INTEGER PRIMARY KEY AUTOINCREMENT,

    full_date DATE UNIQUE,

    day INTEGER,

    month INTEGER,

    month_name TEXT,

    quarter INTEGER,

    year INTEGER
);

-- ======================================================
-- FACT TABLE : NAV
-- Source : clean_nav.csv
-- ======================================================

CREATE TABLE fact_nav (

    nav_id INTEGER PRIMARY KEY AUTOINCREMENT,

    fund_id INTEGER,

    date_id INTEGER,

    nav REAL,

    FOREIGN KEY (fund_id)
        REFERENCES dim_fund(fund_id),

    FOREIGN KEY (date_id)
        REFERENCES dim_date(date_id)
);

-- ======================================================
-- FACT TABLE : TRANSACTIONS
-- Source : clean_transactions.csv
-- ======================================================

CREATE TABLE fact_transactions (

    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,

    fund_id INTEGER,

    date_id INTEGER,

    investor_id TEXT,

    transaction_type TEXT,

    amount REAL,

    kyc_status TEXT,

    FOREIGN KEY (fund_id)
        REFERENCES dim_fund(fund_id),

    FOREIGN KEY (date_id)
        REFERENCES dim_date(date_id)
);

-- ======================================================
-- FACT TABLE : PERFORMANCE
-- Source : clean_performance.csv
-- ======================================================

CREATE TABLE fact_performance (

    performance_id INTEGER PRIMARY KEY AUTOINCREMENT,

    fund_id INTEGER,

    returns_1y REAL,

    returns_3y REAL,

    returns_5y REAL,

    FOREIGN KEY (fund_id)
        REFERENCES dim_fund(fund_id)
);

-- ======================================================
-- FACT TABLE : AUM
-- Source : clean_aum.csv
-- ======================================================

CREATE TABLE fact_aum (

    aum_id INTEGER PRIMARY KEY AUTOINCREMENT,

    fund_id INTEGER,

    date_id INTEGER,

    aum REAL,

    FOREIGN KEY (fund_id)
        REFERENCES dim_fund(fund_id),

    FOREIGN KEY (date_id)
        REFERENCES dim_date(date_id)
);

-- ======================================================
-- FACT TABLE : MONTHLY SIP INFLOWS
-- Source : clean_monthly_sip.csv
-- ======================================================

CREATE TABLE fact_sip_inflows (

    sip_id INTEGER PRIMARY KEY AUTOINCREMENT,

    date_id INTEGER,

    sip_amount REAL,

    FOREIGN KEY (date_id)
        REFERENCES dim_date(date_id)
);

-- ======================================================
-- FACT TABLE : CATEGORY INFLOWS
-- Source : clean_category_inflows.csv
-- ======================================================

CREATE TABLE fact_category_inflows (

    category_inflow_id INTEGER PRIMARY KEY AUTOINCREMENT,

    fund_id INTEGER,

    date_id INTEGER,

    inflow REAL,

    FOREIGN KEY (fund_id)
        REFERENCES dim_fund(fund_id),

    FOREIGN KEY (date_id)
        REFERENCES dim_date(date_id)
);

-- ======================================================
-- FACT TABLE : INDUSTRY FOLIO COUNT
-- Source : clean_industry_folio.csv
-- ======================================================

CREATE TABLE fact_folio_count (

    folio_id INTEGER PRIMARY KEY AUTOINCREMENT,

    fund_id INTEGER,

    date_id INTEGER,

    folio_count INTEGER,

    FOREIGN KEY (fund_id)
        REFERENCES dim_fund(fund_id),

    FOREIGN KEY (date_id)
        REFERENCES dim_date(date_id)
);

-- ======================================================
-- FACT TABLE : PORTFOLIO HOLDINGS
-- Source : clean_portfolio_holdings.csv
-- ======================================================

CREATE TABLE fact_portfolio_holdings (

    holding_id INTEGER PRIMARY KEY AUTOINCREMENT,

    fund_id INTEGER,

    company_name TEXT,

    sector TEXT,

    holding_percent REAL,

    FOREIGN KEY (fund_id)
        REFERENCES dim_fund(fund_id)
);

-- ======================================================
-- FACT TABLE : BENCHMARK INDICES
-- Source : clean_benchmark_indices.csv
-- ======================================================

CREATE TABLE fact_benchmark (

    benchmark_id INTEGER PRIMARY KEY AUTOINCREMENT,

    date_id INTEGER,

    index_name TEXT,

    close_price REAL,

    FOREIGN KEY (date_id)
        REFERENCES dim_date(date_id)
);