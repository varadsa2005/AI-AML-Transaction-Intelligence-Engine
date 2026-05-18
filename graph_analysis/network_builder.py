import pandas as pd

import networkx as nx
transactions_df = pd.read_csv("data/raw/transactions.csv")
G = nx.DiGraph()

for _, row in transactions_df.iterrows():

    G.add_edge(
        row["sender_account"],
        row["receiver_account"],
        amount=row["amount"]
    )

    print("Total Nodes:", G.number_of_nodes())

print("Total Edges:", G.number_of_edges())

print("\nSample Transaction Connections:\n")

edges = list(G.edges(data=True))

print(edges[:10])