#!/usr/bin/python


import cv2
#starting camera
cap = cv2.VideoCapture(0)


#ading plugin
plugin=cv2.VideoWriter_fourcc(*'XVID')

output=cv2.VideoWriter('class.mp4',plugin,20,(480,640))
while cap.isOpened():
	status,frame=cap.read()



	cv2.imshow('live',frame-255)

	if cv2.waitKey(10) & 0xff == ord('q'): # ord function is used to grab q key from keyboard
		break


cv2.destroyWindow('live')
#cv2.destroyAllWindows  -> to destroy all window
 
#to close camera

cap.realease()
