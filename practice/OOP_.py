#create class
#class student:
   # name ="sukhi"

#creating object(instance)
#s1= student()
#print(s1.name)

class Car:
    
    def __init__(self, name):
        self.name = name
        print("creating car")
    
   
#the store name for variable called attributes
car = Car("BMW")
print(car.name)
car1 = Car("TOYOTA")
print(car1.name)