
#filter
"""students = [
            {"name":"Hermione","house":"Gryffindor","patronus":"Otter"},
            {"name":"Harry","house":"Gryffindor","patronus":"Stag"},
            {"name":"Ron","house":"Gryffindor","patronus":"Jack Russel Terrier"},
            {"name":"Draco","house":"Slytherin","patronus":None }
             ]

gryffindors =[
    student["name"] for student in students if student["house"] == "Gryffindor" 
]


gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
   print(gryffindor["name"])"""

#Enumerate
"""students = ["Hermione","Harry","Ron"]

for i, student in enumerate(students):
    print(i+1, student)"""

n = int(input("what's n? "))
for i in range(n):
    print("🍔" * i)
