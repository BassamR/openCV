import cv2 #openCV
import numpy as np

img = cv2.imread("lena.jpg", 0)
#2nd argument represents flag. 1 for color, 0 for grayscale, -1 for unchanged, with alpha channels

#print(img) #prints out matrix of rgb values

cv2.imshow("image", img) #1st argument is name of the window, 2nd variable is the image
key = cv2.waitKey(0) & 0xFF
#ie wait for 5k ms. Give it 0, and the window wont close. The &wtv is a mask for 64bit machines

if key == 27: #ie esc key
    cv2.destroyAllWindows() #self explanatory
elif key == ord("s"):
    cv2.imwrite("lena_copy.png", img) #1st argument is name, 2nd argument is image variable
    cv2.destroyAllWindows()

