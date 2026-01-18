from flask import Flask, render_template, request, redirect, url_for, flash, session
from operations import add_student, view_students, update_student, delete_student
from database import create_tables
from werkzeug.security import check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = "supersecretkey"

create_tables()

# ---------------- LOGIN ----------------
@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        role = request.form["role"]
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("students.db")
        cursor = conn.cursor()

        if role == "admin":
            cursor.execute("SELECT password FROM admins WHERE username=?", (username,))
            result = cursor.fetchone()
            conn.close()
            if result and check_password_hash(result[0], password):
                session["admin"] = username
                return redirect(url_for("admin_home"))
            else:
                flash("Invalid admin credentials", "error")

        elif role == "student":
            cursor.execute("SELECT password FROM students WHERE roll_no=?", (username,))
            result = cursor.fetchone()
            conn.close()
            if result and check_password_hash(result[0], password):
                session["student"] = username
                return redirect(url_for("student_home"))
            else:
                flash("Invalid student credentials", "error")

    return render_template("login.html")

# ---------------- ADMIN ----------------
@app.route("/admin/home")
def admin_home():
    if "admin" not in session:
        return redirect(url_for("login"))
    students = view_students()
    return render_template("admin_home.html", students=students)

@app.route("/admin/add", methods=["GET", "POST"])
def admin_add():
    if "admin" not in session:
        return redirect(url_for("login"))
    if request.method == "POST":
        roll_no = request.form["roll_no"]
        name = request.form["name"]
        email = request.form["email"]
        branch = request.form["branch"]
        password = request.form["password"]
        if add_student(roll_no, name, email, branch, password):
            flash("Student added successfully ✅", "success")
        else:
            flash("Failed to add student ❌", "error")
        return redirect(url_for("admin_home"))
    return render_template("add.html")

@app.route("/admin/edit/<roll_no>", methods=["GET", "POST"])
def admin_edit(roll_no):
    if "admin" not in session:
        return redirect(url_for("login"))

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT roll_no, name, email, branch FROM students WHERE roll_no=?", (roll_no,))
    student = cursor.fetchone()
    conn.close()
    if not student:
        flash("❌ Roll No not found!", "error")
        return redirect(url_for("admin_home"))

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        branch = request.form["branch"]
        password = request.form.get("password")
        if update_student(roll_no, name, email, branch, password):
            flash("Student updated successfully ✅", "success")
        else:
            flash("Failed to update student ❌", "error")
        return redirect(url_for("admin_home"))

    return render_template("edit.html", student=student)

@app.route("/admin/delete_confirm/<roll_no>")
def admin_delete_confirm(roll_no):
    if "admin" not in session:
        return redirect(url_for("login"))
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT roll_no, name FROM students WHERE roll_no=?", (roll_no,))
    student = cursor.fetchone()
    conn.close()
    if not student:
        flash("❌ Roll No not found!", "error")
        return redirect(url_for("admin_home"))
    return render_template("delete.html", student=student)

@app.route("/admin/confirm_delete/<roll_no>", methods=["POST"])
def admin_confirm_delete(roll_no):
    if "admin" not in session:
        return redirect(url_for("login"))
    delete_student(roll_no)
    flash("Student deleted successfully ✅", "success")
    return redirect(url_for("admin_home"))

# ---------------- STUDENT ----------------
@app.route("/student/home")
def student_home():
    if "student" not in session:
        return redirect(url_for("login"))
    roll_no = session["student"]
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT roll_no, name, email, branch FROM students WHERE roll_no=?", (roll_no,))
    student = cursor.fetchone()
    conn.close()
    return render_template("student_home.html", student=student)

# ---------------- LOGOUT ----------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
