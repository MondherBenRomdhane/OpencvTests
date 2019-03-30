import cv2
import numpy as np

img = cv2.imread('img.png')
#print('img shape' + str(img.shape))
rows,cols,channels = img.shape

roi = img[0:rows,0:cols]

img2gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,mask = cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)

cv2.imshow('same window ??',roi)
cv2.imshow('gray version',img2gray)
cv2.imshow('thresholded',mask)

cv2.waitKey(0)
cv2.destroyAllWindows()