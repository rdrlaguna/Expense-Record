import sqlite3
from datetime import datetime


def database_connect():
    """ Connect to the database """

    try:
        # Connect or create database
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
        return f"Error creating categories table: {err}"


def execute_query(query, params=None):
    """ Execute a SQL query """

    try:
        conn = database_connect()
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        
        # Get results
        results = cursor.fetchall()
        cursor.close()
        return results
    
    except sqlite3.Error as err:
        return f"Error executing query: {err}"


def create_category(name=''):
    insert_query= "INSERT INTO categories (name) VALUES (?)"
    params = name
    execute_query(insert_query, params)
    return f"{name} added to categories"