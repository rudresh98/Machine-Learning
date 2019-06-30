*#!usr/bin/python

import cv2

#checking version
print(cv2.__version__)


#image reading

# 1 means image in same color channel --grb or RGB
# 0 MEANS no color channel -- black white -- gray image 
# -1 maintain image transparency
img = cv2.imread('dog.jpg')
#split into bgr

x,y,z=cv2.split(img)


cv2.imshow('dog',myimg)


cv2.imshow('dog1',x)
cv2.imshow('dog2',y)
cv2.imshow('dog3',z)
#wait for window to close
cv2.waitKey(0)   #milli/micro seconds

