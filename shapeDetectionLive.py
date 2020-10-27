import cv2
import numpy as np

camera = 0
cap = cv2.VideoCapture(camera)

while cap.isOpened():
    ret, frame = cap.read()
    imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #if pixel < thresh, pixel = black. Else: pixel = max value
    #_, thresh = cv2.threshold(imgray, 1, 160, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(imgray, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        approx = cv2.approxPolyDP(contour, 1, closed=True)
        #cv2.drawContours(frame, [approx], -1, (0, 0, 0), 4)
        x, y, w, h = cv2.boundingRect(approx)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 0), 2)

    #cv2.imshow("test", thresh)
    cv2.imshow("feed", frame)
    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()