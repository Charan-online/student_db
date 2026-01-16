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
        print("Student added ✅")  # Only prints if insert succeeds
    except sqlite3.IntegrityError:
        conn.rollback()
        print("Failed to add ❌ \n Roll No or Email already exists!")
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
        affected = 0
        if name:
            cursor.execute("UPDATE students SET name = ? WHERE roll_no = ?", (name, roll_no))
            affected += cursor.rowcount
        if email:
            cursor.execute("UPDATE students SET email = ? WHERE roll_no = ?", (email, roll_no))
            affected += cursor.rowcount
        if branch:
            cursor.execute("UPDATE students SET branch = ? WHERE roll_no = ?", (branch, roll_no))
            affected += cursor.rowcount

        conn.commit()

        if affected > 0:
            print("Student updated ✅")
        else:
            print("Failed to update ❌ \n Roll No not found!")

    except sqlite3.IntegrityError:
        conn.rollback()
        print("Failed to update ❌\n Email already exists!")
    finally:
        conn.close()


# Delete a student by Roll No
def delete_student(roll_no):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE roll_no = ?", (roll_no,))
    conn.commit()
    conn.close()
    print("Student deleted ✅")
    
def student_exists(roll_no):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM students WHERE roll_no = ?", (roll_no,))
    result = cursor.fetchone()
    conn.close()
    return result is not None