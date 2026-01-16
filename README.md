# 🎓 Student Database Management System

A simple **Python + SQLite** based CLI application to manage student records with full CRUD operations. This project is beginner-friendly and demonstrates real-world database handling with proper validations.

---

## 🚀 Features

* ➕ Add new students
* 👀 View all students
* ✏️ Update student details using Roll No
* ❌ Delete student records
* 🔐 Roll No as **PRIMARY KEY** (VARCHAR)
* ⚠️ Handles duplicate Roll No / Email errors
* 🧠 Validates existence before update/delete
* 🗃️ Data stored using SQLite

---

## 🛠️ Tech Stack

* **Language:** Python
* **Database:** SQLite3
* **Version Control:** Git & GitHub
* **Interface:** Command Line (CLI)

---

## 📂 Project Structure

```
student_db/
│
├── main.py         # Menu-driven CLI
├── database.py     # Database connection & table creation
├── operations.py   # CRUD operations
├── students.db     # SQLite database (auto-created)
├── LICENSE         # MIT License
└── README.md       # Project documentation
```

---

## ▶️ How to Run the Project

1. **Clone the repository**

```bash
git clone https://github.com/Charan-online/student_db.git
cd student_db
```

2. **Run the application**

```bash
python main.py
```

3. Use the menu options to manage student records 🎯

---

## 🧪 Sample Menu

```
--- Student Database Menu ---
1. Add Student
2. View Students
3. Update Student
4. Delete Student
5. Exit
```

---

## ❗ Validations Implemented

* Roll No must be unique
* Email must be unique
* Update only allowed if Roll No exists
* Clean error handling using try-except

---

## 📈 Future Enhancements

* 🔍 Search student by Roll No or Email
* 🌐 Convert to Flask Web App
* 🎨 Improve CLI UI with colors
* 🧪 Add unit tests
* 📦 Export data to CSV

---

## 💼 Resume Value

This project demonstrates:

* Database design concepts
* CRUD operations
* Error handling
* Git & GitHub workflow
* Clean and modular Python code

Perfect for **college placements & internships** 🚀

---

## 📄 License

This project is licensed under the **MIT License**.

---

👨‍💻 **Author:** Charan

⭐ If you like this project, give it a star on GitHub!
