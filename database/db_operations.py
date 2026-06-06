import sqlite3

# from concurrent.interpreters import create

conn=sqlite3.connect("student.db")

try:
    conn.execute('''create table student(st_id INTEGER PRIMARY KEY AUTOINCREMENT,
                 st_name TEXT,
                 st_class TEXT,
                 maths INTEGER,
                 science INTEGER,
                 english INTEGER)
                 ''')
    
except:
    print("Error...")

    