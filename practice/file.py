"""name = input("Enter name: ")

# Writing to the file (Overwrites existing content)**
with open("file.txt","a") as file:
 file.write(f"{name}\n")
with open("file.txt","r") as file: 
    for line in file:
      print("hello, " ,line.rstrip())"""

#csv write
import csv

name = input("what your name? ")
home = input("where's your home? ")

with open("students.csv","a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home":home})

#csv reader

import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home":row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")