import cv2
import numpy as np

ptValues = [0,0,0]
globtsh = 0

def AdaptiveSensibility(var):
	global globtsh 
	globtsh = var

def printCoordinates(event, x, y, flags, param):
	global img
	global ptValues
	if (event == 1):
		ptValues=img[y, x]

img = cv2.imread("img.png")
img1 = img
cv2.namedWindow("frame")
cv2.namedWindow("frameInput")
cv2.setMouseCallback("frameInput", printCoordinates)
cv2.createTrackbar("adaptive Tsh","frameInput",0,255,AdaptiveSensibility)

#cv2.imshow("Frame",img)

while True :
	lowerTsh = np.array([ptValues[0],ptValues[1],ptValues[2]])+globtsh
	highTsh =  np.array([ptValues[0],ptValues[1],ptValues[2]])-globtsh
	#ret,mask = cv2.threshold(img2gray,K,255,cv2.THRESH_BINARY)
	mask = cv2.inRange(img1,lowerTsh,highTsh)
	inv_mask =cv2.bitwise_not(mask)
	cv2.imshow("frame",inv_mask)
	cv2.imshow("frameInput",mask)
#
#	#res = cv2.bitwise_and(img1,img1,mask=mask)
#	#edges = cv2.Canny(res,100,200)
#	##tres = cv2.bitwise_or(img,img,mask=edges)
#	#cv2.imshow("frame",edges)
	##cv2.imshow("frameInput",img)

	if cv2.waitKey(1) & 0xFF==ord('q'):
		break

cv2.waitKey(0)
cv2.destroyAllWindows()