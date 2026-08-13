"""
Bluestock Mutual Fund Data Ingestion Module.

Discovers CSV datasets in the raw data directory and validates
that they can be loaded successfully using pandas.
"""

from pathlib import Path
import pandas as pd


# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FOLDER = PROJECT_ROOT / "Data" / "raw"


def discover_csv_files(data_folder):
    """
    Find all CSV files in the specified data directory.

    Parameters
    ----------
    data_folder : Path
        Directory containing raw CSV files.

    Returns
    -------
    list[Path]
        List of CSV file paths.
    """
    return sorted(data_folder.glob("*.csv"))


def load_csv(file_path):
    """
    Load a CSV file into a pandas DataFrame.

    Parameters
    ----------
    file_path : Path
        Path to the CSV file.

    Returns
    -------
    pandas.DataFrame
        Loaded dataset.
    """
    return pd.read_csv(file_path)


def ingest_data():
    """
    Discover and validate all raw CSV datasets.

    Returns
    -------
    dict
        Dictionary containing loaded DataFrames keyed by filename.
    """

    if not DATA_FOLDER.exists():
        raise FileNotFoundError(
            f"Data directory not found: {DATA_FOLDER}"
        )

    csv_files = discover_csv_files(DATA_FOLDER)

    if not csv_files:
        raise FileNotFoundError(
            f"No CSV files found in: {DATA_FOLDER}"
        )

    datasets = {}

    for file_path in csv_files:
        datasets[file_path.name] = load_csv(file_path)

    return datasets


def main():
    """Run the data ingestion process."""

    datasets = ingest_data()

    print(
        f"Successfully loaded {len(datasets)} CSV datasets."
    )

    for filename, dataframe in datasets.items():
        print(
            f"  {filename}: "
            f"{len(dataframe):,} rows × "
            f"{len(dataframe.columns)} columns"
        )


if __name__ == "__main__":
    main()