import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('sudoku.png', cv.IMREAD_GRAYSCALE)
lap = cv.Laplacian(img, cv.CV_64F, ksize=3)
lap = np.uint8(np.abs(lap))
sobelX = cv.Sobel(img, cv.CV_64F, 1, 0, )
sobelY = cv.Sobel(img, cv.CV_64F, 0, 1)
edges = cv.Canny(img, 100, 200)
sobelX = np.uint8(np.abs(sobelX))
sobelY = np.uint8(np.abs(sobelY))
sobelCombined = cv.bitwise_or(sobelX, sobelY) #useful!!

titles = ['image', 'laplacian', 'sobelX', 'sobelY',
          'sobelCombined', 'edges']
images = [img, lap, sobelX, sobelY, sobelCombined,edges]

for i in range(len(images)):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
