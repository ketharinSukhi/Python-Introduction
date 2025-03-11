#create class
#class student:
   # name ="sukhi"

#creating object(instance)
#s1= student()
#print(s1.name)

class Car:
    
    def __init__(self, name, color):
        self.name = name
        self.color = color
        print("creating car")
    
   
#the store name for variable called attributes
car = Car("BMW","red")
print(car.name, car.color)
car1 = Car("TOYOTA","Green")
print(car1.name, car1.color)