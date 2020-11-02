import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

img = cv.imread('j.png', cv.IMREAD_GRAYSCALE)
#_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)

kernel = np.ones((5, 5), np.uint8)
dilation = cv.dilate(img, kernel=kernel, iterations=2)
erosion = cv.erode(img, kernel, iterations=2)
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
mg = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
th = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)


title = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th']
image = [img, img, dilation, erosion, opening, closing, mg, th]

for i in range(len(image)):
    plt.subplot(2, 4, i+1)
    plt.imshow(image[i], 'gray')
    plt.xticks([])
    plt.yticks([])
    plt.title(title[i])

plt.show()