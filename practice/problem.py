
number = int(input("Enter the number : "))

#pyramid 1
"""for i in range (1, number+1):
    for j in range(i):
        print("*", end="")
    print(" ")"""

#pyramid 2

for i in range (1, number+1):
    for j in range(number):
        print("*", end="")
    number = number-j
    print("")
    





    