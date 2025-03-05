
"""with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
        #row = line.rstrip().split(",")
        #print(f"{row[0]} is in {row[1]}")"""

#CsvReader

"""import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home":row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")"""

#CsvWriter
"""import csv

name = input("what your name? ")
home = input("where's your home? ")

with open("students.csv","a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home":home})"""

#OOP

def main():
    name, house= get_student()
    print(f"{name} from {house}")


def get_student():
    name = input("name: ")
    house = input("house: ")
    return name, house

if __name__ =="__main__":
    main()
