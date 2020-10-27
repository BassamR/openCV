import cv2
import numpy as np

img = cv2.imread("sudoku.png")
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#source, maxvalue (nonzero value assigned to pixel if pixel>thresh), method, type, block size, C
#2 adaptive methods: cv2.ADAPTIVE_THRESH_MEAN_C and cv2.ADAPTIVE_THRESH_GAUSSIAN_C
#blocksize decides the size of the neighborhood area (has to be an odd number >1)
#C: cte substracted from the mean
th1 = cv2.adaptiveThreshold(imgray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 2)
th2 = cv2.adaptiveThreshold(imgray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)


cv2.imshow("original", imgray)
cv2.imshow("thresh1", th1)
#cv2.imshow("thresh2", th2)

cv2.waitKey(0)
cv2.destroyAllWindows()