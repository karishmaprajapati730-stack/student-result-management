# student-result-management

Student Result Management System

Overview

Student Result Management System is a Python-based project developed to manage student academic records efficiently. The project uses SQLite as the database and Pandas for report generation and data handling. It provides a simple menu-driven interface for performing student record operations and analyzing academic performance.

Features

- Add new student records
- View all student records
- Search student by ID
- Update student marks
- Delete student records
- Find class topper
- Calculate class average
- Find highest marks
- Find lowest marks
- Generate CSV reports using Pandas

Technologies Used

- Python
- SQLite3
- SQL
- Pandas
- Git & GitHub

Project Structure

student-result-management/

├── analytics/

│ └── analytics.py

├── database/

│ ├── db_operations.py

│ └── student.db

├── reports/

│ └── result_report.csv

├── main.py

└── README.md

Database Schema

student(
st_id INTEGER PRIMARY KEY AUTOINCREMENT,
st_name TEXT,
st_class TEXT,
maths INTEGER,
science INTEGER,
english INTEGER
)

Analytics Implemented

- Topper Identification
- Class Average Calculation
- Highest Marks Analysis
- Lowest Marks Analysis

CSV Report Generation

The project generates a CSV report containing all student records and their academic details using the Pandas library.

Learning Outcomes

This project helped in understanding:

- SQLite database operations
- SQL queries (CRUD operations)
- Python modules and functions
- Project structure and organization
- Data analysis using Pandas
- Report generation
- Version control using Git and GitHub

Future Enhancements

- Graphical User Interface (GUI)
- Excel report generation
- REST API integration
- Power BI dashboard integration

Author

Karishma Prajapati

