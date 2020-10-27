import cv2
import numpy as np

#img = cv2.imread("lena.jpg", 1)
#print(img.shape) #gives tuple (width, height)

img = np.zeros([512, 512, 3], np.uint8) #3D array, necessaire car chaque pixel = [R, G, B]
#print(img)

for line in img:
    for col in line:
        for i in range(3): #r,g,b values for each pixel
            col[i] = 100

#BLUE-GREEN-RED FORMAT, NOT THE USUAL RGB FORMAT! thickness goes from 1 to ...
#systeme de coords format image, cf archipelago
img = cv2.line(img, (0, 0), (200, 500), (0, 0, 255), 5) #draws line
img = cv2.arrowedLine(img, (512, 512), (255, 255), (0, 255, 0), 5) #draws arrowed line 

#coords are top left vertex + bottom right vertex
img = cv2.rectangle(img, (100, 100), (300, 300), (10, 100, 200), 5)
img = cv2.rectangle(img, (400, 0), (512, 100), (0, 0, 255), -1) #-1 = fill the rectangle

img = cv2.circle(img, (400, 300), 100, (255, 0, 0), 5)

font = cv2.FONT_HERSHEY_COMPLEX
linetype = cv2.LINE_AA
img = cv2.putText(img, "yeet", (0, 400), font, 4, (255, 255, 255), 10, linetype)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()