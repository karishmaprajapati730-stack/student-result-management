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
print(data)

topper=conn.execute("SELECT st_name FROM student ORDER BY (maths + science + english) DESC LIMIT 1").fetchone()
print("Topper:", topper[0]) 

class_average=conn.execute("SELECT AVG(maths) as maths_avg, AVG(science) as science_avg, AVG(english) as english_avg FROM student").fetchone() 
print("Class Average - Maths:", class_average[0], "Science:", class_average[1], "English:", class_average[2])

highest_maths=conn.execute("SELECT MAX(maths) FROM student").fetchone()[0]
print("Highest Maths Score:", highest_maths)

lowest_science=conn.execute("SELECT MIN(science) FROM student").fetchone()[0]
print("Lowest Science Score:", lowest_science)

conn.commit()
conn.close()

