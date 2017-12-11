#! usr/bin/python
#coding=utf-8

# import numpy as np
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load an color image in grayscale
img = cv2.imread('../pxp_blue.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
plt.subplot(2,3,1),plt.imshow(img,'gray')#默认彩色，另一种彩色bgr

# sobel x
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)#默认ksize=3
sobelx = cv2.convertScaleAbs(sobelx)   # 转回uint8 
plt.subplot(2,3,2),plt.imshow(sobelx,'gray')

# sobel y
sobely = cv2.Sobel(img,cv2.CV_64F,0,1)
sobely = cv2.convertScaleAbs(sobely)   # 转回uint8 
plt.subplot(2,3,3),plt.imshow(sobely,'gray')

# sobel x and y.
sobelxy = cv2.Sobel(img,cv2.CV_64F,1,1,ksize=3)
sobelxy = cv2.convertScaleAbs(sobelxy)   # 转回uint8 
plt.subplot(2,3,4),plt.imshow(sobelxy,'gray')#默认彩色，另一种彩色bgr

# laplace
laplacian = cv2.Laplacian(img,cv2.CV_64F)#默认ksize=3
laplacian = cv2.convertScaleAbs(laplacian)   # 转回uint8 
plt.subplot(2,3,5),plt.imshow(laplacian,'gray')#默认彩色，另一种彩色bgr

#人工生成一个高斯核，去和函数生成的比较
kernel = np.array([[0,-1,0],[-1,4,-1],[0,-1,0]],np.float32)#
img1 = np.float64(img)#转化为浮点型的
img_filter = cv2.filter2D(img1,-1,kernel)
sobelxy1 = cv2.Sobel(img1,-1,1,1)
sobelxy1 = cv2.convertScaleAbs(sobelxy1)   # 转回uint8 
plt.subplot(2,3,6),plt.imshow(sobelxy1, 'gray')#默认彩色，另一种彩色bgr

# 礼帽
# tophat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
# 黑帽
# blackhat = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)
wm = plt.get_current_fig_manager()
wm.window.state('zoomed')
plt.show()