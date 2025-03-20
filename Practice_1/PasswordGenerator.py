import random

def generate_password(length):

def main():

    try:
        passwords_num = input("How many password you want to generate : ")
        length = int(input("Enter the password length : "))

        if length < 4:
            print("Password length should be at least 4 characters")
            return
        
        for _ in range(passwords_num):
            print(generate_password(length))
    except ValueError:
        print("enter valid number")

if __name__=="__main__":
    main()
