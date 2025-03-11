import re

email = input("Enter your email").strip()

username, domain = email.split("@") 

if username and domain.endswith(".com"):
    print("Valid")
else:
    print("Invalid")