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


try:
    n = int(input("enter n: "))
    
    total = 10/n
except ValueError:
   print("Invalid")
except ZeroDivisionError:
    print("Invalid")
else:
    print(f"total is {total}")

 