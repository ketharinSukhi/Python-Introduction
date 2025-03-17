num = int(input("Enter a number to see its times table: "))


print(f"Times Table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")