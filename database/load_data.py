import pandas as pd
from db_connection import create_connection

connection = create_connection()

cursor = connection.cursor()

users_df = pd.read_csv("data/raw/users.csv")

accounts_df = pd.read_csv("data/raw/accounts.csv")

transactions_df = pd.read_csv("data/raw/transactions.csv")

# for _, row in users_df.iterrows():

#     query = """
#     INSERT INTO users
#     (user_id, full_name, email, country, kyc_status, risk_category)
#     VALUES (%s, %s, %s, %s, %s, %s)
#     """

#     values = (
#         int(row["user_id"]),
#         row["full_name"],
#         row["email"],
#         row["country"],
#         row["kyc_status"],
#         row["risk_category"]
#     )

#     cursor.execute(query, values)

# connection.commit()

# print("Users data inserted successfully!")

for _, row in accounts_df.iterrows():

    query = """
    INSERT INTO accounts
    (account_id, user_id, account_type, balance, account_status)
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        int(row["account_id"]),
        int(row["user_id"]),
        row["account_type"],
        float(row["balance"]),
        row["account_status"]
    )

    cursor.execute(query, values)

connection.commit()

print("Accounts data inserted successfully!")

for _, row in transactions_df.iterrows():

    query = """
    INSERT INTO transactions
    (
        transaction_id,
        sender_account,
        receiver_account,
        amount,
        transaction_type,
        location,
        device_id,
        ip_address,
        is_suspicious
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        int(row["transaction_id"]),
        int(row["sender_account"]),
        int(row["receiver_account"]),
        float(row["amount"]),
        row["transaction_type"],
        row["location"],
        row["device_id"],
        row["ip_address"],
        bool(row["is_suspicious"])
    )

    cursor.execute(query, values)

connection.commit()

print("Transactions data inserted successfully!")