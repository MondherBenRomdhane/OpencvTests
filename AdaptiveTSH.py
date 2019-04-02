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

length,widh,NULL = img.shape
BlueImgimg2gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
GreenImgimg2gray =  cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
RedImgimg2gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

##transform BRG to each plan greyscale
#for i in range (0,length-1):
#	for j in range (0,widh-1):
#		BlueImgimg2gray[i][j] = (img[i][j])[0]
#		GreenImgimg2gray[i][j] = (img[i][j])[1]
#		RedImgimg2gray[i][j] = (img[i][j])[2]

#transform BRG to each plan greyscale
GreenImg = img.copy()
BlueImg = img.copy()
RedImg = img.copy()



for i in range (0,length-1):
	for j in range (0,widh-1):
		BlueImg[i][j] = [(BlueImg[i][j])[0],0,0]
		GreenImg[i][j] = [0,(GreenImg[i][j])[1],0]
		RedImg[i][j] = [0,0,(RedImg[i][j])[2]]

cv2.imshow("BLUE",BlueImg)
cv2.imshow("GReen",GreenImg)
cv2.imshow("Red",RedImg)

cv2.namedWindow("frame")
cv2.namedWindow("frameInput")
cv2.setMouseCallback("frameInput", printCoordinates)
cv2.createTrackbar("adaptive Tsh","frameInput",0,255,AdaptiveSensibility)

#cv2.imshow("Frame",img)

while True :
	lowerTsh = np.array([ptValues[0],ptValues[1],ptValues[2]])-globtsh
	highTsh =  np.array([ptValues[0],ptValues[1],ptValues[2]])+globtsh
	#ret,mask = cv2.threshold(img2gray,K,255,cv2.THRESH_BINARY)
	mask = cv2.inRange(img1,lowerTsh,highTsh)
	inv_mask =cv2.bitwise_not(mask)
	cv2.imshow("frame",inv_mask)
	cv2.imshow("frameInput",img1)
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