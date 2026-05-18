import pandas as pd

from sklearn.ensemble import IsolationForest

transactions_df = pd.read_csv("data/raw/transactions.csv")

features = transactions_df[
    [
        "amount"
    ]
]

model = IsolationForest(
    contamination=0.05,
    random_state=42
)
model.fit(features)

transactions_df["anomaly_prediction"] = model.predict(features)

anomalies = transactions_df[
    transactions_df["anomaly_prediction"] == -1
]

print("Detected Anomalies:", len(anomalies))

print(
    anomalies[
        [
            "transaction_id",
            "amount",
            "is_suspicious",
            "anomaly_prediction"
        ]
    ].head()
)