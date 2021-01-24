import matplotlib.pyplot as plt

from skimage.feature import hog
from skimage import data, exposure
from skimage.io import imread
from skimage.io import imshow
import cv2

import os,glob

from os import listdir,makedirs

from os.path import isfile,join
path = '/root/Desktop/covid-19/Dataset/segcovid' # Source Folder
dstpath = '/root/Desktop/covid-19/Dataset/hogcovid' # Destination Folder
try:
    makedirs(dstpath)
except:
    print ("Directory already exist, images will be written in same folder")
# Folder won't used
files = [f for f in listdir(path) if isfile(join(path,f))] 
for image in files:
    try:
        img = cv2.imread(os.path.join(path,image))
        fd, hog_image = hog(img, orientations=8, pixels_per_cell=(16, 16),
                    cells_per_block=(1, 1), visualize=True, multichannel=True)
        dstPath = join(dstpath,image)
        cv2.imwrite(dstPath,hog_image)
    except:
        print ("{} is not converted".format(image))
for fil in glob.glob("*.jpg"):
    try:
        image = cv2.imread(fil) 
        fd, hog_images = hog(image, orientations=8, pixels_per_cell=(16, 16),
                    cells_per_block=(1, 1), visualize=True, multichannel=True)
        cv2.imwrite(os.path.join(dstpath,fil),hog_images)
    except:
        print('{} is not converted')
