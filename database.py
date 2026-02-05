import psycopg2
import os

DATABASE_URL = os.getenv("DATABASE_URL")

def connection():
    try:
        return psycopg2.connect(DATABASE_URL)
    except Exception as e:
        print("Database connection failed:", e)
        return None


def create_table_user():
    conn = connection()
    
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
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
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()
