
"""
i=0
while i<4:
 print("hello")
 i+=1"""

"""while True:
  n = int(input("what's n? "))
  if n>0:
    break
for _ in range(n):
  print("hello")"""
#function and loops
"""def main():
    number = get_number()
    hello(number)

def get_number():
    while True:
        n = int(input("what's n?"))
        if n > 0:
            break
    return n
def hello(n):
    for _ in range(n):
        print("hello")
main()"""

#list

""""students = ["Hermione","Harry","Ron"]


for i in range(len(students)):
    print(i+1, students[i])"""

#dict
students = {"Hermione":"Gryffindor",
            "Harry":"Gryffindor",
            "Ron":"Gryffindor",
             "Draco":"Slytherin" 
             }

s=str(input("enter s: "))
print(students[s])




