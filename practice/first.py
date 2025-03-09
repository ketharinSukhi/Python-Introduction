"""name = str(input("What is your name? \n"))

if str.isalpha(name):
 print("my name is", name)
else:
 print("enter name")"""

def select(x, y):
    if x >y:
        print("x is greater than y")
    elif x<y:
        print("x is smaller than y")
    else:
        print("x is equal to y")
def main():
    x = input("what is x ?")
    y = input("what is y ?")
    select(x, y)
   

main()
 
  





