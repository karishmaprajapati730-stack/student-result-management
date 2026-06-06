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


