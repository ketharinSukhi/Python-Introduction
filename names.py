"""names = []

for  _ in range(3): 
    names.append(input("what's your name? "))

for name in sorted(names):
    print(f"hello,{name}")"""



#OpenWith
name = input("what's your name? ")

"""with open("names.txt","a") as file:
 file.write(f"{name}\n")
file.close()"""

with open("names.txt","r") as file:
     #lines = file.readlines()
    for line in file:
      print("hello, " ,line.rstrip())

#sorted name
names = []

"""with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
#for name in sorted(names, reverse=True):
    print(f"hello, {name}")"""


#only print house name
"""students = [
            {"name":"Hermione","house":"Gryffindor"},
            {"name":"Harry","house":"Gryffindor"},
            {"name":"Ron","house":"Gryffindor"},
            {"name":"Draco","house":"Slytherin"}
             ]
houses = set()
for student in students:
    if student in students:
        houses.add(student["house"])

for house in sorted(houses):
    print(house)"""



