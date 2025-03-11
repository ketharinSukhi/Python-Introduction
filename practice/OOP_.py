#create class
#class student:
   # name ="sukhi"

#creating object(instance)
#s1= student()
#print(s1.name)

class Car:
    
    def __init__(self, fullname):
        self.name = fullname
        print("creating car")
    
   

car = Car("BMW")
print(car.name)