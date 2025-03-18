
number = int(input("Enter the number : "))
#pyramid 1
print("pyramid 1\n")
for i in range (1, number+1):
    for j in range(i):
        print("*", end="")
    print(" ")

#pyramid 2
print("pyramid 2\n")
num = number+1
for i in range (1, num):
    for j in range(num-i):
        print("*", end="")
    
    print(" ")

#pyramid 3
print("pyramid 3\n")
num = number+1
for i in range (1, num):
    for j in range(num-i):
        print(" ", end="")
    for m in range(i):

        print("*", end="")   
    print(" ")


#pyramid 4
"""print("pyramid 4\n")

for i in range (1, num):
    for j in range(i):
        print(" ", end="")
    for m in range(num-1):
        print("*", end="")
    num = num-1   
    print(" ")


#pyramid 5

print("pyramid 5\n")
for i in range (1, number+1):
    for j in range(number-i):
        print(" ", end="")
    for m in range(i):
        print("*", end=" ")
    print(" ")

#square

print("Square :\n")

for i in range(number):
    for j in range(number):
        print("*", end=" ")

    print("")"""


#diamond

print("diamond\n")
for i in range (1, number+1):
    for j in range(number-i):
        print(" ", end="")
    for m in range(i):
        print("*", end=" ")
    print(" ")

for i in range (1, num):
    for j in range(i):
        print(" ", end="")
    for m in range(num-1):
        print("*", end=" ")
    num = num-1   
    print(" ")
    

    





    