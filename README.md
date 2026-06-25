# Library-Management_Mini-Project

A **console-based Library Management System** for managing library book stocks, student book transactions, and book demand records using a MySQL database backend.

---

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Database Setup](#database-setup)
- [Configuration](#configuration)
- [Usage](#usage)
- [Example Menu](#example-menu)
- [Notes](#notes)
- [License](#license)

---

## Features

- **Manage Book Stock**
  - Import new books, add existing books to shelves
  - View and update available stock

- **Student Transactions**
  - Record when students take or return books
  - View student transaction history
  
- **Demand Tracking**
  - Log requests for new books
  - Display all demanded books

- **Comprehensive Reports**
  - List all imports, demands, stocks, and student activities

---

## Prerequisites

- Python 3.12
- MySQL Server (running and accessible)
- MySQL Connector for Python: pip install mysql-connector-python

## Database Setup

Make sure your MySQL server has a database and tables as follows:

- **Database:** `jaykamavisdar`
- **Tables:**
- `libimport` (`book_name`, `author`, `quantity`, `date_of_arrival`)
- `libstocks` (`book_id`, `book_name`, `author`, `shelf_no`)
- `libdemands` (`book_name`, `author`, `quantity`)
- `taken_by_student` (`reg_no`, `student_name`, `date_of_taking`, `book_id`)
- `return_by_student` (`reg_no`, `student_name`, `date_of_return`, `book_id`)

*Field types and constraints should match your application logic.*

---

## Configuration

Edit MySQL credentials in your Python script as needed:
mdb = mc.connect(
host='localhost',
user='root',
passwd='jayk',
database='jaykamavisdar'
)

Set the `user`, `passwd`, and `database` fields to your own MySQL settings.

---

## Usage

1. **Install dependencies** as in [Prerequisites](#prerequisites).
2. **Ensure your MySQL server is running** with the required tables populated.
3. **Run the script:**
    ```
    python Mini-Project.py
    ```
4. **Follow on-screen menu prompts** to perform various operations.

---

## Example Menu

Edit Stock Records

Edit Student Records

Add/View Book Demands

View Reports

Exit


---

## Notes

- Minimal input validation: please enter valid input.
- All actions directly alter the database.
- This system is for educational/demo use and is not intended for production.

---

## License

For educational use only. No specific license.
