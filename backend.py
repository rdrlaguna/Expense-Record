import sqlite3
from datetime import datetime


def database_connect():
    """ Connect to the database """

    try:
        conn = sqlite3.connect('expenses.db')
        return conn
    except sqlite3.Error as err:
        print(f"Error connecting to the database: {err}")
        return None
    

    