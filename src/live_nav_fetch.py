import requests
import pandas as pd

# Example Scheme Code
scheme_code = 119551  # SBI Bluechip Fund

url = f"https://api.mfapi.in/mf/{scheme_code}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("Scheme Name:", data["meta"]["scheme_name"])

    nav_df = pd.DataFrame(data["data"])

    print(nav_df.head())

    nav_df.to_csv("Data/raw/SBI_Bluechip_NAV.csv", index=False)

    print("\nNAV data saved successfully in Data/raw/")
else:
    print("Failed to fetch data.")