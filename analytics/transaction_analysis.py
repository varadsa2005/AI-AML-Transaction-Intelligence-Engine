import pandas as pd
transactions_df = pd.read_csv("data/raw/transactions.csv")

total_volume = transactions_df["amount"].sum()

print("Total Transaction Volume:", total_volume)

total_transactions = len(transactions_df)

print("Total Transactions:", total_transactions)

suspicious_transactions = transactions_df[
    transactions_df["is_suspicious"] == True
]

suspicious_count = len(suspicious_transactions)

print("Suspicious Transactions:", suspicious_count)

suspicious_percentage = (
    suspicious_count / total_transactions
) * 100

print("Suspicious Percentage:", suspicious_percentage)

average_transaction = transactions_df["amount"].mean()

print("Average Transaction Amount:", average_transaction)