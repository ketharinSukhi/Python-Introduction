import random

word_list = ["dog", "carrot","banana","apple"]

def choose_word():
    return random.choice(word_list)

def display_word():

def hangman():
    word_to_guess = choose_word()
    guessed_letter = set()
    attempts =6

    print("WELCOME TO HANGMAN GAME !!")
    

def main():
    
    hangman()

if __name__=="__main__":
    main()