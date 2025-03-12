#create class
#class student:
   # name ="sukhi"

#creating object(instance)
#s1= student()
#print(s1.name)

class Student:
    #class Attribute
    college_name = "MBSTU"
 
    #default constructor only self parameter
    """def __init__(self):
       
        print("adding new student")"""

    #parameterized constructors
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    #method function
    def welcome(self):
        print("welcom students", self.name)

    def get_marks(self):
        return self.marks
    
   
#the store name for variable called attributes
s1 = Student("Edward",75)

s1.welcome()
print(s1.get_marks()) 


