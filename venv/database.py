print("running")

import sqlite3

print("imported")

def get_connection():
    print("trying to connect")
    return  sqlite3.connect("todos.db")

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS jar (id INTEGER PRIMARY KEY, title TEXT NOT NULL)""")
    table = cursor.fetchall()
    print(table)
    conn.commit()
    conn.close()
    print("ready table")

