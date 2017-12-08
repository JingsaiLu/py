import cv2
import numpy as np
from matplotlib import pyplot as plt

img_bgr = cv2.imread('c:\\video\pxp_blue.jpg')
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2HSV)
r, g, b = cv2.split(img_rgb)
h, s, v = cv2.split(img_hsv)
h = cv2.Canny(img_gray, 100, 200)

# cv2.adaptiveThreshold(img_gray,img_gray,100)
ret, mask = cv2.threshold(img_gray, 10, 255, cv2.THRESH_BINARY)
print mask
plt.subplot(131),plt.imshow(img_rgb)
plt.subplot(132),plt.imshow(img_gray)
plt.subplot(133),plt.imshow(mask)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
# h, s, v = cv2.split(yuv)

# LowerBlue = np.array([100, 100, 50])
# UpperBlue = np.array([130, 255, 255])
# mask = cv2.inRange(hsv, LowerBlue, UpperBlue)
# blueThings = cv2.bitwise_and(img, img, mask=mask)
# print blueThings
# rgb = cv2.cvtColor(blueThings, cv2.COLOR_HSV2BGR)

# edges = cv2.Canny(rgb,100,200)
# plt.subplot(151),plt.imshow(img)
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(152),plt.imshow(hsv,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(153),plt.imshow(blueThings,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(154),plt.imshow(rgb,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
# # plt.subplot(154),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
wm = plt.get_current_fig_manager()
wm.window.state('zoomed')
plt.show()