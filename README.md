# 📚 Library Management System (Python)

## 🚀 Overview

This project is a **menu-driven Library Management System** built using Python. It follows a modular structure and separates logic across multiple files, ensuring clean and maintainable code.

The system allows users to manage books, issue and return them, and interact through a simple command-line interface.

---

## ⚙️ Features

* Add new books to the library
* Display all available books
* Borrow (issue) books
* Return books
* Menu-driven system using an infinite loop (`while True`)

---

## 🏗️ Project Structure

```
Library-Management-System/
│
├── Main.py          # Entry point (menu-driven system)
├── add.py           # Add book functionality
├── show.py          # Display books
├── issue.py         # Borrow/issue book logic
├── returnbk.py      # Return book logic
├── lis.py           # Data storage (books list/dictionary)
```

---

## 🧠 Concepts Used

* Functions and modular programming
* Lists / Dictionaries for data storage
* Conditional statements
* Loops (`while`, `for`)
* Basic input/output handling

---

## ▶️ How to Run

1. Clone the repository:

   ```
   git clone https://github.com/sagar-dev777/Library_managment_system.git
   ```

2. Navigate to the project folder:

   ```
   cd Library-Management-System
   ```

3. Run the main file:

   ```
   python Main.py
   ```

---

## 🖥️ Menu Interface

```
--------------------------
|--WELCOME TO CGC LIBRARY--|
--------------------------
1. Add book
2. Show books
3. Borrow book
4. Return books
5. Exit
```

---

## ⚠️ Limitations

* No persistent storage (data resets after program ends)
* Basic input validation
* No user authentication

---

## 🔧 Future Improvements

* Add file/database storage (JSON / SQLite)
* Implement fine calculation for late returns
* Add date tracking for issued books
* Improve user interface and validation
* Convert into a GUI or web-based system

---

## 📌 Author

Sagar
B.Tech CSE (AI & ML)

---

## 📄 License

This project is for educational purposes.
