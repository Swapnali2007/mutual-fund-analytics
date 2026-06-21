import requests
import pandas as pd
import os

# folder create if not exists
os.makedirs("data/raw", exist_ok=True)

schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for fund_name, code in schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)
    data = response.json()

    print("Fetching:", data["meta"]["scheme_name"])

    df = pd.DataFrame(data["data"])

    file_name = f"data/raw/{fund_name}.csv"
    df.to_csv(file_name, index=False)

    print(file_name, "saved successfully")

print("All 5 NAV files fetched")