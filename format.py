"""import re
name = input("what's your name? ").strip()

if matches:= re.search(r"^(.+), (.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello,{name}")"""

#facebook URL
import re
url = input("URL : ").strip()

if matches:=re.search(r"^https?://(www\.)?facebook\.com/(.+)$" , url, re.IGNORECASE):
    print(f"Username:" , matches.group(2))


