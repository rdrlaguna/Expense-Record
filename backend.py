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
        return 
    

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
            );
            CREATE UNIQUE INDEX category_name ON categories (category_name)
        ''')
        conn.commit()
        cursor.close()
    except sqlite3.Error as err:
        print(f"Error creating categories table: {err}")
        return 


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
        raise sqlite3.Error(f"{err}")


def create_category(name=''):
    try:
        insert_query= "INSERT INTO categories (name) VALUES (?)"
        params = name
        execute_query(insert_query, params)
        return f"{name} added to categories"
    
    except sqlite3.Error as err:
        return f"Error executing query: {err}"