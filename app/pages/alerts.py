import streamlit as st
import pandas as pd

transactions_df = pd.read_csv(
    "data/raw/transactions.csv"
)

alerts = []

for _, row in transactions_df.iterrows():

    if row["amount"] > 200000:

        alerts.append({
            "transaction_id": row["transaction_id"],
            "alert_type": "High Value Transaction",
            "amount": row["amount"],
            "status": "Open"
        })

    if row["is_suspicious"] == True:

        alerts.append({
            "transaction_id": row["transaction_id"],
            "alert_type": "Suspicious Transaction",
            "amount": row["amount"],
            "status": "Critical"
        })

alerts_df = pd.DataFrame(alerts)

st.title("AML Alerts Dashboard")

st.metric(
    "Total Alerts",
    len(alerts_df)
)

st.dataframe(alerts_df)