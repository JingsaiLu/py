import cv2
import numpy as np
from matplotlib import pyplot as plt

filename = 'c:\\video\\pxp_blue.jpg'
img = cv2.imread(filename)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

rows,cols = img.shape[0:2]

M = cv2.getRotationMatrix2D((cols/2,rows/2),-90,1)
print M
dst = cv2.warpAffine(img,M,(cols,rows))

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(121),plt.imshow(dst,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.show()