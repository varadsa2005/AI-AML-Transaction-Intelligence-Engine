import streamlit as st
import pandas as pd

transactions_df = pd.read_csv(
    "data/raw/transactions.csv"
)

def calculate_risk(row):

    score = 0

    if row["amount"] > 200000:
        score += 50

    if row["is_suspicious"] == True:
        score += 40

    return score

transactions_df["risk_score"] = (
    transactions_df.apply(
        calculate_risk,
        axis=1
    )
)

st.title("Risk Intelligence Dashboard")

high_risk = transactions_df.sort_values(
    by="risk_score",
    ascending=False
)

st.subheader("Highest Risk Transactions")

st.dataframe(
    high_risk[
        [
            "transaction_id",
            "sender_account",
            "receiver_account",
            "amount",
            "risk_score",
            "is_suspicious"
        ]
    ].head(20)
)