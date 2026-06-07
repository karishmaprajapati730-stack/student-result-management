import pandas as pd
import sqlite3 

# data = sqlite3.connect("student.db")

path = "database/student.db"

def show_topper():
    conn = sqlite3.connect(path)

    topper = conn.execute("SELECT * ,(maths + science + english) AS total FROM student ORDER BY total DESC LIMIT 1").fetchone()

    conn.close()

    return topper

def class_avg():
    conn = sqlite3.connect(path)

    avg = conn.execute("SELECT AVG(maths) AS math_avg, AVG(science) AS science_avg, AVG(english) AS eng_avg FROM student").fetchone()

    conn.close()

    return avg

def highest_marks():
    conn = sqlite3.connect(path)

    highest_marks = conn.execute("SELECT MAX(maths + science + english) FROM student").fetchone()
    
    conn.close()

    return highest_marks

def lowest_marks():
    conn = sqlite3.connect(path)
    
    lowest_marks = conn.execute("SELECT MIN(maths + science + english) FROM student").fetchone()
    
    conn.close()

    return lowest_marks

def generate_csv_report():

    conn = sqlite3.connect("database/student.db")
    
    df = pd.read_sql_query("SELECT * FROM student", conn)
    
    df.to_csv("reports/result_report.csv")

    conn.close()

    print("CSV report generated successfully")

