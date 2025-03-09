"""name = str(input("What is your name? \n"))

if str.isalpha(name):
 print("my name is", name)
else:
 print("enter name")"""

"""def select(b):
    print(f"my name is {b}")
    
def main():
    x = str(input("what is your name ? "))
    select(x)
   
main()"""


students = [
            {"name":"Hermione","house":"Gryffindor","patronus":"Otter"},
            {"name":"Harry","house":"Gryffindor","patronus":"Stag"},
            {"name":"Ron","house":"Gryffindor","patronus":"Jack Russel Terrier"},
            {"name":"Draco","house":"Slytherin","patronus":None }
             ]
for student in students:
  print(student["name"], student["house"], student["patronus"], sep=" --> ")
  
 