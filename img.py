#!usr/bin/python

import cv2

#checking version
print(cv2.__version__)


#image reading

# 1 means image in same color channel --grb or RGB
# 0 MEANS no color channel -- black white -- gray image 
# -1 maintain image transparency
img = cv2.imread('dog.jpg',0)
img1 = cv2.imread('dog.jpg',1)
img2 = cv2.imread('dog.jpg',-1)

#print(img)


#print shape
#print(img.shape)

#print image type
#print(type(img))


#to display image

#cv2.imshow('dog',img)
#cv2.imshow('dog',img1)
cv2.imshow('dog',img2)

#wait for window to close
cv2.waitKey(0)   #milli/micro seconds

