#pyramid 1
number = int(input("Enter the number : "))

for i in range (1, number+1):
    for j in range(i):
        print("*", end="")
    print(" ")

#pyramid 2

for i in range (1, number+1):
    for j in range(i):
        print(" o", end="")
    print("*")

print("\n\n")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i}, {j})", end=" ")

    print(" ")



    