#!usr/bin/python

import cv2
import numpy as np
#checking version
print(cv2.__version__)


#image reading

# 1 means image in same color channel --grb or RGB
# 0 MEANS no color channel -- black white -- gray image 
# -1 maintain image transparency
img = cv2.imread('dog.jpg')

myimg = np.zeros((512,512))

cv2.line(img,(0,0),(200,300),(0,0,255))
cv2.rectangle(img,(50,50),(200,500),(0,0,255),2)


cv2.imshow('my',img)
#wait for window to close
cv2.waitKey(0)   #milli/micro seconds

