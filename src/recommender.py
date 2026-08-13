"""
Mutual Fund Recommendation Module

Provides mutual fund recommendations based on investor
risk appetite and Sharpe ratio.
"""

import pandas as pd


def recommend_funds(
    fund_data: pd.DataFrame,
    risk_appetite: str,
    top_n: int = 3
) -> pd.DataFrame:
    """
    Recommend top mutual funds based on risk appetite.

    Parameters
    ----------
    fund_data : pd.DataFrame
        Fund performance dataset.

    risk_appetite : str
        Investor risk preference:
        Low, Moderate, or High.

    top_n : int
        Number of funds to recommend.

    Returns
    -------
    pd.DataFrame
        Recommended funds sorted by Sharpe ratio.
    """

    valid_risk_levels = ["Low", "Moderate", "High"]

    if risk_appetite not in valid_risk_levels:
        raise ValueError(
            "Risk appetite must be Low, Moderate, or High."
        )

    filtered_funds = fund_data[
        fund_data["risk_grade"] == risk_appetite
    ].copy()

    if filtered_funds.empty:
        return pd.DataFrame()

    recommendations = (
        filtered_funds
        .sort_values(
            "sharpe_ratio",
            ascending=False
        )
        .head(top_n)
    )

    return recommendations


def main():
    """Run a basic test of the recommender module."""

    print("Fund recommender module loaded successfully.")


if __name__ == "__main__":
    main()