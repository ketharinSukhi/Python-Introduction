"""import re
name = input("what's your name? ").strip()

if matches:= re.search(r"^(.+), (.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello,{name}")"""

#facebook URL

url = input("URL : ").strip()

username = url.replace("https://www.facebook.com/" , "")
print(f"Username: {username}")


