import numpy as np
import cv2


img = cv2.imread('messi5.jpg')
img2 = cv2.imread('opencv-logo.png')
img3 = cv2.imread('rly.jpeg')
img4 = cv2.imread('hjw.jpeg')

print(img.shape)
print(img.size)
print(img.dtype)


b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))
img3 = cv2.resize(img3, (512, 512))
img4 = cv2.resize(img4, (512, 512))


## combine
dst = cv2.add(img, img2)
dst2 = cv2.addWeighted(img, 0.9, img2, 0.1, 0)
dst3 = cv2.addWeighted(img3, 0.5, img2, 0.5, 0)

cv2.imshow('image', dst3)
k = cv2.waitKey(2000)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows()