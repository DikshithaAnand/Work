
import sqlite3

def get_connection():
    return sqlite3.connect("tasks.db", check_same_thread=False)

def init_db():
    conn = get_connection()
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE
    )
    """)

    c.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        category TEXT,
        task_name TEXT,
        date TEXT,
        start_time TEXT,
        end_time TEXT,
        duration REAL
    )
    """)

    conn.commit()
    conn.close()
