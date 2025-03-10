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

if len(sys.argv)<2:
    print("Too few arguments")
elif len(sys.argv)>2:
    print("Too many arguments")

print("hello", sys.argv[1])

