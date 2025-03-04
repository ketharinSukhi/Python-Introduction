
"""with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
        #row = line.rstrip().split(",")
        #print(f"{row[0]} is in {row[1]}")"""

#phrases
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name":name, "house":house}
        student["name"]=name
        student["house"]=house
        students.append(student)

def get_name(student):
    return student["name"]
def get_house(student):
    return student["name"]
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
