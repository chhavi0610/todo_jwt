import psycopg2
import os

DATABASE_URL = os.getenv("DATABASE_URL")

def connection():
        return psycopg2.connect(DATABASE_URL)



def create_table_user():
    conn = connection()
    
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()


def create_table_task():
    conn = connection()
    if conn is None:
        return

    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks ( id SERIAL PRIMARY KEY, title TEXT NOT NULL );""")
    conn.commit()
    cursor.close()
    conn.close()
