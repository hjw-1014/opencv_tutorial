# tut_1 read and write image
import numpy as np
import cv2
#img = cv2.imread('lena.jpg', 1)
#using numpy modules
img = np.zeros([512, 512, 3], np.uint8)


#draw a line
img = cv2.line(img, (0,0), (255, 255), (86, 25 ,255), 10)
img = cv2.arrowedLine(img, (0,255), (255, 255), (0, 255 ,255), 5) # BGR-> bule, green, red

# draw a rectangle
img = cv2.rectangle(img, (384,0), (510, 128), (0, 0, 255), 10)
# circle
img = cv2.circle(img, (447, 63), 63, (0, 255, 0), -1)
# put text
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'OpenCv', (10, 500), font, 4, (255, 255, 255), 10, lineType=cv2.LINE_AA)

print((img)) # matix

cv2.imshow('image', img)

k = cv2.waitKey(4000)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('q'):
    cv2.imwrite('lena_copy.png', img)
    cv2.destroyAllWindows()

print(img.view())