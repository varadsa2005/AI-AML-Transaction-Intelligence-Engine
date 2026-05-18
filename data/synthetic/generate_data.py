import random
from faker import Faker
import pandas as pd


fake = Faker()

def generate_users(num_users=100):

    users = []

    risk_categories = ["Low", "Medium", "High"]

    kyc_statuses = ["Verified", "Pending"]

    countries = [
        "India",
        "USA",
        "UK",
        "UAE",
        "Singapore"
    ]

    for user_id in range(1, num_users + 1):

        user = {
            "user_id": user_id,
            "full_name": fake.name(),
            "email": fake.email(),
            "country": random.choice(countries),
            "kyc_status": random.choice(kyc_statuses),
            "risk_category": random.choice(risk_categories)
        }

        users.append(user)

    return pd.DataFrame(users)

def generate_accounts(users_df):

    accounts = []

    account_types = [
        "Savings",
        "Current",
        "Business"
    ]

    statuses = [
        "Active",
        "Blocked"
    ]

    account_id = 1

    for _, user in users_df.iterrows():

        num_accounts = random.randint(1, 3)

        for _ in range(num_accounts):

            account = {
                "account_id": account_id,
                "user_id": user["user_id"],
                "account_type": random.choice(account_types),
                "balance": round(random.uniform(1000, 500000), 2),
                "account_status": random.choice(statuses)
            }

            accounts.append(account)

            account_id += 1

    return pd.DataFrame(accounts)

def generate_transactions(accounts_df, num_transactions=1000):

    transactions = []

    transaction_types = [
        "UPI",
        "Bank Transfer",
        "Wallet Transfer",
        "Card Payment"
    ]

    locations = [
        "Mumbai",
        "Delhi",
        "Dubai",
        "Singapore",
        "London",
        "New York"
    ]

    for transaction_id in range(1, num_transactions + 1):

        sender = random.choice(accounts_df["account_id"].tolist())

        receiver = random.choice(accounts_df["account_id"].tolist())

        while sender == receiver:
            receiver = random.choice(accounts_df["account_id"].tolist())

        is_suspicious = random.random() < 0.05

        if is_suspicious:
            amount = round(random.uniform(200000, 1000000), 2)
        else:
            amount = round(random.uniform(100, 100000), 2)

        transaction = {
            "transaction_id": transaction_id,
            "sender_account": sender,
            "receiver_account": receiver,
            "amount": amount,
            "transaction_type": random.choice(transaction_types),
            "location": random.choice(locations),
            "device_id": fake.uuid4(),
            "ip_address": fake.ipv4(),
            "is_suspicious": is_suspicious
        }

        transactions.append(transaction)

    return pd.DataFrame(transactions)

if __name__ == "__main__":

    users_df = generate_users(100)

    accounts_df = generate_accounts(users_df)

    transactions_df = generate_transactions(accounts_df)

    print(users_df.head())

    print(accounts_df.head())

    print(transactions_df.head())

    print("\nSuspicious Transactions:\n")

    print(
        transactions_df[
            transactions_df["is_suspicious"] == True
        ].head()
    )

    users_df.to_csv("data/raw/users.csv", index=False)

accounts_df.to_csv("data/raw/accounts.csv", index=False)

transactions_df.to_csv("data/raw/transactions.csv", index=False)

print("\nCSV files saved successfully!")