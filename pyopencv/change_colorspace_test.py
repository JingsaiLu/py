import numpy as np
import cv2
import copy
# Load an color image in grayscale
img = cv2.imread('C:\\video\pxp_BLUE.jpg')
flags = [i for i in dir(cv2) if i.startswith('COLOR_BGR2')]
print flags
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

LowerBlue = np.array([100, 100, 50])
UpperBlue = np.array([130, 255, 255])
mask = cv2.inRange(hsv, LowerBlue, UpperBlue)
BlueThings = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('image',BlueThings)
cv2.waitKey(0)
cv2.destroyAllWindows()
# cv2.imwrite('pxp_rgb_result.jpg', BlueThings)

