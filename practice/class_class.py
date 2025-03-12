#class method

"""class Person:
    name = "anonymous"

       #def changeName(self, name):
        #to change attribute in method
        #self.__class__.name = name
        #Person.name = name

    @classmethod
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("Liza Rain")
print(p1.name)
print(Person.name)"""

#property
"""class Student:
    def __init__(self, phy, chem, math):
       self.phy = phy
       self.chem = chem
       self.math = math
    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3) + "%"

stu1 = Student(76, 54, 70)
print(stu1.percentage)
stu1.chem = 75
print(stu1.percentage)"""
#polymorphism
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img =img

    def showNumber(self):
        print(self.real,"i+", self.img,"j")
    #dunder function
    def __add__(self, num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)


num1 = Complex(1, 3)
num1.showNumber()
num2 = Complex(4, 5)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()