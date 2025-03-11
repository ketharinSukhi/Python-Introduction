from PIL import Image, ImageDraw, ImageFont

image1 =Image.open('image1.jpg')

#show image
image1.show()
#save in png 
image1.save('image_1.png')
#Resizing an Image (width, height)
resized_image = image1.resize((300, 300))
resized_image.show()
#Converting Image to Grayscale
gray_image = image1.convert("L")
gray_image.show()
#Rotating an Image
rotated_image = image1.rotate(90)
rotated_image.show()
#cropping an Image
# (left, upper, right, lower) - Cropping coordinates
cropped_image = image1.crop((50, 50, 200, 200))
cropped_image.show()
# Create a drawing object
draw = ImageDraw.Draw(image1)

# Add text (requires a font file)
draw.text((10, 10), "Hello!", fill="red")

image1.show()


#Applying Filter
from PIL import ImageFilter 
blurred = image1.filter(ImageFilter.BLUR) 
blurred.show() 
sharpened = image1.filter(ImageFilter.SHARPEN) 
sharpened.show()
