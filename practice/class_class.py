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
class Student:
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
print(stu1.percentage)


