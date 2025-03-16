"""x=int(input("what's x "))
y=int(input("what's y "))

score = int(input("score : "))
if 90 <= score <= 100:
    print("Grade:A")
elif 80 <= score < 90:
    print("Grade:B")
elif 70 <= score < 80:
    print("Grade:C")
elif 60 <= score < 70:
    print("Grade:D")
else:
    print("Grade:F")"""

#using boolean
def main():
    number =int(input("what's number?"))
    if is_even(number) is True:
        print("even")
    else:
        print("odd")
def is_even(number):
   #return True if number%2 ==0 else False
   return number%2 ==0 
main()

#match
name = input("what's your name: ")
match name:
    case "Harry" | "Hermione" | "Ron" | "Jenny":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("who?")