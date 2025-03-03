"""def main():
   x=get_int("what's x? ")
   print(f"x is {x}")


def get_int(prompt):
  while True:
    try :
     return int(input(prompt))
   
    except ValueError:
      pass
main()"""
#random
"""import random

coin = random.choice(["heads", "tails"])
number = random.randint(1, 10)
cards = ["jack","king","queen"]
random.shuffle(cards)
for card in cards:
   print(card)
print(coin, number)"""

#average
import sys

if len(sys.argv)<2 :
  print("too few arguments")
elif len(sys.argv)>2 :
  print("too many arguments")
else:
  print("hello, my name is", sys.argv[1])

  


