from flask import Flask, render_template, request, redirect, url_for, flash
from operations import add_student, view_students, update_student, delete_student
from database import create_table

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Required for flash messages
create_table()

# ------------------- Routes -------------------

# Home / welcome page
@app.route("/")
def home():
    return render_template("home.html")

# Add student page
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        roll_no = request.form["roll_no"]
        name = request.form["name"]
        email = request.form["email"]
        branch = request.form["branch"]
        success = add_student(roll_no, name, email, branch)
        if success:
            flash("✅ Student added successfully!", "success")
        else:
            flash("❌ Failed to add student! Roll No or Email may already exist.", "error")
        return redirect(url_for("home"))
    return render_template("add.html")

# View students page
@app.route("/view")
def view():
    students = view_students()
    return render_template("view.html", students=students)

# Edit / update student page
@app.route("/edit/<roll_no>", methods=["GET", "POST"])
def edit(roll_no):
    students = view_students()
    student = next((s for s in students if s[0] == roll_no), None)
    if not student:
        flash("❌ Roll No not found!", "error")
        return redirect(url_for("home"))

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        branch = request.form["branch"]
        success = update_student(roll_no, name, email, branch)
        if success:
            flash("✅ Student updated successfully!", "success")
        else:
            flash("❌ Failed to update student! Email may already exist.", "error")
        return redirect(url_for("home"))
    return render_template("edit.html", student=student)

# Delete confirmation page
@app.route("/delete_confirm/<roll_no>")
def delete_confirm(roll_no):
    students = view_students()
    student = next((s for s in students if s[0] == roll_no), None)
    if not student:
        flash("❌ Roll No not found!", "error")
        return redirect(url_for("home"))
    return render_template("delete.html", student=student)

# Confirm delete action (POST)
@app.route("/confirm_delete/<roll_no>", methods=["POST"])
def confirm_delete(roll_no):
    delete_student(roll_no)
    flash("✅ Student deleted successfully!", "success")
    return redirect(url_for("home"))

# ------------------- Run server -------------------
if __name__ == "__main__":
    app.run(debug=True)

