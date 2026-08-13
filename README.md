# Bluestock Mutual Fund Analytics Capstone

An end-to-end mutual fund analytics project that combines data ingestion, ETL, exploratory data analysis, performance measurement, risk analytics, investor analytics, portfolio concentration analysis, fund recommendation, and an interactive Power BI dashboard.

---

## Project Overview

The objective of this project is to build a comprehensive analytics solution for Indian mutual funds.

The project processes mutual fund datasets covering:

- Fund master information
- Historical NAV
- Assets Under Management (AUM)
- SIP inflows
- Category inflows
- Investor folios
- Scheme performance
- Investor transactions
- Portfolio holdings
- Benchmark indices

The processed data is analyzed using Python, SQLite, and Power BI to generate actionable insights for investors, fund managers, and financial analysts.

**At a glance:**

| Metric | Value |
|---|---|
| Funds analysed | 40 (10 fund houses) |
| Investors / transactions | 5,000 / 32,778 |
| NAV history | 46,000+ daily observations, 2022–2026 |
| Equity funds in HHI analysis | 34 |
| Avg. 3-Yr CAGR | 14.09% |
| Avg. Sharpe ratio | 1.36 |
| Total industry AUM | ₹62,74,000 Cr |
| Latest monthly SIP inflow | ₹31,002 Cr (17.17% YoY growth) |

---

## Objectives

The project focuses on the following objectives:

1. Analyze mutual fund industry-level trends.
2. Evaluate fund performance and risk-adjusted returns.
3. Analyze historical NAV and benchmark performance.
4. Understand investor transaction behavior.
5. Analyze SIP inflows and investor continuity.
6. Calculate Historical VaR and CVaR.
7. Calculate rolling 90-day Sharpe ratios.
8. Analyze investor cohorts.
9. Identify SIP investors at risk of discontinuation.
10. Measure sector concentration using HHI.
11. Build a risk-based mutual fund recommender.
12. Develop an interactive Power BI dashboard.

---

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Data processing and analytics |
| Pandas | Data cleaning and transformation |
| NumPy | Numerical calculations |
| Matplotlib | Data visualization |
| SQLite | Database storage |
| SQLAlchemy | Database connectivity |
| Jupyter Notebook | Advanced analytics |
| Power BI | Interactive dashboard |
| Git | Version control |
| GitHub | Project repository |

---

## Project Architecture

```text
Raw CSV Datasets
       |
       v
Data Ingestion
       |
       v
Data Cleaning & Validation
       |
       v
Processed CSV Files
       |
       v
SQLite Database
       |
       v
Star Schema
       |
       +-------------------+
       |                   |
       v                   v
Python Analytics       Power BI
       |                   |
       v                   v
Risk / Investor       Interactive
Performance           Dashboard
Analytics
       |
       v
Reports & Insights
```

---

## Repository Structure

```
bluestock-mf-capstone/
├── data/
│   ├── raw/                          # 01_fund_master.csv ... 10_benchmark_indices.csv
│   └── bluestock_mf.db               # SQLite warehouse (raw + star schema)
├── notebooks/                        # Jupyter notebooks: cleaning, EDA, analytics
├── dashboard/
│   └── bluestock_mf_dashboard.pbix   # Power BI dashboard (5 pages)
├── reports/
│   ├── Final_Report.pdf              # 20-page capstone report
│   └── Bluestock_MF_Presentation.pptx
├── assets/                           # Dashboard screenshots, generated charts
├── requirements.txt
└── README.md
```

---

## Data Sources

Ten structured datasets, cleaned and loaded into the SQLite warehouse (`bluestock_mf.db`) with both a normalized operational schema and a star schema (`dim_fund`, `dim_date`, `fact_*` tables) for BI consumption.

| # | Dataset | Rows | Description |
|---|---|---|---|
| 1 | `01_fund_master.csv` | 40 | Fund attributes: house, category, plan, launch date, benchmark, expense ratio, risk grade |
| 2 | `02_nav_history.csv` | 46,000 | Daily NAV per scheme, 2022–2026 |
| 3 | `03_aum_by_fund_house.csv` | 90 | Quarterly AUM and scheme count per fund house |
| 4 | `04_monthly_sip_inflows.csv` | 48 | Monthly industry-wide SIP inflow, active accounts, SIP AUM |
| 5 | `05_category_inflows.csv` | 144 | Monthly net inflow by fund category |
| 6 | `06_industry_folio_count.csv` | 21 | Total and category-wise investor folio counts over time |
| 7 | `07_scheme_performance.csv` | 40 | CAGR, Sharpe, Sortino, alpha, beta, drawdown, risk grade per scheme |
| 8 | `08_investor_transactions.csv` | 32,778 | Investor-level SIP / lumpsum / redemption transactions |
| 9 | `09_portfolio_holdings.csv` | 322 | Stock-level portfolio holdings and sector weights per equity fund |
| 10 | `10_benchmark_indices.csv` | 8,050 | Daily closing levels for benchmark indices (NIFTY 50, NIFTY 100, etc.) |

---

## Getting Started

### Prerequisites
- Python 3.11+
- Power BI Desktop (Windows) to open the `.pbix` dashboard
- Jupyter (included in `requirements.txt`)

### Setup

```bash
# Clone the repository
git clone https://github.com/<your-username>/bluestock-mf-capstone.git
cd bluestock-mf-capstone

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter to explore the notebooks
jupyter lab
```

### Running the analysis

1. Open the notebooks in `notebooks/` in order (cleaning → EDA → performance → risk → recommender)
2. Each notebook reads from and/or writes to `data/bluestock_mf.db` via SQLAlchemy
3. Open `dashboard/bluestock_mf_dashboard.pbix` in Power BI Desktop and hit **Refresh** to pull the latest data from the SQLite warehouse

---

## Dashboard

The Power BI dashboard is organized into 5 pages:

| Page | Contents |
|---|---|
| **Page 1 — Industry Overview** | Total AUM, SIP inflow, folios, scheme count; industry AUM trend; AUM by fund house |
| **Page 2 — Fund Performance** | Return-vs-risk scatter, fund scorecard table, CAGR/Sharpe/Alpha/Expense Ratio/Drawdown/Fund Score KPIs — filterable by fund house, category, plan and scheme |
| **NAV Detail** *(drill-through)* | NAV history for any selected scheme |
| **Page 3 — Investor Analytics** | Transaction value by state, average SIP by age group, transaction-type split, monthly transaction volume — filterable by state, age group and city tier |
| **Page 4 — SIP & Market Trends** | SIP inflow vs. NIFTY 50, monthly SIP trend, SIP AUM trend, category inflow heatmap, top-5 categories by net inflow, SIP account growth |

---

## Key Findings

- **Highest downside risk:** small-cap equity funds (SBI, Axis, ABSL, Nippon India Small Cap) show the worst 95% VaR/CVaR, and several funds carry maximum drawdowns near ‑33%
- **SIP continuity:** only 28.6% of SIP investors have made 6+ contributions; 73.9% are classified At-Risk under a 35-day-since-last-SIP rule
- **Best risk-adjusted funds:** Mirae Asset Large Cap, ICICI Pru Midcap and Kotak Flexicap lead the composite fund-score ranking
- **Sector concentration:** 3 equity funds exceed an HHI of 2,500 against a 34-fund average HHI of 2,029, flagging a diversification review

Full methodology, formulas and results are in [`reports/Final_Report.pdf`](reports/Final_Report.pdf).

---

## Limitations & Future Scope

**Limitations:** all metrics are backward-looking; portfolio-holdings data reflects a single snapshot per fund; historical VaR does not guarantee future risk; the fund recommender is rule-based (Sharpe-only ranking within a risk-grade pool); dataset coverage is a representative but partial slice of the industry.

**Future scope:** machine-learning-based fund recommendations, real-time NAV and benchmark integration, automated threshold alerts, and a predictive SIP-churn model.

---

## Author
 Anuj Kunturwar
Data Engineering Capstone Project, in association with Bluestock.in

## License

This project is submitted as an academic capstone. Data used is illustrative/synthetic for educational purposes.