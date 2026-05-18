import mysql.connector


def create_connection():

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_PASSWORD",
        database="ai_aml_engine"
    )

    return connection


if __name__ == "__main__":

    conn = create_connection()

    if conn.is_connected():
        print("Database connected successfully!")

    conn.close()