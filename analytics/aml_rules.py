import pandas as pd
transactions_df = pd.read_csv("data/raw/transactions.csv")

high_value_transactions = transactions_df[
    transactions_df["amount"] > 200000
]

print(
    "High Value Transactions:",
    len(high_value_transactions)
)

print("\nSample High Value Transactions:\n")

print(
    high_value_transactions[
        [
            "transaction_id",
            "sender_account",
            "receiver_account",
            "amount"
        ]
    ].head()
)