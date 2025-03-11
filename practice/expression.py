import re
email = input("what's your email? ").strip()

username, domain = email.split("@")

if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.com$", email, re.IGNORECASE): #\w=[a-zA-Z0-9_]
    print("valid")
else:
    print("Invalid")