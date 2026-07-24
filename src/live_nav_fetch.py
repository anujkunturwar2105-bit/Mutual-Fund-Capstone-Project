import requests
import pandas as pd
import os

# Create output folder if it doesn't exist
os.makedirs("Data/raw", exist_ok=True)

schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for fund_name, scheme_code in schemes.items():

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        file_name = f"Data/raw/{fund_name}_NAV.csv"

        nav_df.to_csv(file_name, index=False)

        print(f"✓ {fund_name} downloaded successfully.")

    else:
        print(f"✗ Failed to fetch {fund_name}")