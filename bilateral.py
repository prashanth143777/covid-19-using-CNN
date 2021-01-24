import cv2

import os,glob

from os import listdir,makedirs

from os.path import isfile,join
path = '/root/Desktop/covid-19/Dataset/covid data' # Source Folder
dstpath = '/root/Desktop/covid-19/Dataset/bilateral covid' # Destination Folder
try:
    makedirs(dstpath)
except:
    print ("Directory already exist, images will be written in same folder")
# Folder won't used
files = [f for f in listdir(path) if isfile(join(path,f))] 
for image in files:
    try:
        img = cv2.imread(os.path.join(path,image))
        #gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        bilateral = cv2.bilateralFilter(img, 15, 75, 75) 
        dstPath = join(dstpath,image)
        cv2.imwrite(dstPath,bilateral)
    except:
        print ("{} is not converted".format(image))
for fil in glob.glob("*.jpg"):
    try:
        image = cv2.imread(fil) 
        #gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # convert to greyscale
        bilateral_image = cv2.bilateralFilter(img, 15, 75, 75) 
        cv2.imwrite(os.path.join(dstpath,fil),bilateral_image)
    except:
        print('{} is not converted')
