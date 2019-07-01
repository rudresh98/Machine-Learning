#!usr/bin/python
import sys
import cv2

print(cv2.__version__)


#data = sys.argv[1]

img =cv2.imread('data.jpeg',1)
img1 =cv2.imread('data.jpeg',0)
print(img)


print(img.shape)


cv2.imshow('dog',img-50)
cv2.imshow('dogor',0)
cv2.imshow('dog2',img-100)


cv2.imwrite('newdog.jpeg',img1)
cv2.waitKey(0)
