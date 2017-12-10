#! usr/bin/python
#coding=utf-8

# import numpy as np
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load an color image in grayscale
img = cv2.imread('../pxp_blue.jpg', 0)
plt.subplot(2,3,1),plt.imshow(img,'gray')#默认彩色，另一种彩色bgr
kernel = np.ones((5,5),np.uint8)

# 腐蚀
erosion = cv2.erode(img,kernel,1)
plt.subplot(2,3,2),plt.imshow(erosion,'gray')

# 膨胀
dilate = cv2.dilate(img,kernel,1)
plt.subplot(2,3,3),plt.imshow(dilate,'gray')

# 开运算
morphOpen = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
plt.subplot(2,3,4),plt.imshow(morphOpen,'gray')#默认彩色，另一种彩色bgr

# 闭运算
morphClose = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
plt.subplot(2,3,5),plt.imshow(morphClose,'gray')#默认彩色，另一种彩色bgr

# 形态学梯度
gradiant = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
plt.subplot(2,3,6),plt.imshow(gradiant, 'gray')#默认彩色，另一种彩色bgr

# 礼帽
# tophat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
# 黑帽
# blackhat = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)
plt.show()