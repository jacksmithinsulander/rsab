import mysql.connector
from mysql.connector import Error
import apiKeys


def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


connection = create_connection(
    "192.168.0.237", apiKeys.sql_user, apiKeys.sql_pass, "wagmi")
