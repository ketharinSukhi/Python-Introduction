
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

#OOP Class Method Property
class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        """if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw","Slytherin"]:
            raise ValueError("Invalid house")"""

        self.name = name 
        self.house = house
        self.patronus = patronus

    def __str__(self):
        return f"{self.name} from {self.house}"


#Getter
    @property
    def house(self):
        return self._house
#Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw","Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house

    def charm(self):
        match self.patronus:
            case "Stag":
                return "😊"
            case "Otter":
                return "🦄"
            case "Jack Rusell Terrier":
               return "🐴"
            case _:
                return "/"


def main():
    student= get_student()
    print(student)
    print(student.charm())


def get_student():
    
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    
    return Student(name, house, patronus)

if __name__ =="__main__":
    main()
