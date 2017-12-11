#! usr/bin/python
#coding=utf-8

# import numpy as np
import cv2
import numpy as np
from matplotlib import pyplot as plt

colorImage = cv2.imread('c:/video/pxp_RGB.jpg')
img = cv2.cvtColor(colorImage, cv2.COLOR_BGR2GRAY)#灰度图像 
colorImage = cv2.cvtColor(colorImage, cv2.COLOR_BGR2RGB)#灰度图像 
img = cv2.blur(img,(3,5))#模板大小3*5
# img = cv2.GaussianBlur(img, (3,3), 0)  

img=cv2.equalizeHist(img)  
img_float32 = np.float32(img)

dft = cv2.dft(img_float32, flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

rows, cols = img.shape
crow, ccol = rows/2 , cols/2     # center

# create a mask first, center square is 1, remaining all zeros
mask = np.ones((rows, cols, 2), np.uint8)
squareArea = 50
mask[crow-squareArea:crow+squareArea, ccol-squareArea:ccol+squareArea] = 0

# apply mask and inverse DFT
fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)

img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])
# img_back = cv2.convertScaleAbs(img_back)   # 转回uint8
img_back = img_back / (img_back.max() - img_back.min()) * 255
# img_back.dtype = np.uint8
img_back = img_back.astype('uint8')

# img_back = cv2.blur(img_back,(3,5))#模板大小3*5
kernelSize = 3
kernel = np.ones((kernelSize,kernelSize),np.uint8)

# # sobel x
# sobelx = cv2.Sobel(img_back,cv2.CV_64F,1,0,ksize=3)#默认ksize=3
# sobelx = cv2.convertScaleAbs(sobelx)   # 转回uint8 
# # sobel y
# sobely = cv2.Sobel(img_back,cv2.CV_64F,0,1,ksize=3)
# sobely = cv2.convertScaleAbs(sobely)   # 转回uint8 
# img_back = cv2.bitwise_or(sobelx,sobely)



# img_back = cv2.erode(img_back,kernel,1)

# img_back = cv2.dilate(img_back,kernel,1)
# img_back = cv2.morphologyEx(img_back,cv2.MORPH_CLOSE,kernel)
# img_back = cv2.equalizeHist(img_back)  

#hough transform
# img_back = cv2.cvtColor(img_back, cv2.COLOR_GRAY2BGR)
# img_back = cv2.equalizeHist(img_back)  
# img_back = cv2.erode(img_back,kernel,1)
img_back = cv2.Canny(img_back,10,200)#其他的默认
img_back = cv2.morphologyEx(img_back,cv2.MORPH_CLOSE,kernel)
# img_back = cv2.blur(img_back,(3,5))#模板大小3*5
# img_back = cv2.dilate(img_back,kernel,1)
# img_back = cv2.erode(img_back,kernel,1)



# lines = cv2.HoughLines(img_back,1,np.pi/180,200)
# print lines
# for rho,theta in lines[0]:

#     a = np.cos(theta)
#     b = np.sin(theta)
#     x0 = a*rho
#     y0 = b*rho
#     x1 = int(x0 + 1000*(-b))
#     y1 = int(y0 + 1000*(a))
#     x2 = int(x0 - 1000*(-b))
#     y2 = int(y0 - 1000*(a))

#     cv2.line(img_back,(x1,y1),(x2,y2),(0,0,255),2)
# cv2.line(img_back,(0,0),(1000,1000),(255,0,255),5)
kernelSize = 3
kernel = np.ones((kernelSize,kernelSize),np.float32)/25
img_back = cv2.filter2D(img_back,-1,kernel)
img_back = cv2.medianBlur(img_back,5)
img_back = cv2.blur(img_back,(3,5))#模板大小3*5



# cv2.FindContours(image, storage, mode=CV_RETR_LIST, method=CV_CHAIN_APPROX_SIMPLE, offset=(0, 0)) → contours

lines = cv2.HoughLinesP(img_back,1,np.pi/180, 80, minLineLength=200,maxLineGap=15)
# lines = cv2.HoughLinesP(img_back, rho = 1,theta = 1*np.pi/180,threshold = 100,minLineLength = 100,maxLineGap = 50)

lines1 = lines[0]#提取为二维
print lines1
for x1,y1,x2,y2 in lines1[:]: 
    cv2.line(colorImage, (x1,y1),(x2,y2), (255,0,125), 1)

plt.subplot(121),plt.imshow(colorImage, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(img_back, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
wm = plt.get_current_fig_manager()
wm.window.state('zoomed')
plt.show()