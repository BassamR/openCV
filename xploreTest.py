import cv2
import numpy as np

#This is a first draft of the ARtag detector

"""Notes:
-is the diff of frames necessary? the camera isnt really detecting a moving object
    - =>No it isnt necessary
-find the artag using edges/contours/shape detection, then track it using some method
-Using thresholds: if pixel < 20 then its black, else its white (maybe use adaptive)
    => the artag should ideally be the only black object
-Properly thresh the image, then edge/contour/shape detect the artag
-Place bounding box
-Once ^ is confirmed, refine the tracking / get the coords
-Convert coords
"""

def threshFrame():
    pass

def computeDistance():
    pass

videoSource = 0 #PC webcam
cap = cv2.VideoCapture(videoSource)

while cap.isOpened():
    ret, frame = cap.read()

    #stuff

    cv2.imshow("feed", frame)
    if cv2.waitKey(40) == 27: #press esc to stop
        break

cv2.destroyAllWindows()
cap.release()