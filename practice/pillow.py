from PIL import Image, ImageDraw, ImageFont

image1 =Image.open('image1.jpg')

# Create a drawing object
draw = ImageDraw.Draw(image1)

# Add text (requires a font file)
draw.text((20, 20), "Hello!", fill="green")

image1.show()