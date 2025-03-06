#Unpacking

"""def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(**coins), "Knuts") #unpacking"""

#args and kwargs
"""def f(*args, **kwargs):
    print("Positional: ", kwargs)

f(galleons=100, sickles=50, knuts=25)"""

#map
def main():
    yell("This","is","CS50")

def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)


if __name__ == "__main__":
     main()