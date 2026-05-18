import pandas as pd
transactions_df = pd.read_csv("data/raw/transactions.csv")

def calculate_risk_score(row):

    score = 0

    if row["amount"] > 200000:
        score += 50

    if row["is_suspicious"] == True:
        score += 40

    return score

transactions_df["risk_score"] = transactions_df.apply(
    calculate_risk_score,
    axis=1
)

high_risk = transactions_df.sort_values(
    by="risk_score",
    ascending=False
)

print(
    high_risk[
        [
            "transaction_id",
            "amount",
            "is_suspicious",
            "risk_score"
        ]
    ].head(10)
)