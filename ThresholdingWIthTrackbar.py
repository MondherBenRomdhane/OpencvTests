import cv2
import numpy as np

HUEHighSlide = 0
HUELowSlide = 0

SatHighSlide = 0
SatLowSlide = 0

ValHighSlide = 0
ValLowSlide = 0

def HueHigh(a):
	global HUEHighSlide 
	HUEHighSlide = a

def HueLow(a):
	global HUELowSlide 
	HUELowSlide = a

def SatHigh(a):
	global SatHighSlide 
	SatHighSlide = a

def SatLow(a):
	global SatLowSlide 
	SatLowSlide = a

def ValHigh(a):
	global ValHighSlide 
	ValHighSlide = a

def ValLow(a):
	global ValLowSlide 
	ValLowSlide = a

img = cv2.imread('img.png')
cv2.namedWindow("frame")
cv2.createTrackbar("High Hue","frame",0,255,HueHigh)
cv2.createTrackbar("Low Hue","frame",0,255, HueLow )

cv2.createTrackbar("High Sat","frame",0,255,SatHigh)
cv2.createTrackbar("Low Sat","frame",0,255, SatLow )

cv2.createTrackbar("High Val","frame",0,255,ValHigh)
cv2.createTrackbar("Low Val","frame",0,255, ValLow )

#img2gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow("frame",img)


while True :
	lowerTsh = np.array([HUELowSlide,SatLowSlide,ValLowSlide])
	highTsh =  np.array([HUEHighSlide,SatHighSlide,ValHighSlide])
	#ret,mask = cv2.threshold(img2gray,K,255,cv2.THRESH_BINARY)
	mask = cv2.inRange(img,lowerTsh,highTsh)
	res = cv2.bitwise_and(img,img,mask=mask)
	cv2.imshow("frame",res)

	if cv2.waitKey(1) & 0xFF==ord('q'):
		break

cv2.waitKey(0)
cv2.destroyAllWindows()

