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

def multiply(*numbers):
    sum=0
    for i in numbers:
        sum += i
    return sum

print(multiply(2,3,4,5))



 
  





