#! usr/bin/python
#coding=utf-8

# import numpy as np
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load an color image in grayscale
img = cv2.imread('../pxp_blue.jpg', 0)
plt.subplot(2,2,1),plt.imshow(img,'gray')#默认彩色，另一种彩色bgr

# sobel x
pyDown = cv2.pyrDown(img)
plt.subplot(2,2,2),plt.imshow(pyDown,'gray')

# sobel y
img1 = cv2.pyrDown(img)
img2 = cv2.pyrUp(img1)
plt.subplot(2,2,3),plt.imshow(img2,'gray')

# sobel x and y.
img1 = cv2.pyrDown(img)#高斯金字塔
temp_img1 = cv2.pyrDown(img1)
temp = cv2.pyrUp(temp_img1)
img2 = img1 - temp #拉普拉斯金字塔
plt.subplot(2,2,4),plt.imshow(img2,'gray')#默认彩色，另一种彩色bgr

plt.show()