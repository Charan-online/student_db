from database import create_table
from operations import (
    add_student,
    view_students,
    update_student,
    delete_student,
    student_exists
)

create_table()

while True:
    print("\n--- Student Database Menu ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        roll_no = input("Roll No: ")
        name = input("Name: ")
        email = input("Email: ")
        branch = input("Branch: ")
        add_student(roll_no, name, email, branch)

    elif choice == "2":
        students = view_students()
        if students:
            for s in students:
                print(s)
        else:
            print("No students found 😅")

    elif choice == "3":  # ✅ FIXED UPDATE FLOW
        roll_no = input("Enter student Roll No to update: ")

        if not student_exists(roll_no):
            print("❌ Roll No not found in database!")
            continue  # go back to menu

        print("Leave blank if you don't want to change a field")
        name = input("New Name: ")
        email = input("New Email: ")
        branch = input("New Branch: ")

        name = name if name else None
        email = email if email else None
        branch = branch if branch else None

        update_student(roll_no, name, email, branch)

    elif choice == "4":
        roll_no = input("Enter student Roll No to delete: ")
        delete_student(roll_no)

    elif choice == "5":
        print("Bye! 👋")
        break

    else:
        print("Invalid option ❌")
