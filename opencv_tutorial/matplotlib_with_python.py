import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('sudoku.png', 0)

cv.imshow('Image', img) #BGR
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

plt.imshow(img) #RGB
#plt.xticks([]), plt.yticks([])
plt.show()


k = cv.waitKey(4000)
if k == 27:
    cv.destroyAllWindows()
elif k == ord('q'):
    cv.destroyAllWindows()

