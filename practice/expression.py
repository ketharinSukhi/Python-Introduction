#email validation
import re
email = input("what's your email? ").strip()

username, domain = email.split("@")

if re.search(r"^(\w|\.)+@(\w+\.)?\w+\.com$", email, re.IGNORECASE): #\w=[a-zA-Z0-9_]
    print("valid")
else:
    print("Invalid")

#facebook URL
import re
url = input("URL : ").strip()

if matches:=re.search(r"^https?://(?:www\.)?facebook\.com/(.+)$" , url, re.IGNORECASE):
    print(f"Username:" , matches.group(1))