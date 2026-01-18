import sqlite3
from werkzeug.security import generate_password_hash

def connect_db():
    return sqlite3.connect("students.db")

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    # Students table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        roll_no TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        branch TEXT NOT NULL,
        password TEXT NOT NULL
    )
    """)

    # Admins table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS admins (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    # Create default admin if not exists
    cursor.execute("INSERT OR IGNORE INTO admins (username, password) VALUES (?, ?)",
                   ("admin", generate_password_hash("admin123")))
    
    conn.commit()
    conn.close()
