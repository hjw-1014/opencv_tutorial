import cv2 as cv
import numpy as np

img = cv.imread('lena.jpg')
layer = img.copy()
gp = [layer]

# lr1 = cv.pyrDown(img)
# lr2 = cv.pyrDown(lr1)
# hr2 = cv.pyrUp(lr2)
for i in range(6):
    layer = cv.pyrDown(layer)
    gp.append(layer)
    #cv.imshow(str(i), layer)

layer = gp[5]
cv.imshow('upper level Gaussian Pyramid', layer)
lp = [layer]

for i in range(5, 0, -1):
    gaussian_extended = cv.pyrUp(gp[i])
    laplacian = cv.subtract(gp[i-1], gaussian_extended)
    cv.imshow(str(i), laplacian)

cv.imshow('Original image', img)
# cv.imshow('pyrdown 1 image', lr1)
# cv.imshow('pyrdown 2 image', lr2)
# cv.imshow('pyrUp 2  image', hr2)
cv.waitKey(0)
cv.destroyAllWindows()