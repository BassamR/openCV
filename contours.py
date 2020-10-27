import cv2
import numpy as np 

img = cv2.imread("opencv-logo.png")
#imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #cuz working with grey is less buggy
imgray = cv2.imread("opencv-logo.png", cv2.IMREAD_GRAYSCALE)

#source, threshhold, maxvalue, type
ret, thresh = cv2.threshold(imgray, 127, 255, 0)

#source, contour mode, contour approximation method,
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
#contours is a list that contains all contours
#contours are an array of (x,y) that represent the boundary point of the object
print("number of contours = " + str(len(contours)))
print(contours[0])

#image on which contours are drawn, contours, contours indexes (-1 for all), color, thickness
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

cv2.imshow("image", img)
#cv2.imshow("imageGray", imgray)

cv2.waitKey(0)
cv2.destroyAllWindows()