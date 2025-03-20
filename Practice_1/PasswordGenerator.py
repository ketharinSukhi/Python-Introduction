import random
import string

def generate_password(length):

    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


def main():

    try:
        passwords_num = int(input("How many password you want to generate : "))
        length = int(input("Enter the password length : "))

        if length < 4:
            print("Password length should be at least 4 characters")
            return
        print("Here are your passwords:")
        for _ in range(passwords_num):
            print(generate_password(length))
    except ValueError:
        print("enter valid number")

if __name__=="__main__":
    main()
