
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

#filter() iterates over students and selects only those whose "house" is "Gryffindor"
gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)

for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
   print(gryffindor["name"])"""

#Enumerate : used to count 
"""students = ["Hermione","Harry","Ron"]

for i, student in enumerate(students):
    print(i+1, student)"""

#flock yield
def main():
  n = int(input("what's n? "))
  for s in sheep(n):
     print(s)

def sheep(n):
   #flock = []
   for i in range(n):
      yield "🍔" * i
      #flock.append("🍔" * i)
   #return flock

if __name__ == "__main__":
    main()
