# pip install mysql-connector-python
import mysql.connector

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='cyss2026',
            password='cyss2026',
            database='magazzino'
        )
        if connection.is_connected():
            print("Connected to the database successfully!")
            return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def close_database_connection(connection):
    if connection and connection.is_connected():
        connection.close()
        print("Database connection closed.")
    

if __name__ == "__main__":
    db_connection = connect_to_database()
    if db_connection:
        close_database_connection(db_connection)
        print("Database connection closed.")

