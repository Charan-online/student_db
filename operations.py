import sqlite3
from database import connect_db

# Add a new student
def add_student(roll_no, name, email, branch):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO students (roll_no, name, email, branch) VALUES (?, ?, ?, ?)",
            (roll_no, name, email, branch)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

# View all students
def view_students():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Update student info by Roll No
def update_student(roll_no, name=None, email=None, branch=None):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        if name:
            cursor.execute("UPDATE students SET name = ? WHERE roll_no = ?", (name, roll_no))
        if email:
            cursor.execute("UPDATE students SET email = ? WHERE roll_no = ?", (email, roll_no))
        if branch:
            cursor.execute("UPDATE students SET branch = ? WHERE roll_no = ?", (branch, roll_no))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

# Delete a student by Roll No
def delete_student(roll_no):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE roll_no = ?", (roll_no,))
    conn.commit()
    conn.close()
