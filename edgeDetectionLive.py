import cv2
import numpy as np
from matplotlib import pyplot as plt

camera = 0
cap = cv2.VideoCapture(camera)

while cap.isOpened():
    ret, frame = cap.read()
    imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #if pixel < thresh, pixel = black. Else: pixel = max value
    #ret, thresh = cv2.threshold(imgray, 150, 255, 0)
    thresh = cv2.adaptiveThreshold(imgray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 3)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    #cv2.drawContours(frame, contours, -1, (0, 0, 0), 3)

    for contour in contours:
        approx = cv2.approxPolyDP(contour, 7, closed=True)
        cv2.drawContours(frame, [approx], -1, (0, 0, 0), 1)

    cv2.imshow("test", thresh)
    cv2.imshow("feed", frame)
    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()