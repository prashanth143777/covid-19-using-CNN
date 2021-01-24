import cv2
import numpy as np
import os,glob

from os import listdir,makedirs

from os.path import isfile,join
path = '/root/Desktop/covid-19/Dataset/hist covid' # Source Folder
dstpath = '/root/Desktop/covid-19/Dataset/kmeanseg covid' # Destination Folder
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
	img2 = img.reshape((-1,3))
	img2 = np.float32(img2)
	criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
	k = 5
	attempts = 10
	ret,label,center=cv2.kmeans(img2, k, None, criteria, attempts, cv2.KMEANS_PP_CENTERS)
	center = np.uint8(center)
	res = center[label.flatten()]
	res2 = res.reshape((img.shape))
        dstPath = join(dstpath,image)
        cv2.imwrite(dstPath,res2)
    except:
        print ("{} is not converted".format(image))
for fil in glob.glob("*.jpg"):
    try:
        image = cv2.imread(fil) 
        #gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # convert to greyscale
	img2 = img.reshape((-1,3))
	img2 = np.float32(img2)
	criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
	k = 5
	attempts = 10
	ret,label,center=cv2.kmeans(img2, k, None, criteria, attempts, cv2.KMEANS_PP_CENTERS)
	center = np.uint8(center)
	res = center[label.flatten()]
	res3 = res.reshape((img.shape))
        cv2.imwrite(os.path.join(dstpath,fil),res3)
    except:
        print('{} is not converted')
