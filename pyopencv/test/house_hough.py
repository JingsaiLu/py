#! usr/bin/python
#coding=utf-8


import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../house.jpg') 
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#灰度图像 
#open to see how to use: cv2.Canny
#http://blog.csdn.net/on2way/article/details/46851451 
edges = cv2.Canny(gray,50,200)
plt.subplot(121),plt.imshow(edges,'gray')
plt.xticks([]),plt.yticks([])
#hough transform
lines = cv2.HoughLinesP(edges,1,np.pi/180,30,minLineLength=60,maxLineGap=10)
lines1 = lines[:,0,:]#提取为二维
for x1,y1,x2,y2 in lines1[:]: 
    cv2.line(img,(x1,y1),(x2,y2),(255,0,0),1)

plt.subplot(122),plt.imshow(img,)
plt.xticks([]),plt.yticks([])

plt.show()