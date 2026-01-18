import sqlite3
from database import connect_db
from werkzeug.security import generate_password_hash

# ---------------- STUDENT OPERATIONS ----------------
def add_student(roll_no, name, email, branch, password):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        hashed_pw = generate_password_hash(password)
        cursor.execute(
            "INSERT INTO students (roll_no, name, email, branch, password) VALUES (?, ?, ?, ?, ?)",
            (roll_no, name, email, branch, hashed_pw)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def view_students():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT roll_no, name, email, branch FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_student(roll_no, name=None, email=None, branch=None, password=None):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        if name:
            cursor.execute("UPDATE students SET name=? WHERE roll_no=?", (name, roll_no))
        if email:
            cursor.execute("UPDATE students SET email=? WHERE roll_no=?", (email, roll_no))
        if branch:
            cursor.execute("UPDATE students SET branch=? WHERE roll_no=?", (branch, roll_no))
        if password:
            hashed_pw = generate_password_hash(password)
            cursor.execute("UPDATE students SET password=? WHERE roll_no=?", (hashed_pw, roll_no))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def delete_student(roll_no):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE roll_no=?", (roll_no,))
    conn.commit()
    conn.close()
