#! usr/bin/python
#coding=utf-8

# import numpy as np
import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load an color image in grayscale
img = cv2.imread('../pxp_blue.jpg', 0)
plt.subplot(121),plt.imshow(img,'gray')

edges = cv2.Canny(img,100,200)#其他的默认
plt.subplot(122),plt.imshow(edges,'gray')

plt.show()