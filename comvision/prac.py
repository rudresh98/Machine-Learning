#!usr/bin/python

import cv2


#checking version
print(cv2.__version__)

#image reading 

img = cv2.imread('dog.jpg',0)



cv2.imshow('dog',img)


cv2.waitKey(0)
