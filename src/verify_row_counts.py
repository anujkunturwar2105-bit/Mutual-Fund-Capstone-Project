import sqlite3
import pandas as pd
from pathlib import Path

# ==========================================
# Paths
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "Data" / "processed"

DB_PATH = BASE_DIR / "bluestock_mf.db"

# ==========================================
# Database Connection
# ==========================================

conn = sqlite3.connect(DB_PATH)

# ==========================================
# CSV ↔ TABLE Mapping
# ==========================================

tables = {
    "clean_fund_master.csv": "dim_fund",
    "clean_nav.csv": "fact_nav",
    "clean_aum.csv": "fact_aum",
    "clean_monthly_sip.csv": "fact_sip_inflows",
    "clean_category_inflows.csv": "fact_category_inflows",
    "clean_industry_folio.csv": "fact_folio_count",
    "clean_performance.csv": "fact_performance",
    "clean_transactions.csv": "fact_transactions",
    "clean_portfolio_holdings.csv": "fact_portfolio_holdings",
    "clean_benchmark_indices.csv": "fact_benchmark",
}

print("=" * 70)
print("VERIFYING STAR SCHEMA ROW COUNTS")
print("=" * 70)

all_pass = True

for csv_file, table in tables.items():

    csv_path = DATA_DIR / csv_file

    csv_rows = len(pd.read_csv(csv_path))

    db_rows = pd.read_sql(
        f"SELECT COUNT(*) AS cnt FROM {table}",
        conn
    ).iloc[0]["cnt"]

    status = "PASS" if csv_rows == db_rows else "FAIL"

    if status == "FAIL":
        all_pass = False

    print(f"{table:<30} CSV={csv_rows:<8} DB={db_rows:<8} {status}")

print("=" * 70)

if all_pass:
    print("ALL TABLES VERIFIED SUCCESSFULLY")
else:
    print("WARNING: Some tables have row count mismatches.")

conn.close()