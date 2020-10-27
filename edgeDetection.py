import cv2
import numpy as np
from matplotlib import pyplot as plt

#img = cv2.imread("sudoku.png", cv2.IMREAD_GRAYSCALE)
img = cv2.imread("messi5.jpg", cv2.IMREAD_GRAYSCALE)

#LAPLACIAN GRADIENT
#input: image source, datatype (here 64bit float), ksize for how strict do we have to be with edges
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
#reconvert back to unsigned int, and take absolute values
lap = np.uint8(np.absolute(lap))

#SOBEL GRADIENT
#3rd & 4th input: dx and dy either 1 or 0. dx=1 dy=0 -> only do it in x direction
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelXY = cv2.Sobel(img, cv2.CV_64F, 1, 1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
sobelXY = np.uint8(np.absolute(sobelXY))
#combine both x and y using bitwise or
sobelCombined = cv2.bitwise_or(sobelX, sobelY)

#CANNY EDGE DETECTION
canny = cv2.Canny(img, 100, 200)
#source, threshold 1, threshold 2
#try and do thresholds with trackbars :p


#SHOWING THE IMAGES
titles = ['image', 'laplacian', 'sobelX', 'sobelY', 'sobelXY', 'sobelCombined', 'canny']
images = [img, lap, sobelX, sobelY, sobelXY, sobelCombined, canny]

for i in range(7):
    plt.subplot(3, 3, 1+i), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()