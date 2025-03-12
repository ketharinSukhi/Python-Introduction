class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks =marks
    
    def get_average(self):
        sum=0
        for i in self.marks:
            sum +=i
        avge = sum/3
        print(f"{self.name}, {avge:.2f}")


s1 = Student("Tina",[67, 80, 95])
s1.get_average()