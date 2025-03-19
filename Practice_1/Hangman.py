import random

word_list = ["dog", "carrot","banana","apple"]

def choose_word():
    return random.choice(word_list)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word_to_guess = choose_word()
    guessed_letters = set()
    attempts =10

    print("WELCOME TO HANGMAN GAME !!")

    while attempts >0:
        print("\n", display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word_to_guess:
            print("Good job! That letter is in the word.")
            if set(word_to_guess) <= guessed_letters:
                print(f"Congratulations! You guessed the word: {word_to_guess}")
                break
        else:
            attempts -= 1
            print(f"Incorrect! You have {attempts} attempts left.")
    else:
        print(f"Game over! The word was: {word_to_guess}")

def main():
    
    hangman()

if __name__=="__main__":
    main()