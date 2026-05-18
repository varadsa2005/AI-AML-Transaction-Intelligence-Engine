import pandas as pd

import networkx as nx

transactions_df = pd.read_csv("data/raw/transactions.csv")
G = nx.DiGraph()

suspicious_transactions = transactions_df[
    transactions_df["is_suspicious"] == True
]

for _, row in suspicious_transactions.iterrows():

    G.add_edge(
        row["sender_account"],
        row["receiver_account"],
        amount=row["amount"]
    )

print(
    "Suspicious Network Nodes:",
    G.number_of_nodes()
)

print(
    "Suspicious Network Edges:",
    G.number_of_edges()
)

degrees = dict(G.degree())

sorted_degrees = sorted(
    degrees.items(),
    key=lambda x: x[1],
    reverse=True
)

print("\nHighly Connected Suspicious Accounts:\n")

print(sorted_degrees[:10])