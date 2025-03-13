class Account:
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
    main()