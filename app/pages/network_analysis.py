import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

transactions_df = pd.read_csv(
    "data/raw/transactions.csv"
)

st.title("Transaction Network Analysis")

G = nx.DiGraph()

suspicious_transactions = transactions_df[
    transactions_df["is_suspicious"] == True
]

for _, row in suspicious_transactions.iterrows():

    G.add_edge(
        row["sender_account"],
        row["receiver_account"]
    )

fig, ax = plt.subplots(figsize=(12, 8))

pos = nx.spring_layout(G)

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=500,
    font_size=8,
    ax=ax
)

st.pyplot(fig)

