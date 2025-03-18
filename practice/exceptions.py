try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Result:", result)  
finally:
    print("Finally runs")

#raise 
age = int(input("Enter your age: "))

if age < 18:
    raise ValueError("Age must be 18 or above!") 
else:
    print("You are eligible!")


#custom exception

class TooYoungError(Exception):
    pass

age = int(input("Enter your age: "))

if age < 18:
    raise TooYoungError("You are too young to vote!")
else:
    print("You can vote.")