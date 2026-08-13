"""
Bluestock Mutual Fund Database Loader.

Loads cleaned CSV datasets from Data/processed into the
Bluestock Mutual Fund SQLite database.
"""

import sqlite3
from pathlib import Path

import pandas as pd


# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATABASE_PATH = PROJECT_ROOT / "bluestock_mf.db"
PROCESSED_DATA_FOLDER = PROJECT_ROOT / "Data" / "processed"


# Mapping of SQLite table names to processed CSV files
DATASETS = {
    "fund_master": "clean_fund_master.csv",
    "nav_history": "clean_nav.csv",
    "aum_by_fund_house": "clean_aum.csv",
    "monthly_sip_inflows": "clean_monthly_sip.csv",
    "category_inflows": "clean_category_inflows.csv",
    "industry_folio_count": "clean_industry_folio.csv",
    "scheme_performance": "clean_performance.csv",
    "investor_transactions": "clean_transactions.csv",
    "portfolio_holdings": "clean_portfolio_holdings.csv",
    "benchmark_indices": "clean_benchmark_indices.csv",
}


def load_dataset(
    connection: sqlite3.Connection,
    table_name: str,
    file_name: str,
) -> int:
    """
    Load a processed CSV file into a SQLite table.

    Parameters
    ----------
    connection : sqlite3.Connection
        Active SQLite database connection.

    table_name : str
        Destination SQLite table name.

    file_name : str
        Name of the processed CSV file.

    Returns
    -------
    int
        Number of rows loaded.
    """

    file_path = PROCESSED_DATA_FOLDER / file_name

    if not file_path.exists():
        raise FileNotFoundError(
            f"Processed file not found: {file_path}"
        )

    dataframe = pd.read_csv(file_path)

    dataframe.to_sql(
        table_name,
        connection,
        if_exists="replace",
        index=False,
    )

    return len(dataframe)


def load_all_datasets():
    """Load all processed datasets into the SQLite database."""

    if not PROCESSED_DATA_FOLDER.exists():
        raise FileNotFoundError(
            f"Processed data folder not found: "
            f"{PROCESSED_DATA_FOLDER}"
        )

    connection = sqlite3.connect(DATABASE_PATH)

    loaded_tables = 0
    total_rows = 0

    try:
        for table_name, file_name in DATASETS.items():

            try:
                row_count = load_dataset(
                    connection,
                    table_name,
                    file_name,
                )

                loaded_tables += 1
                total_rows += row_count

                print(
                    f"✓ {table_name:<30} "
                    f"{row_count:,} rows"
                )

            except FileNotFoundError as error:

                print(f"✗ {error}")

        connection.commit()

    finally:
        connection.close()

    return loaded_tables, total_rows


def main():
    """Run the complete database loading process."""

    print("Loading processed datasets into SQLite...")
    print(f"Database: {DATABASE_PATH}")

    loaded_tables, total_rows = load_all_datasets()

    print(
        f"\nCompleted: {loaded_tables}/{len(DATASETS)} "
        f"tables loaded."
    )

    print(
        f"Total rows loaded: {total_rows:,}"
    )


if __name__ == "__main__":
    main()