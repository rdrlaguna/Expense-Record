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
        ''')
        # Allow only unique categoy names
        cursor.execute('''
                CREATE UNIQUE INDEX category_name ON categories (category_name);
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

        conn.commit()
        # Get results
        results = cursor.fetchall()
        cursor.close()
        return results
    
    except sqlite3.Error as err:
        raise sqlite3.Error(f"{err}")


def create_category(name=''):
    """ Add category to table or crete table if not exists. """
    try:
        insert_query= "INSERT INTO categories (category_name) VALUES (?)"
        params = (name,)
        execute_query(insert_query, params)
        return f"{name[0]} added to categories"
    
    except sqlite3.Error as err:
        # Create table if it does not exist
        if "no such table:" in str(err):
            create_categories_table()
            return "Categories table created. Add category again"

        print(err)
        return f"Error executing query: {err}"
    

def get_all_categories():
    """ Get a list of all categories in database """
    select_query = "SELECT * FROM categories ORDER BY category_name ASC"
    results = execute_query(select_query)
    return {"status": 0, "results": results}


def delete_category(category_id):
    """ Delete a category by its id """
    delete_query = "DELETE FROM categories WHERE id = ?"
    params = (category_id,)
    execute_query(delete_query, params)
    return {"status": 0, "results": "Category deleted"}