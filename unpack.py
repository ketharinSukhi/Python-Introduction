#Unpacking

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(**coins), "Knuts") #unpacking

#args and kwargs
"""def f(*args, **kwargs):
    print("Positional: ", kwargs)

f(galleons=100, sickles=50, knuts=25)"""

#map and list comprehensions
"""def main(): 
    yell("This","is","CS50")

def yell(*words):
    uppercased = [word.upper() for word in words]
    #uppercased = map(str.upper, words)
    print(*uppercased)


if __name__ == "__main__":
     main()"""