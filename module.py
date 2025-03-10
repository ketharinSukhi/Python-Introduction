"""def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"hello {name}")

def goodbye(name):
    print(f"goodbye {name}")
    
if __name__ == "__main__":
   main()"""

import sys

def main():
  ok=sys()
  print("Hello", ok)

def sys(): 
 for i in range(2):
   print(sys.argv[i+1])
