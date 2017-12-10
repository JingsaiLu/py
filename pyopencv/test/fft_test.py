#! usr/bin/python
#coding=utf-8

import numpy as np
import cv2
import copy

from matplotlib import pyplot as plt
 
img = cv2.imread('C:\\video\pxp_BLUE.jpg')  
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
f = np.fft.fft2(h) # 快速傅里叶变换算法得到频率分布  
fshift = np.fft.fftshift(f) # 默认结果中心点位置是在左上角，转移到中间位置
 
fimg = np.log(np.abs(fshift)) # fft 结果是复数，求绝对值结果才是振幅
print fimg
 
# 展示结果
plt.subplot(121), plt.imshow(img, 'gray'), plt.title('Original Fourier')  
plt.subplot(122), plt.imshow(fimg, 'gray'), plt.title('Fourier Fourier')  
plt.show()