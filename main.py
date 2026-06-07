from database.db_operations import *
from analytics.analytics import *

create_table()

add_student()

data = view_student()

print(data)

info = search_student(4)
print(info)

topper = show_topper()
print(topper)

class_avg = class_avg()
print(class_avg)

highest = highest_marks()
print(highest)

lowest = lowest_marks()
print(lowest)

generate_csv_report()
