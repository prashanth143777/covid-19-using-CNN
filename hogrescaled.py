#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 01:30:42 2020

@author: root
"""

import cv2

import os,glob


from skimage.feature import hog
from skimage import data, exposure



from os import listdir,makedirs

from os.path import isfile,join
path = '/root/Desktop/covid-19/Dataset/hogcovid' # Source Folder
dstpath = '/root/Desktop/covid-19/Dataset/hogrescalecovid' # Destination Folder
try:
    makedirs(dstpath)
except:
    print ("Directory already exist, images will be written in same folder")
# Folder won't used
files = [f for f in listdir(path) if isfile(join(path,f))] 
for image in files:
    try:
        img = cv2.imread(os.path.join(path,image))
        hog_image_rescaled = exposure.rescale_intensity(img, in_range=(0, 50))
        dstPath = join(dstpath,image)
        cv2.imwrite(dstPath,hog_image_rescaled)
    except:
        print ("{} is not converted".format(image))
for fil in glob.glob("*.jpg"):
    try:
        image = cv2.imread(fil) 
        hog_image_rescaleded = exposure.rescale_intensity(image, in_range=(0, 50))
        cv2.imwrite(os.path.join(dstpath,fil),hog_image_rescaleded)
    except:
        print('{} is not converted')
