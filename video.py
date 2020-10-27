import numpy as np
import cv2

#1st argument is either input file name or camera device index (0 or -1 or 1 or 2)
cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*"XVID")

#1st argument is name of output, 2nd argument is 4cc code, 3rd is fps, 4th is size
out = cv2.VideoWriter("output.avi", fourcc, 20, (640, 480))

while(cap.isOpened()):
    #if frame is available it returns true and saves it in ret, and frame is saved in frame
    ret, frame = cap.read()

    if ret == True:
        out.write(frame)
            
        #get certain properties of the prop (cf documentation for more)
        #width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) #cap.get(3) works, every property has a number
        #height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        #print(width, height)

        #converts colors of the frame, here to gray
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("frame", grey) #shows frame
        #print(grey)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break #if we press q, exit loop

    else:
        break


cap.release()
out.release()
cv2.destroyAllWindows()