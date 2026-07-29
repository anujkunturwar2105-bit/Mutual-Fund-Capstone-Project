import sqlite3
import pandas as pd
from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Database path
DB_PATH = BASE_DIR / "bluestock_mf.db"

# Processed data folder
PROCESSED_DIR = BASE_DIR / "Data" / "processed"

# Connect to SQLite database
conn = sqlite3.connect(DB_PATH)

# Mapping of table names to processed CSV files
datasets = {
    "fund_master": "clean_fund_master.csv",
    "nav_history": "clean_nav.csv",
    "aum_by_fund_house": "clean_aum.csv",
    "monthly_sip_inflows": "clean_monthly_sip.csv",
    "category_inflows": "clean_category_inflows.csv",
    "industry_folio_count": "clean_industry_folio.csv",
    "scheme_performance": "clean_performance.csv",
    "investor_transactions": "clean_transactions.csv",
    "portfolio_holdings": "clean_portfolio_holdings.csv",
    "benchmark_indices": "clean_benchmark_indices.csv"
}

print("=" * 70)
print("LOADING CLEANED DATASETS INTO SQLITE")
print("=" * 70)

for table_name, file_name in datasets.items():

    file_path = PROCESSED_DIR / file_name

    if file_path.exists():

        df = pd.read_csv(file_path)

        # Load data into SQLite
        df.to_sql(
            table_name,
            conn,
            if_exists="replace",
            index=False
        )

        print(f"✅ {table_name:<30} Loaded ({len(df)} rows)")

    else:
        print(f"❌ Missing File : {file_name}")

conn.close()

print("\n" + "=" * 70)
print("ALL CLEANED DATASETS LOADED INTO SQLITE SUCCESSFULLY!")
print("=" * 70)