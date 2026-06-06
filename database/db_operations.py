import sqlite3

# from concurrent.interpreters import create

conn=sqlite3.connect("student.db")

# try:
#     conn.execute('''create table student(st_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                  st_name TEXT,
#                  st_class TEXT,
#                  maths INTEGER,
#                  science INTEGER,
#                  english INTEGER)
#                  ''')
    
# except:
#     print("Error...")

# conn.execute('''INSERT INTO student (st_name, st_class, maths, science, english) VALUES
#     ('Aarav Sharma', 'BTech-CSE', 85, 78, 92),
#     ('Priya Singh', 'BTech-CSE', 91, 88, 84),
#     ('Rahul Verma', 'BTech-CSE', 76, 82, 79),
#     ('Sneha Gupta', 'BTech-CSE', 95, 93, 97),
#     ('Vikram Patel', 'BTech-CSE', 68, 74, 70),
#     ('Ananya Mishra', 'BTech-CSE', 89, 90, 86),
#     ('Rohan Kumar', 'BTech-CSE', 81, 77, 83)
# ''')


data = conn.execute("SELECT * FROM student").fetchall()

conn.commit()
conn.close()

