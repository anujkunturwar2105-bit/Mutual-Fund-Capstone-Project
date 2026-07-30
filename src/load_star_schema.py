import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

# ==========================================
# Paths
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "Data" / "processed"
DB_PATH = BASE_DIR / "bluestock_mf.db"

engine = create_engine(f"sqlite:///{DB_PATH}")

print("Connected to SQLite Database")

# ==========================================
# Load Dimension : Fund
# ==========================================

fund = pd.read_csv(DATA_DIR / "clean_fund_master.csv")

dim_fund = fund[
    [
        "amfi_code",
        "fund_house",
        "scheme_name",
        "category",
        "sub_category",
        "plan",
        "benchmark",
        "expense_ratio_pct",
        "exit_load_pct",
        "min_sip_amount",
        "min_lumpsum_amount",
        "fund_manager",
        "risk_category",
    ]
].drop_duplicates()

dim_fund.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False,
)

print("✓ dim_fund loaded")

# ==========================================
# Load Dimension : Date
# ==========================================

dates = []

# NAV
nav = pd.read_csv(DATA_DIR / "clean_nav.csv")
dates.extend(pd.to_datetime(nav["date"]))

# Transactions
txn = pd.read_csv(DATA_DIR / "clean_transactions.csv")
dates.extend(pd.to_datetime(txn["transaction_date"]))

# AUM
aum = pd.read_csv(DATA_DIR / "clean_aum.csv")
dates.extend(pd.to_datetime(aum["date"]))

# Benchmark
benchmark = pd.read_csv(DATA_DIR / "clean_benchmark_indices.csv")
dates.extend(pd.to_datetime(benchmark["date"]))

# Portfolio
portfolio = pd.read_csv(DATA_DIR / "clean_portfolio_holdings.csv")
dates.extend(pd.to_datetime(portfolio["portfolio_date"]))

# Monthly SIP
sip = pd.read_csv(DATA_DIR / "clean_monthly_sip.csv")
dates.extend(pd.to_datetime(sip["month"]))

# Category Inflow
cat = pd.read_csv(DATA_DIR / "clean_category_inflows.csv")
dates.extend(pd.to_datetime(cat["month"]))

# Industry Folio
folio = pd.read_csv(DATA_DIR / "clean_industry_folio.csv")
dates.extend(pd.to_datetime(folio["month"]))

dates = pd.Series(dates).drop_duplicates().sort_values()

dim_date = pd.DataFrame()

dim_date["full_date"] = dates
dim_date["day"] = dates.dt.day
dim_date["month"] = dates.dt.month
dim_date["month_name"] = dates.dt.month_name()
dim_date["quarter"] = dates.dt.quarter
dim_date["year"] = dates.dt.year

dim_date.to_sql(
    "dim_date",
    engine,
    if_exists="replace",
    index=False,
)

print("✓ dim_date loaded")

# ==========================================
# FACT NAV
# ==========================================

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False,
)

print("✓ fact_nav loaded")

# ==========================================
# FACT TRANSACTIONS
# ==========================================

txn.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False,
)

print("✓ fact_transactions loaded")

# ==========================================
# FACT PERFORMANCE
# ==========================================

performance = pd.read_csv(DATA_DIR / "clean_performance.csv")

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False,
)

print("✓ fact_performance loaded")

# ==========================================
# FACT AUM
# ==========================================

aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False,
)

print("✓ fact_aum loaded")

# ==========================================
# FACT SIP INFLOWS
# ==========================================

sip.to_sql(
    "fact_sip_inflows",
    engine,
    if_exists="replace",
    index=False,
)

print("✓ fact_sip_inflows loaded")

# ==========================================
# FACT CATEGORY INFLOWS
# ==========================================

cat.to_sql(
    "fact_category_inflows",
    engine,
    if_exists="replace",
    index=False,
)

print("✓ fact_category_inflows loaded")

# ==========================================
# FACT INDUSTRY FOLIO
# ==========================================

folio.to_sql(
    "fact_folio_count",
    engine,
    if_exists="replace",
    index=False,
)

print("✓ fact_folio_count loaded")

# ==========================================
# FACT PORTFOLIO HOLDINGS
# ==========================================

portfolio.to_sql(
    "fact_portfolio_holdings",
    engine,
    if_exists="replace",
    index=False,
)

print("✓ fact_portfolio_holdings loaded")

# ==========================================
# FACT BENCHMARK
# ==========================================

benchmark.to_sql(
    "fact_benchmark",
    engine,
    if_exists="replace",
    index=False,
)

print("✓ fact_benchmark loaded")

print("\n===================================")
print(" STAR SCHEMA LOADED SUCCESSFULLY ")
print("===================================")