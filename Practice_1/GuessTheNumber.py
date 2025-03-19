import random

def get_random_number(start, end):

    return random.randint(start, end)

def play_game():
    print("WELCOME TO NUMBER GUESSING GAME")
    #number range
    start, end = 1, 10
    random_number = get_random_number(start, end)
    attempts = 0

    while True:
        try:
            guess = int(input(f"Guess a number between {start} and {end}: "))
            attempts += 1
            if guess <start or guess>end :
                print(f"Guess a number between {start} and {end}:")
            elif guess < random_number:
                print("try again!!")
            elif guess > random_number:
                print("try again!!")
            else:
                print(f"Congratulations! You guessed the number {random_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def main():
    play_game()
if __name__ == "__main__":
    main()


        

