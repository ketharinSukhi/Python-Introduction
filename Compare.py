"""x=int(input("what's x "))
y=int(input("what's y "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y") 

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

def main():
    number =int(input("what's number?"))
    if is_even(number):
        print("even")
    else:
        print("odd")
def is_even(number):
    return number%2 ==0 
main()

#match
name = input("what's your name: ")
match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("who?")