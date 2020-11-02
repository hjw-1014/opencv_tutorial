#remove noise
import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

img = cv.imread('lena.jpg')
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32)/25
dst = cv.filter2D(img, -1, kernel)
blur = cv.blur(img, (3, 3))
gblur = cv.GaussianBlur(img, (3, 3), 0)
median = cv.medianBlur(img, 5)
bilateralFilter = cv.bilateralFilter(img, 9, 75, 75)

titles = ['opencv', '2D convolution', 'blur',
          'Gaussianblur', 'median', 'bilateralFilter']
image = [img, dst, blur, gblur, median, bilateralFilter]

for i in range(len(image)):
    plt.subplot(2, 3, i+1)
    plt.imshow(image[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()