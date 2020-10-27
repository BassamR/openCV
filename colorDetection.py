import cv2
import numpy as np

def nothing(x):
    pass

cv2.namedWindow("Tracking")

cv2.createTrackbar("LowerHue", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LowerSaturation", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LowerValue", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UpperHue", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UpperSaturation", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UpperValue", "Tracking", 255, 255, nothing)

while(True):
    frame = cv2.imread("smarties.png")
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #convert rgb->hsv

    lowerHue = cv2.getTrackbarPos("LowerHue", "Tracking")
    lowerSaturation = cv2.getTrackbarPos("LowerSaturation", "Tracking")
    lowerValue = cv2.getTrackbarPos("LowerValue", "Tracking")

    upperHue = cv2.getTrackbarPos("UpperHue", "Tracking")
    upperSaturation = cv2.getTrackbarPos("UpperSaturation", "Tracking")
    upperValue = cv2.getTrackbarPos("UpperValue", "Tracking")

    lowerBlue = np.array([lowerHue, lowerSaturation, lowerValue]) #lower blue values in hsv
    upperBlue = np.array([upperHue, upperSaturation, upperValue]) #upper limit for blue

    #threshold the image to filter out everything not in [lowerBlue, upperBlue]
    mask = cv2.inRange(hsvFrame, lowerBlue, upperBlue)

    #to get only the filtered image, use bitwise_and, and apply the mask we created
    res = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", res)

    key = cv2.waitKey(1) & 0xFF
    if key == 27: #ie esc key
        break


cv2.destroyAllWindows()