import sqlite3

# from concurrent.interpreters import create

conn=sqlite3.connect("student.db")

try:
    conn.execute('''create table student(st_id INT AUTO_INCREMENT,
                 st_name VARCHAR(50),
                 st_class VARCHAR(10),
                 st_email VARCHAR(30))
                 ''')
    
except:
    print("Error...")

