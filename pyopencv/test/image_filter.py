#! usr/bin/python
#coding=utf-8

# import numpy as np
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load an color image in grayscale
img = cv2.imread('../pxp_blue.jpg', 0)
# 添加点噪声
for i in range(2000): #添加点噪声
    temp_x = np.random.randint(0,img.shape[0])
    temp_y = np.random.randint(0,img.shape[1])
    img[temp_x][temp_y] = 255
plt.subplot(2,3,1),plt.imshow(img,'gray')#默认彩色，另一种彩色bgr


imgf = np.float32(img) #转化数值类型
kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(imgf,-1,kernel)
#cv2.filter2D(src,dst,kernel,auchor=(-1,-1))函数：
#输出图像与输入图像大小相同
#中间的数为-1，输出数值格式的相同plt.figure()
plt.subplot(2,3,2),plt.imshow(dst,'gray')

# 均值滤波
blur = cv2.blur(img,(3,5))#模板大小3*5
plt.subplot(2,3,3),plt.imshow(blur,'gray')

# 高斯模糊模板
gauss = cv2.GaussianBlur(img,(5,5),0)
plt.subplot(2,3,4),plt.imshow(gauss,'gray')#默认彩色，另一种彩色bgr

# 中值滤波模板
median = cv2.medianBlur(img,5)
plt.subplot(2,3,5),plt.imshow(median,'gray')#默认彩色，另一种彩色bgr


#9---滤波领域直径
#后面两个数字：空间高斯函数标准差，灰度值相似性标准差
bila = cv2.bilateralFilter(img,9,75,75)
plt.subplot(2,3,6),plt.imshow(bila,'gray')#默认彩色，另一种彩色bgr

plt.show()