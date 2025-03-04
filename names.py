"""names = []

for  _ in range(3): 
    names.append(input("what's your name? "))

for name in sorted(names):
    print(f"hello,{name}")"""



#OpenWith
"""name = input("what's your name? ")

with open("names.txt","a") as file:
 file.write(f"{name}\n")
file.close()"""

with open("names.txt","r") as file:
    lines = file.readlines()

for line in lines:
    print("hello, " ,line)
