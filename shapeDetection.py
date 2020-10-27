import cv2
import numpy as np
from math import pow

img = cv2.imread("shapes.jpg")
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#thresh the gray image and find contours
_, thresh = cv2.threshold(imgray, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

#iterate: draw each contour, put the name of the shape on the shape
for contour in contours:
    #curve, epsilon, closed (bool, is shape closed?)
    #approximates a shape using polygons, returns array of contours containing the polygon
    #epsilon = distance from original curve. 0 is the most precise, go higher for sth else
    #approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, closed=True), closed=True)
    approx = cv2.approxPolyDP(contour, 3, closed=True)
    cv2.drawContours(img, [approx], -1, (0, 0, 0), 1)

    #Printing the name of the shape:
    x = approx.ravel()[0]
    y = approx.ravel()[1] #finds coords of starting point of the approx

    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0), 1)

    elif len(approx) == 4:
        x, y, w, h = cv2.boundingRect(approx)
        aspectRatio = float(w)/h

        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
            cv2.putText(img, "Square", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0), 1)
        else:
            cv2.putText(img, "Rectangle", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0), 1)

    elif len(approx) == 5:
        cv2.putText(img, "Pentagon", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0), 1)

    elif len(approx) == 6:
        cv2.putText(img, "Hexagon", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0), 1)

    elif len(approx) == 10:
        cv2.putText(img, "Star", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0), 1)

    else:
        cv2.putText(img, "Circle", (x,y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0), 1)

    #cv2.putText(img, "OK", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 6)

cv2.imshow("shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()