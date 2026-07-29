-- ===============================================
-- Mutual Fund Capstone Project
-- SQLite Database Schema
-- ===============================================

DROP TABLE IF EXISTS fund_master;
DROP TABLE IF EXISTS nav_history;
DROP TABLE IF EXISTS aum_by_fund_house;
DROP TABLE IF EXISTS monthly_sip_inflows;
DROP TABLE IF EXISTS category_inflows;
DROP TABLE IF EXISTS industry_folio_count;
DROP TABLE IF EXISTS scheme_performance;
DROP TABLE IF EXISTS investor_transactions;
DROP TABLE IF EXISTS portfolio_holdings;
DROP TABLE IF EXISTS benchmark_indices;

--------------------------------------------------
-- 1. Fund Master
--------------------------------------------------
CREATE TABLE fund_master (
    amfi_code INTEGER PRIMARY KEY,
    fund_house TEXT,
    scheme_name TEXT,
    category TEXT,
    sub_category TEXT,
    plan TEXT,
    launch_date TEXT,
    benchmark TEXT,
    expense_ratio_pct REAL,
    exit_load_pct REAL,
    min_sip_amount REAL,
    min_lumpsum_amount REAL,
    fund_manager TEXT,
    risk_category TEXT,
    sebi_category_code TEXT
);

--------------------------------------------------
-- 2. NAV History
--------------------------------------------------
CREATE TABLE nav_history (
    amfi_code INTEGER,
    date TEXT,
    nav REAL
);

--------------------------------------------------
-- 3. AUM by Fund House
--------------------------------------------------
CREATE TABLE aum_by_fund_house (
    fund_house TEXT,
    month TEXT,
    aum REAL
);

--------------------------------------------------
-- 4. Monthly SIP Inflows
--------------------------------------------------
CREATE TABLE monthly_sip_inflows (
    month TEXT,
    sip_amount REAL
);

--------------------------------------------------
-- 5. Category Inflows
--------------------------------------------------
CREATE TABLE category_inflows (
    category TEXT,
    inflow REAL,
    month TEXT
);

--------------------------------------------------
-- 6. Industry Folio Count
--------------------------------------------------
CREATE TABLE industry_folio_count (
    category TEXT,
    folio_count INTEGER
);

--------------------------------------------------
-- 7. Scheme Performance
--------------------------------------------------
CREATE TABLE scheme_performance (
    amfi_code INTEGER,
    returns_1y REAL,
    returns_3y REAL,
    returns_5y REAL
);

--------------------------------------------------
-- 8. Investor Transactions
--------------------------------------------------
CREATE TABLE investor_transactions (
    transaction_id INTEGER,
    amfi_code INTEGER,
    investor_id TEXT,
    transaction_type TEXT,
    amount REAL,
    transaction_date TEXT
);

--------------------------------------------------
-- 9. Portfolio Holdings
--------------------------------------------------
CREATE TABLE portfolio_holdings (
    amfi_code INTEGER,
    company_name TEXT,
    sector TEXT,
    holding_percent REAL
);

--------------------------------------------------
-- 10. Benchmark Indices
--------------------------------------------------
CREATE TABLE benchmark_indices (
    index_name TEXT,
    date TEXT,
    close_price REAL
);