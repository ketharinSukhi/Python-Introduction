"""name = str(input("What is your name? \n"))

if str.isalpha(name):
 print("my name is", name)
else:
 print("enter name")"""

name = input("what is your name? ").strip().title()
first, last = name.split(" ")
print("my name is",end=" ")
print(f"{first}")

