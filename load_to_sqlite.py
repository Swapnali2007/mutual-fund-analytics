import pandas as pd
from sqlalchemy import create_engine
import sqlite3

engine = create_engine("sqlite:///bluestock_mf.db")

# Load CSVs
fund = pd.read_csv("data/raw/01_fund_master.csv")
nav = pd.read_csv("data/processed/clean_nav_history.csv")
txn = pd.read_csv("data/processed/clean_transactions.csv")
perf = pd.read_csv("data/processed/clean_performance.csv")

# Load to SQLite
fund.to_sql("dim_fund", engine, if_exists="replace", index=False)
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
txn.to_sql("fact_transactions", engine, if_exists="replace", index=False)
perf.to_sql("fact_performance", engine, if_exists="replace", index=False)

print("Database Loaded Successfully")

# Verify Row Counts
conn = sqlite3.connect("bluestock_mf.db")

tables = {
    "dim_fund": len(fund),
    "fact_nav": len(nav),
    "fact_transactions": len(txn),
    "fact_performance": len(perf)
}

print("\nRow Count Verification")

for table, csv_rows in tables.items():
    db_rows = pd.read_sql(
        f"SELECT COUNT(*) as cnt FROM {table}",
        conn
    )["cnt"][0]

    print(
        f"{table}: CSV={csv_rows}, DB={db_rows}"
    )

conn.close()