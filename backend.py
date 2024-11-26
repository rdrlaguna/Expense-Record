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
    

def create_categories_table():
    """ Create a categories table in database """

    try:
        # Connect to database
        conn = database_connect()
        cursor = conn.cursor()
        # Execute query
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                category_name TEXT NOT NULL
            )
        ''')
        conn.commit()
        cursor.close()
    except sqlite3.Error as err:
        print(f"Error creating notes table: {err}")


        