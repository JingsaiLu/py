#! usr/bin/python
#coding=utf-8


import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('c:/video/pxp_blue.jpg',0)

# img_float32 = np.float32(img)
# dft = cv2.dft(img_float32, flags = cv2.DFT_COMPLEX_OUTPUT)

fftret = np.fft.fft2(img) # 快速傅里叶变换算法得到频率分布  
fftsret = np.fft.fftshift(fftret)
fftImage = np.log(np.abs(fftsret)) # fft 结果是复数，求绝对值结果才是振幅

rows, cols = img.shape
crow, ccol = rows/2 , cols/2     # center

# create a mask first, center square is 1, remaining all zeros
mask = np.ones((rows, cols), np.uint8)
squareArea = 30
mask[crow-squareArea:crow+squareArea, ccol-squareArea:ccol+squareArea] = 0

# apply mask and inverse DFT
fftsretMask = fftsret*mask
fftisret = np.fft.ifftshift(fftsretMask)
fftiret = np.fft.ifft2(fftisret)
print fftiret
# img_back = cv2.idft(f_ishift)
# img_back = cv2.magnitude(img_back)

# img_back = np(img_back)

# img_back = cv2.cvtColor(img_back, cv2.COLOR_BGR2HSV)
print fftiret.dtype
img_back = np.log(np.abs(fftiret))
img_back = np.uint8(img_back)
cv2.imwrite('fft_hpf.png',img_back)
# cv2.cv.SaveImage('fft_hpf.jpg',cv2.cv.fromarray(img_back))

plt.subplot(131),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(132),plt.imshow(img_back, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])

plt.show()    