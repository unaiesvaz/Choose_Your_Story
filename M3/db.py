import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="choose_user",
            password="choose_pass",
            database="choose_your_story"
        )
        return conn
    except Error as e:
        raise Exception(f"Error de conexión a MySQL: {e}")





