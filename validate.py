email = input("what's your email ").strip()

if "@" in email:
    print(f"{email} is valid")
else:
    print("invalid")











"""import sys

from PIL import Image
images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)

image [0].save(
    "costume.gif", save_all=True, append_images=[images[1]], duration=200, loop=0
)"""
