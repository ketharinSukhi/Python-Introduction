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

def hello(n: int)-> str: #what the return value function is 
    return "hello\n" * n

number: int = int(input("Number: "))
hellos: str = hello(number)

print(hellos)


