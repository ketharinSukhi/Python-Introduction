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
#bank account
"""class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account = acc
        print("my account is ", self.account)
        

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
acc1.credit(1000)"""
#private method and attribute
""""class Account:
    def __init__(self, acc_no, acc_pass):
        self.account = acc_no
        # to make it private use two under score before __
        self.__password = acc_pass

    #private method __
    def __hello(self):
        print("hello")

    def welcom(self):
        self.__hello()
   
    def reset_pass(self):
        print(self.__password)

acc1 = Account(12345,"abcd")

print(acc1.account)
print(acc1.reset_pass())"""

#single Inheritance
#multi-level Inheritance
class Car:

    def __init__(self, type):
        self.type =type
    @staticmethod
    def start():
        print("Car started")
    @staticmethod
    def stop():
        print("Car ped")

class ToyotaCar(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)

"""class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type"""

car1 = ToyotaCar("diesel", "manual")
print(car1.type)

#multiple Inheritance

"""class A:
    varA = "class A"
class B:
    varB = "class B"

class C(A, B):

    varC = "class C"

c1=C()

print(c1.varC)
print(c1.varB)
print(c1.varA)"""
    










