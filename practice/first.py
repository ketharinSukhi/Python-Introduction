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


def main():
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
main()