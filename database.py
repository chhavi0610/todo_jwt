import psycopg2

DATABASE_URL = "postgresql://postgres:Chhavi%40123@localhost:5432/todo"

def connection():
        conn = psycopg2.connect(DATABASE_URL)
        return conn
 

def create_table_task():
    conn = connection()
    if conn is None:
        print("Skipping table creation: DB not available")
        return
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS task(
            id INTEGER PRIMARY KEY, title TEXT NOT NULL )""")

    conn.commit()
    cursor.close()
    conn.close()
    print("task table ready")

def create_table_user():
    conn = connection()
    if conn is None:
        print("Skipping table creation: DB not available")
        return
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY,name TEXT NOT NULL, email TEXT UNIQUE NOT NULL,
            hashed_password TEXT NOT NULL)  """)

    conn.commit()
    cursor.close()
    conn.close()
    print("users table ready")


