import sqlite3

data = sqlite3.connect("student.db")

path = "database/student.db"

def create_table():
    conn = sqlite3.connect(path)
    
    conn.execute('''
    CREATE TABLE IF NOT EXISTS student(
    st_id INTEGER PRIMARY KEY AUTOINCREMENT,
    st_name TEXT,
    st_class TEXT,
    maths INTEGER,
    science INTEGER,
    english INTEGER
    )
    ''')

    conn.commit()
    conn.close()

    print("Table is created successfully")

def add_student():
    conn = sqlite3.connect(path)
    
    conn.execute('''
    INSERT INTO student(st_name,st_class,maths,science,english)
    VALUES(('Aarav Sharma', 'BTech-CSE', 85, 78, 92),

    ('Priya Singh', 'BTech-CSE', 91, 88, 84),

    ('Rahul Verma', 'BTech-CSE', 76, 82, 79),

    ('Sneha Gupta', 'BTech-CSE', 95, 93, 97),

    ('Vikram Patel', 'BTech-CSE', 68, 74, 70),

    ('Ananya Mishra', 'BTech-CSE', 89, 90, 86),

    ('Rohan Kumar', 'BTech-CSE', 81, 77, 83))

    ''')

    conn.commit()
    conn.close()

    print("Student data added successfully")

