import cv2
import numpy as np

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

cv2.namedWindow("Tracking")

cv2.createTrackbar("LowerHue", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LowerLightness", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LowerSaturation", "Tracking", 0, 255, nothing)

cv2.createTrackbar("UpperHue", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UpperLightness", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UpperSaturation", "Tracking", 255, 255, nothing)

while(True):
    ret, frame = cap.read()
    hlsFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS) #convert rgb->hsv

    #Trackbars
    lowerHue = cv2.getTrackbarPos("LowerHue", "Tracking")
    lowerSaturation = cv2.getTrackbarPos("LowerSaturation", "Tracking")
    lowerLightness = cv2.getTrackbarPos("LowerLightness", "Tracking")

    upperHue = cv2.getTrackbarPos("UpperHue", "Tracking")
    upperSaturation = cv2.getTrackbarPos("UpperSaturation", "Tracking")
    upperLightness = cv2.getTrackbarPos("UpperLightness", "Tracking")

    """
    White in HLS: just the top of the cylinder, ie:
    (0, 250, 0) -> (255, 255, 255)
    """

    #Ranges
    lowerRange = np.array([lowerHue, lowerSaturation, lowerLightness]) #lower color values in hls
    upperRange = np.array([upperHue, upperSaturation, upperLightness]) #upper limit for color

    #threshold the image to filter out everything not in [lowerBlue, upperBlue]
    mask = cv2.inRange(hlsFrame, lowerRange, upperRange)

    #to get only the filtered image, use bitwise_and, and apply the mask we created
    res = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", res)

    key = cv2.waitKey(1) & 0xFF
    if key == 27: #ie esc key
        break

cap.release()
cv2.destroyAllWindows()