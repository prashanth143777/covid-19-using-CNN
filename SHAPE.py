from PIL import Image
import glob
import os

#img_path = '/root/Desktop/le.png'
#im = Image.open(img_path)
#print('{}' .format(im.format))
#print('size: {}' .format(im.size))
#print('image mode: {}' .format(im.mode))
#im.show

image_list = []
resized_images = []

for filename in glob.glob('/root/Desktop/covid-19/Dataset/CT_COVID/*.png'):
	print(filename)
	img = Image.open(filename)
	image_list.append(img)
for image in image_list:
	image = image.resize((300,300))
	resized_images.append(image)
for(i, new) in enumerate(resized_images):
	new.save('{}{}{}' .format('/root/Desktop/covid-19/Dataset/New_shapes/shape' ,i+1, '.png'))
