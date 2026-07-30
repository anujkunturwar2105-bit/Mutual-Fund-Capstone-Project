# Mutual Fund Data Dictionary

## 1. fund_master
| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | INTEGER | Unique AMFI Scheme Code |
| fund_house | TEXT | Mutual Fund Company |
| scheme_name | TEXT | Name of the Mutual Fund Scheme |
| category | TEXT | Fund Category (Equity, Debt, etc.) |
| sub_category | TEXT | Sub-category of the Scheme |
| plan | TEXT | Direct or Regular Plan |
| benchmark | TEXT | Benchmark Index |
| expense_ratio_pct | REAL | Annual Expense Ratio (%) |
| risk_category | TEXT | Risk Level of the Scheme |

**Source:** `01_fund_master.csv`

---

## 2. nav_history
| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | INTEGER | AMFI Scheme Code |
| date | DATE | NAV Date |
| nav | REAL | Net Asset Value |

**Source:** `02_nav_history.csv`

---

## 3. aum_by_fund_house
| Column | Data Type | Description |
|---------|-----------|-------------|
| fund_house | TEXT | Mutual Fund Company |
| date | DATE | Reporting Date |
| aum | REAL | Assets Under Management |

**Source:** `03_aum_by_fund_house.csv`

---

## 4. monthly_sip_inflows
| Column | Data Type | Description |
|---------|-----------|-------------|
| month | DATE | Reporting Month |
| sip_amount | REAL | Monthly SIP Collection |

**Source:** `04_monthly_sip_inflows.csv`

---

## 5. category_inflows
| Column | Data Type | Description |
|---------|-----------|-------------|
| category | TEXT | Fund Category |
| month | DATE | Reporting Month |
| inflow | REAL | Net Inflow/Outflow |

**Source:** `05_category_inflows.csv`

---

## 6. industry_folio_count
| Column | Data Type | Description |
|---------|-----------|-------------|
| month | DATE | Reporting Month |
| folio_count | INTEGER | Total Investor Folios |

**Source:** `06_industry_folio_count.csv`

---

## 7. scheme_performance
| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | INTEGER | AMFI Scheme Code |
| returns_1y | REAL | One-Year Return (%) |
| returns_3y | REAL | Three-Year Return (%) |
| returns_5y | REAL | Five-Year Return (%) |

**Source:** `07_scheme_performance.csv`

---

## 8. investor_transactions
| Column | Data Type | Description |
|---------|-----------|-------------|
| transaction_id | INTEGER | Unique Transaction ID |
| investor_id | INTEGER | Investor Identifier |
| amfi_code | INTEGER | AMFI Scheme Code |
| transaction_type | TEXT | SIP, Lumpsum or Redemption |
| amount | REAL | Transaction Amount |
| transaction_date | DATE | Transaction Date |
| state | TEXT | Investor State |
| kyc_status | TEXT | KYC Verification Status |

**Source:** `08_investor_transactions.csv`

---

## 9. portfolio_holdings
| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | INTEGER | AMFI Scheme Code |
| company_name | TEXT | Invested Company |
| sector | TEXT | Industry Sector |
| holding_percent | REAL | Portfolio Allocation (%) |

**Source:** `09_portfolio_holdings.csv`

---

## 10. benchmark_indices
| Column | Data Type | Description |
|---------|-----------|-------------|
| date | DATE | Trading Date |
| index_name | TEXT | Benchmark Index |
| close_price | REAL | Closing Index Value |

**Source:** `10_benchmark_indices.csv`