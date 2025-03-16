#print(type({}))
"""import random
class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw","Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))
Hat.sort("Harry")"""

#class method
class Wizard:
    def __init__(self, name):
         if not name:
            raise ValueError("Missing name")
         self.name = name
    
    ...

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

    ...

class Professor(Wizard):
    def __int__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    ...
wizard = Wizard("Albus")        
student = Student("Harry", "Gryffindor")
professor = Professor("Severus","Defense Against the Dark Arts")