import random
print ("WELCOME TO ROCK PAPER SCISSOR GAME !!!")

def get_computer_choice():
    return random.choice(["rock","paper","scissor"])

def get_user_choice():
   choice = input("Enter rock, paper or scissors: ")
   while choice not in ["rock","paper","scissors"]:
        print("Invalid choice :(")
        choice = input("Enter rock, paper or scissors: ")
   return choice

def winner(user, computer):
    if user == computer:
       return "It is a tie"
    elif(user == "rock" and computer =="scissors") or \
        (user == "paper" and computer == "rock") or \
        (user == "scissors" and computer == "rock"):
       return "YOU WIN !!"

    else:
       return "YOU LOST !!"

def play_game():
   user_choice = get_user_choice()
   computer_choice = get_computer_choice()
   print(f"Computer Chose : {computer_choice}")
   print(winner(user_choice, computer_choice))

def main():
    play_game()
if __name__ =="__main__":

 main()











