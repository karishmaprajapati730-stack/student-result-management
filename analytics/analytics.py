import sqlite3 

def show_topper():
    conn = sqlite3.connect(path)

    topper = conn.connect("SELECT * ,(maths + science + english) AS total FROM student ORDER BY total DESC LIMIT 1;")

    conn.close()

    return topper

def class_avg():
    conn = sqlite3.connect(path)

    avg = conn.connect("SELECT AVG(maths) AS math_avg, AVG(science) AS science_avg, AVG(english) AS eng_avg FROM student")

    conn.close()

    return avg

def highest_marks():
    conn = sqlite3.connect(path)

    highest_marks = conn.connect("SELECT MAX(maths + science + english) FROM student")
    
    conn.close()

    return highest_marks
    