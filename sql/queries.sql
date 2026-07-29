-- =====================================================
-- MUTUAL FUND CAPSTONE PROJECT
-- BASIC SQL ANALYTICS QUERIES
-- =====================================================

---------------------------------------------------------
-- Query 1 : Total Number of Schemes
---------------------------------------------------------
SELECT COUNT(*) AS total_schemes
FROM fund_master;

---------------------------------------------------------
-- Query 2 : List All Fund Houses
---------------------------------------------------------
SELECT DISTINCT fund_house
FROM fund_master
ORDER BY fund_house;

---------------------------------------------------------
-- Query 3 : Number of Schemes by Category
---------------------------------------------------------
SELECT
    category,
    COUNT(*) AS total_schemes
FROM fund_master
GROUP BY category
ORDER BY total_schemes DESC;

---------------------------------------------------------
-- Query 4 : Average NAV
---------------------------------------------------------
SELECT
    ROUND(AVG(nav),2) AS average_nav
FROM nav_history;

---------------------------------------------------------
-- Query 5 : Highest 10 NAV Values
---------------------------------------------------------
SELECT
    amfi_code,
    date,
    nav
FROM nav_history
ORDER BY nav DESC
LIMIT 10;

---------------------------------------------------------
-- Query 6 : Top 10 Fund Houses by AUM
---------------------------------------------------------
SELECT
    fund_house,
    SUM(aum) AS total_aum
FROM aum_by_fund_house
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 10;

---------------------------------------------------------
-- Query 7 : Monthly SIP Inflows
---------------------------------------------------------
SELECT *
FROM monthly_sip_inflows
ORDER BY month;

---------------------------------------------------------
-- Query 8 : Category-wise Inflows
---------------------------------------------------------
SELECT
    category,
    SUM(inflow) AS total_inflow
FROM category_inflows
GROUP BY category
ORDER BY total_inflow DESC;

---------------------------------------------------------
-- Query 9 : Total Portfolio Holdings
---------------------------------------------------------
SELECT COUNT(*) AS total_holdings
FROM portfolio_holdings;

---------------------------------------------------------
-- Query 10 : Latest Benchmark Index Records
---------------------------------------------------------
SELECT *
FROM benchmark_indices
ORDER BY date DESC
LIMIT 10;