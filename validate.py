import re
email = input("what's your email? ").strip()

username, domain = email.split("@")

if re.search(".+@.+", email):
    print("valid")
else:
    print("Invalid")










"""import sys

from PIL import Image
images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

image [0].save(
    "costume.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)"""
