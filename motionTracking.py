import cv2
import numpy as np 

cap = cv2.VideoCapture("vtest.avi")

ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    """
    find difference between 2 adjacent frames (gets rid of "constant" background items)
    cvt to gray cuz we want contours, and working with gray > working with rgb
    blur to eliminate noise
    threshold the image
    dilate
    find contours
    draw contours on original frame (1)
    show original frame
    assign frame1 to the next frame (ie frame2), and assign frame2 to the frame after it

    (1) improvement:
    iterate on the contours and find the bounding rectangle on each contour 
    find the area of the rect. if area < some value then the contour isnt a human contour
    """
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, ksize=(5, 5), sigmaX=0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, kernel=None, iterations=3)

    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        (x, y, width, height) = cv2.boundingRect(contour)
        
        minArea = 700
        if cv2.contourArea(contour) < minArea:
            continue #skip this iteration of the for loop
        
        cv2.rectangle(frame1, (x, y), (x+width, y+height), (0, 255, 0), 2)
        cv2.putText(frame1, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 
                    1, (0, 0, 255), 3)

    #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
    cv2.imshow("feed", frame1)

    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()