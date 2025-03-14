import random

def generate_random_number(start, end):

    return random.randint(start, end)

def play_game():
    print("welcome to the game")
    #number range
    start, end = 1, 100
    random_number = generate_random_number(start, end)
    attempts = 0

    