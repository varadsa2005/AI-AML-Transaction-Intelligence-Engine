import pandas as pd
transactions_df = pd.read_csv("data/raw/transactions.csv")

transactions_df["high_amount_flag"] = (
    transactions_df["amount"] > 200000
).astype(int)

print(
    transactions_df[
        [
            "amount",
            "high_amount_flag"
        ]
    ].head(10)
)