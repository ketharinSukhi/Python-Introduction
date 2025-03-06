# x=int(input())
# y=int(input())
# print("hello, world",x+y)

# remove whitespace from str
#name= name.strip().title()
#Capitalize user's name and capitalization
# name=name.title()

"""name=input("what's your name?",).strip().title()
print(f"hello, world, {name}")

#print(name)
#print(*objects, sep='', end='\n')

#function create
def hello(to="world"):
    print("hello,", to)
hello()
name = input("what's your name? ")
#hello(name)
hello(name)"""

"""def main():
    name = input("what's your name? ")
    print(hello(name))
def hello(to="world"):
    return f"hello, {to}"

if __name__ == "__main__":
   main()"""

"""def hello(n: int)-> str: #-> what the return value function is 
    #hello n times
    return "hello\n" * n

number: int = int(input("Number: "))
hellos: str = hello(number)

print(hellos, end="")"""


#sys
"""import sys


if len(sys.argv) == 1:
    print("hello")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("hello")
else :
    print("usage:hello.py")"""

import argparse

parser = argparse.ArgumentParser(description="hello to the world")
parser.add_argument("-n", default=1, help="number of times to  hello")
args = parser.parse_args()

for _ in range(args.n):
    print("hello")



