import cv2
import numpy as np

img1 = np.zeros([250, 500, 3], np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img2 = cv2.imread("image_2.png")

#black is 0, white is 1
bitAnd = cv2.bitwise_not(img2, img1)

cv2.imshow("image1", img1)
cv2.imshow("image2", img2)
cv2.imshow("bitAnd", bitAnd)

key = cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()