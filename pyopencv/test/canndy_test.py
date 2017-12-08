import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('c:\\video\pxp_rgb.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
# h, s, v = cv2.split(yuv)

LowerBlue = np.array([100, 100, 50])
UpperBlue = np.array([130, 255, 255])
mask = cv2.inRange(hsv, LowerBlue, UpperBlue)
blueThings = cv2.bitwise_and(img, img, mask=mask)
print blueThings
rgb = cv2.cvtColor(blueThings, cv2.COLOR_HSV2BGR)

edges = cv2.Canny(rgb,100,200)
plt.subplot(151),plt.imshow(img)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(152),plt.imshow(hsv,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.subplot(153),plt.imshow(blueThings,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(154),plt.imshow(rgb,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(154),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
plt.show()