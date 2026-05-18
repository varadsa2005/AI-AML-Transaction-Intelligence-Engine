import streamlit as st
import pandas as pd

transactions_df = pd.read_csv(
    "data/raw/transactions.csv"
)

st.title("Transactions Monitoring")

st.dataframe(transactions_df)