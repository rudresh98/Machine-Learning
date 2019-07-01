#!/usr/bin/python


import cv2
#starting camera
cap = cv2.VideoCapture(0)

while cap.isOpened():
	status,frame=cap.read()

	#converting image frame into gray scale
	grayimg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	#print(frame.shape)
	#now we can draw all those patterns
	#line
	cv2.line(frame,(0,0),(200,300),(0,255,0),3)
	cv2.rectangle(frame,(50,50),(250,300),(0,0,255),2)
	cv2.circle(frame,(100,200),250,(0,0,255),2)
	cv2.imshow('live',frame-255)
	font= cv2.FONT_HERSHEY_SIMPLEX
	cv2.putText(frame,'RUDRESH',(10,50),font,2,(0,2,55),2,cv2.LINE_AA)

	#cv2.imshow('livegray',grayimg)
	if cv2.waitKey(10) & 0xff == ord('q'): # ord function is used to grab q key from keyboard
		break


cv2.destroyWindow('live')
#cv2.destroyAllWindows  -> to destroy all window
 
#to close camera

cap.realease()
