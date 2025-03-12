"""class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks =marks

    @staticmethod #decorator convert
    def hello():
        print("hello")

    def get_average(self):
        sum=0
        for i in self.marks:
            sum +=i
        avge = sum/3
        print(f"{self.name}, {avge:.2f}")


s1 = Student("Tina",[67, 80, 95])
s1.get_average()"""

#abstraction
#encapsulation

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account = acc
        print("my account number",self.acc)

    def debit(self, amount):
        self.balance -=amount
        print("debited amount",amount)
        print("total balance",self.balance)

    def credit(self, amount):
        self.balance +=amount
        print("credit amount",amount)
        print("total balance",self.balance)

    def get_balace(self):
        return self.balance

acc1 = Account(10000, 1234)

acc1.debit(500)
acc1.credit(1000)