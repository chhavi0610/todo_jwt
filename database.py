import psycopg2
import os

DATABASE_URL = os.getenv("DATABASE_URL")

def connection():
    if os.getenv("TESTING") == "true":
        raise Exception("DB disabled during tests")

    return psycopg2.connect(
        host=os.getenv("DB_HOST", "postgres"),
        port=5432,
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "postgres"),
        dbname=os.getenv("DB_NAME", "postgres"),
    )



def create_table_user():
    conn = connection()
    
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
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
        CREATE TABLE IF NOT EXISTS tasks ( id INTEGER PRIMARY KEY, title TEXT NOT NULL );""")
    conn.commit()
    cursor.close()
    conn.close()
