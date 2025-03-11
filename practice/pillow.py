from PIL import Image

image1 =Image.open('image1.jpg')
#show image
image1.show()
#save in png 
image1.save('image_1.png')
#Resizing an Image (width, height)
resized_image = image1.resize((300, 300))
resized_image.show()