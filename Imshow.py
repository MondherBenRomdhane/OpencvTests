import cv2
import matplotlib.pyplot as pt

img = cv2.imread('img.png',1)

#cv2.imshow('test window name',img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

pt.imshow(img ,camp = 'gray' , interpolation = 'bicubic')
