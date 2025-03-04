"""x=float(input("what's x "))
y=float(input("what's y "))
# print("sum",x+y)
z = round(x + y)
print(f"{z:,}")
#f=round(x/y)
f=(x/y)
print(f"{f:.2f}")

#print(int(input("what's x ")) + int(input("what's y ")))"""

def main():
    x=int(input("what's x "))
    print("x squared is",square(x))

def square(n):
    return n + n

if __name__ == "__main__":
   main()

