import re
text = "Python is great!"
match = re.match(r"Python", text)
if match:
    print("Match found at the beginning!")