import cv2
import numpy as np

cap = cv2.VideoCapture(0) # choose right webcam video input

width = cap.get(3)
height = cap.get(4)

print ('height = '+str(height))
print ('width = '+ str(width))

while True:
	ret, frame = cap.read()
	#print('img shape' + str(frame.shape))
	#draw line
	cv2.line(frame,(int(width/2),0),(int(width/2),int(height)),(255,0,0),30,8)
	cv2.imshow('smile this is the camera',frame)
	if cv2.waitKey(1) & 0xFF==ord('q') :
		break

cap.release()
cv2.destroyAllWindows()
