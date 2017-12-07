import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('c:\\video\pxp_blue.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# h, s, v = cv2.split(yuv)

LowerBlue = np.array([100, 100, 50])
UpperBlue = np.array([130, 255, 255])
mask = cv2.inRange(hsv, LowerBlue, UpperBlue)
blueThings = cv2.bitwise_and(img, img, mask=mask)

edges = cv2.Canny(blueThings,100,200)
plt.subplot(121),plt.imshow(blueThings,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()