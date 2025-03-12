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
        print("adding new student")
    
   
#the store name for variable called attributes
s1 = Student("Edward",75)
print(s1.name, s1.marks)
s2 = Student("Toya",80)
print(s2.name, s2.marks)
print()