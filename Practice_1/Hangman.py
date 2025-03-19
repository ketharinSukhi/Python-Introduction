import random

word_list = ["dog", "carrot","banana","apple"]

def choose_word():
    return random.choice(word_list)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word_to_guess = choose_word()
    guessed_letters = set()
    attempts =6

    print("WELCOME TO HANGMAN GAME !!")

    while attempts >0:
        print("\n" + display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()

    

def main():
    
    hangman()

if __name__=="__main__":
    main()