
"""with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
        #row = line.rstrip().split(",")
        #print(f"{row[0]} is in {row[1]}")"""

#phrases

import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for name, home in reader:
        students.append({"name": name, "home":home})
    """for line in file:
        name, home = line.rstrip().split(",")
        student = {"name":name, "home":home}
        student["name"]=name
        student["home"]=home
        students.append(student)"""

""""def get_name(student):
    return student["name"]
def get_home(student):
    return student["name"]"""

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
