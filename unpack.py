#Unpacking

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(**coins), "Knuts") #unpacking

#arguments and keywords unpacking
def f(*args, **kwargs):
    print("Positional: ", kwargs)

f(galleons=100, sickles=50, knuts=25)

#map and list comprehensions
def main(): 
    call("This","is","CS50")

def call(*words):
    uppercased = [word.upper() for word in words]
    #uppercased = map(str.upper, words)
    print(*uppercased)


if __name__ == "__main__":
     main()