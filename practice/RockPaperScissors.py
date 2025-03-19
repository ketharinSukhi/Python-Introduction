import random
print ("WELCOME TO ROCK PAPER SCISSOR GAME !!!")

def computer_choice():
    return random.choice(["rock","paper","scissor"])

def user_choice():
   choice = input("Enter rock, paper or scissors: ")
   while choice not in ["rock","paper","scissor"]:
        print("Invalid choice :(")
        choice = input("Enter rock, paper or scissors: ")
   return choice

def winner(user, computer):


def play_game():
   user_choice = user_choice()
   computer_choice = computer_choice()
   print(f"Computer Chose : {computer_choice}")
   print(winner(user_choice, computer_choice))

def main():
    play_game()
if __name__ =="__main__":

 main()











