#! usr/bin/python
#coding=utf-8

# import numpy as np
import cv2
import numpy as np
from matplotlib import pyplot as plt

grayImage = np.zeros((512,512),np.uint8)#生成一个空灰度图像
cv2.line(grayImage,(0,0),(511,511),255,5)
plt.subplot(121),plt.imshow(grayImage,'gray')
plt.title("gray image"), plt.xticks([]), plt.yticks([])

colorImage = np.zeros((512,512,3), np.uint8)
# image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.rectangle(colorImage,(20,20),(411,411),(55,255,155),5)
cv2.circle(colorImage,(200,200),50,(55,255,155),1)#修改最后一个参数
cv2.circle(colorImage,(300,300),50,(55,255,155),8)#修改最后一个参数
cv2.ellipse(colorImage,(156,56),(150,100),0,0,180,250,-1)
#注意最后一个参数-1，表示对图像进行填充，默认是不填充的，如果去掉，只有椭圆轮廓了
plt.subplot(122),plt.imshow(colorImage, 'brg')
plt.title("Color image"), plt.xticks([]), plt.yticks([])
plt.show()