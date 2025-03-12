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

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    
    def start(self):
        self.clutch = True
        self.acc =True
        print("start the car")

car1 = Car()
car1.start()