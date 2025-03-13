"""class Account:
    def __init__(self):
        self._balance = 100


    
    def balance(self):
        return self._balance
    
    def deposit(self,n):
        self._balance +=n
        print("Total Balance: ", self.balance)
        
    def withdraw(self, n):
        self._balance -=n

def main():
    account = Account()
    print("Balance :", account.balance)
    account.deposit(1000)
    account.withdraw(700)
    print("Balance:", account.balance)

if __name__ =="__main__":
    main()"""

#docstring
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

print(add.__doc__) 

#argparse
"""import argparse

parser = argparse.ArgumentParser(description="numbers of time to say hello")
parser.add_argument("-n", default=3,type=int)
args = parser.parse_args()

for _ in range(int(args.n)):
    print("hello")"""

#unpacking

data = (2,3,4,5)
