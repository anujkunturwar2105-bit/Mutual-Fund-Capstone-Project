"""
Bluestock Mutual Fund Star Schema Loader.

Creates dimension and fact tables in the SQLite database
using the cleaned datasets from Data/processed.
"""

from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine


# ---------------------------------------------------------------------
# Project paths
# ---------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent
PROCESSED_DATA_FOLDER = PROJECT_ROOT / "Data" / "processed"
DATABASE_PATH = PROJECT_ROOT / "bluestock_mf.db"


def create_database_engine():
    """Create and return a SQLAlchemy SQLite database engine."""

    return create_engine(
        f"sqlite:///{DATABASE_PATH}"
    )


def load_csv(filename):
    """
    Load a processed CSV file.

    Parameters
    ----------
    filename : str
        Name of the CSV file in Data/processed.

    Returns
    -------
    pandas.DataFrame
        Loaded dataset.
    """

    file_path = PROCESSED_DATA_FOLDER / filename

    if not file_path.exists():
        raise FileNotFoundError(
            f"Processed dataset not found: {file_path}"
        )

    return pd.read_csv(file_path)


def load_table(dataframe, table_name, engine):
    """
    Load a DataFrame into a SQLite table.

    Parameters
    ----------
    dataframe : pandas.DataFrame
        Dataset to load.

    table_name : str
        Destination table name.

    engine : sqlalchemy.Engine
        Database engine.

    Returns
    -------
    int
        Number of rows loaded.
    """

    dataframe.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False,
    )

    return len(dataframe)


def create_dim_fund(engine):
    """Create the fund dimension table."""

    fund = load_csv("clean_fund_master.csv")

    columns = [
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

    dim_fund = (
        fund[columns]
        .drop_duplicates()
    )

    return load_table(
        dim_fund,
        "dim_fund",
        engine,
    )


def create_dim_date(engine):
    """Create the date dimension from all relevant date fields."""

    date_sources = [
        ("clean_nav.csv", "date"),
        ("clean_transactions.csv", "transaction_date"),
        ("clean_aum.csv", "date"),
        ("clean_benchmark_indices.csv", "date"),
        ("clean_portfolio_holdings.csv", "portfolio_date"),
        ("clean_monthly_sip.csv", "month"),
        ("clean_category_inflows.csv", "month"),
        ("clean_industry_folio.csv", "month"),
    ]

    all_dates = []

    for filename, date_column in date_sources:

        dataframe = load_csv(filename)

        all_dates.extend(
            pd.to_datetime(
                dataframe[date_column],
                errors="coerce",
            )
        )

    dates = (
        pd.Series(all_dates)
        .dropna()
        .drop_duplicates()
        .sort_values()
        .reset_index(drop=True)
    )

    dim_date = pd.DataFrame(
        {
            "full_date": dates,
            "day": dates.dt.day,
            "month": dates.dt.month,
            "month_name": dates.dt.month_name(),
            "quarter": dates.dt.quarter,
            "year": dates.dt.year,
        }
    )

    return load_table(
        dim_date,
        "dim_date",
        engine,
    )


def create_fact_tables(engine):
    """Create all fact tables used by the star schema."""

    fact_datasets = {
        "fact_nav": "clean_nav.csv",
        "fact_transactions": "clean_transactions.csv",
        "fact_performance": "clean_performance.csv",
        "fact_aum": "clean_aum.csv",
        "fact_sip_inflows": "clean_monthly_sip.csv",
        "fact_category_inflows": "clean_category_inflows.csv",
        "fact_folio_count": "clean_industry_folio.csv",
        "fact_portfolio_holdings": "clean_portfolio_holdings.csv",
        "fact_benchmark": "clean_benchmark_indices.csv",
    }

    results = {}

    for table_name, filename in fact_datasets.items():

        dataframe = load_csv(filename)

        results[table_name] = load_table(
            dataframe,
            table_name,
            engine,
        )

    return results


def main():
    """Build the complete Bluestock Mutual Fund star schema."""

    print("Loading Bluestock Mutual Fund star schema...")
    print(f"Database: {DATABASE_PATH}")

    engine = create_database_engine()

    # Dimension tables
    dim_fund_rows = create_dim_fund(engine)
    dim_date_rows = create_dim_date(engine)

    print(
        f"✓ dim_fund loaded: {dim_fund_rows:,} rows"
    )

    print(
        f"✓ dim_date loaded: {dim_date_rows:,} rows"
    )

    # Fact tables
    fact_results = create_fact_tables(engine)

    for table_name, row_count in fact_results.items():
        print(
            f"✓ {table_name:<25} "
            f"{row_count:,} rows"
        )

    print("\nStar schema loaded successfully.")


if __name__ == "__main__":
    main()