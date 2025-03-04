"""names = []

for  _ in range(3): 
    names.append(input("what's your name? "))

for name in sorted(names):
    print(f"hello,{name}")"""

name = input("what's your name? ")

file = open("names.txt","a")
file.write(f"{name}\n")
file.close()