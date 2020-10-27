import cv2 as cv
import numpy as np

def nothing(x): #value of current position of trackbar
    print(x)
    return


img = np.zeros([300, 512, 3], np.uint8)
cv.namedWindow("image")

#inputs: (unique name, name of the window, init value, final value, callback function)
cv.createTrackbar("B", "image", 0, 255, nothing)
cv.createTrackbar("G", "image", 0, 255, nothing)
cv.createTrackbar("R", "image", 0, 255, nothing)

switch = "0: OFF\n 1: ON"
cv.createTrackbar(switch, "image", 0, 1, nothing)

while(True):
    cv.imshow("image", img)
    key = cv.waitKey(1) & 0xFF
    if key == 27: #ie escape key
        break

    b = cv.getTrackbarPos("B", "image") #name + window in which the trackbar is present
    g = cv.getTrackbarPos("G", "image")
    r = cv.getTrackbarPos("R", "image")
    s = cv.getTrackbarPos(switch, "image")

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b, g, r]

cv.destroyAllWindows()