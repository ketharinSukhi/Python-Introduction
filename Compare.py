"""x=int(input("what's x "))
y=int(input("what's y "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y") """

score = int(input("score : "))
if score >= 90 and score <= 100:
    print("Grade:A")
elif score >= 80 and score < 90:
    print("Grade:B")
elif score >= 70 and score < 80:
    print("Grade:C")
elif score >= 60 and score < 70:
    print("Grade:D")
else:
    print("Grade:F")