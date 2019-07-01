#!/usr/bin/python


import cv2
#starting camera
cap = cv2.VideoCapture(0)


#this is first camera


#this to check camera started or not 
open=cap.isOpened()

print(open)

if open:
	print ("camera is ready to click picture")
else:
	print ("check your web cam")


#now read input from camera

status,readpic=cap.read()

print (readpic)

cv2.imshow('imag',readpic)
cv2.waitKey(0)


#closing camera

cap.release()

