import pandas as pd
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

NAV_FILE = BASE_DIR / "Data" / "raw" / "02_nav_history.csv"
FUND_FILE = BASE_DIR / "Data" / "raw" / "01_fund_master.csv"

# Load data
nav = pd.read_csv(NAV_FILE)
fund_master = pd.read_csv(FUND_FILE)

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(
    ["amfi_code", "date"]
)

# Daily returns
nav["daily_return"] = (
    nav.groupby("amfi_code")["nav"]
    .pct_change()
)

# 90-day rolling Sharpe
nav["rolling_mean"] = (
    nav.groupby("amfi_code")["daily_return"]
    .transform(lambda x: x.rolling(90).mean())
)

nav["rolling_std"] = (
    nav.groupby("amfi_code")["daily_return"]
    .transform(lambda x: x.rolling(90).std())
)

nav["rolling_sharpe_90"] = (
    nav["rolling_mean"] /
    nav["rolling_std"]
) * np.sqrt(252)

# Average Sharpe by fund
fund_sharpe = (
    nav.groupby("amfi_code")["rolling_sharpe_90"]
    .mean()
    .reset_index(name="sharpe_ratio")
)

# Annualized volatility
fund_risk = (
    nav.groupby("amfi_code")["daily_return"]
    .std()
    .mul(np.sqrt(252))
    .mul(100)
    .reset_index(name="annualized_risk_pct")
)

# Create Low / Moderate / High grades
fund_risk["risk_grade"] = pd.qcut(
    fund_risk["annualized_risk_pct"],
    q=3,
    labels=["Low", "Moderate", "High"],
    duplicates="drop"
)

# Combine risk + Sharpe
fund_sharpe = fund_sharpe.merge(
    fund_risk,
    on="amfi_code",
    how="left"
)

# Add fund information
fund_sharpe = fund_sharpe.merge(
    fund_master[
        [
            "amfi_code",
            "scheme_name",
            "fund_house",
            "category"
        ]
    ],
    on="amfi_code",
    how="left"
)


def recommend_funds(risk_appetite):

    risk_appetite = risk_appetite.strip().title()

    if risk_appetite not in ["Low", "Moderate", "High"]:
        raise ValueError(
            "Enter Low, Moderate, or High."
        )

    result = (
        fund_sharpe[
            fund_sharpe["risk_grade"].astype(str)
            == risk_appetite
        ]
        .sort_values(
            "sharpe_ratio",
            ascending=False
        )
        .head(3)
    )

    return result[
        [
            "scheme_name",
            "fund_house",
            "category",
            "risk_grade",
            "annualized_risk_pct",
            "sharpe_ratio"
        ]
    ]


if __name__ == "__main__":

    print("\n=== Mutual Fund Recommender ===")
    print("Risk options: Low / Moderate / High")

    risk = input(
        "Enter your risk appetite: "
    )

    try:

        result = recommend_funds(risk)

        if result.empty:
            print("No matching funds found.")
        else:
            print("\nTop 3 Recommended Funds:\n")
            print(result.to_string(index=False))

    except ValueError as error:
        print(f"Error: {error}")