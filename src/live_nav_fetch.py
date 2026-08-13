"""
Live Mutual Fund NAV Fetcher.

Fetches current historical NAV data for selected mutual fund schemes
using the MFAPI service and saves the results as CSV files.
"""

from pathlib import Path

import pandas as pd
import requests


# Project directories
PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_DATA_FOLDER = PROJECT_ROOT / "Data" / "raw"


# Selected mutual fund schemes
SCHEMES = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841,
}


def fetch_nav(scheme_code):
    """
    Fetch NAV data for a mutual fund scheme.

    Parameters
    ----------
    scheme_code : int
        AMFI scheme code used by MFAPI.

    Returns
    -------
    pandas.DataFrame
        NAV history returned by the API.

    Raises
    ------
    requests.HTTPError
        If the API returns an unsuccessful HTTP status.
    """
    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(
        url,
        timeout=30
    )

    response.raise_for_status()

    data = response.json()

    return pd.DataFrame(data["data"])


def save_nav_data(fund_name, nav_data):
    """
    Save NAV data to the raw data directory.

    Parameters
    ----------
    fund_name : str
        Name used for the output file.

    nav_data : pandas.DataFrame
        NAV history to save.

    Returns
    -------
    Path
        Path of the saved CSV file.
    """
    RAW_DATA_FOLDER.mkdir(
        parents=True,
        exist_ok=True
    )

    output_path = RAW_DATA_FOLDER / f"{fund_name}_NAV.csv"

    nav_data.to_csv(
        output_path,
        index=False
    )

    return output_path


def main():
    """Fetch and save NAV data for all configured schemes."""

    print("Starting live NAV data fetch...")

    successful = 0
    failed = 0

    for fund_name, scheme_code in SCHEMES.items():

        try:
            nav_data = fetch_nav(scheme_code)

            output_path = save_nav_data(
                fund_name,
                nav_data
            )

            print(
                f"✓ {fund_name}: "
                f"{len(nav_data):,} records saved"
            )

            successful += 1

        except requests.RequestException as error:

            print(
                f"✗ {fund_name}: API request failed "
                f"({error})"
            )

            failed += 1

        except (KeyError, ValueError) as error:

            print(
                f"✗ {fund_name}: Invalid API response "
                f"({error})"
            )

            failed += 1

    print("\nNAV fetch completed.")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")


if __name__ == "__main__":
    main()