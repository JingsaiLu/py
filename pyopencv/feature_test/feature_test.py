#! usr/bin/python
#coding=utf-8


import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../pxp_rgb.jpg') 
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#灰度图像 
plt.subplot(121),plt.imshow(gray,'gray')

# GoodFeaturesToTrack() is better to void conner connection

# connners = cv2.cornerHarris(gray,3, 3, 0.04)  
# print connners

# thresh = 0.00001
# • cv2.THRESH_BINARY（黑白二值） 
# • cv2.THRESH_BINARY_INV（黑白二值反转） 
# • cv2.THRESH_TRUNC （得到的图像为多像素值） 
# • cv2.THRESH_TOZERO 
# • cv2.THRESH_TOZERO_INV 

# # find contours in the thresholded image
# cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
#     cv2.CHAIN_APPROX_SIMPLE)
# cnts = cnts[0]

ret, thresImage = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV) 
print thresImage
plt.subplot(122),plt.imshow(thresImage, 'gray')
plt.xticks([]),plt.yticks([])

wm = plt.get_current_fig_manager()
wm.window.state('zoomed')
plt.show()
