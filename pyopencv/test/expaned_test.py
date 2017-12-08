# import numpy as np
import cv2
import copy
# Load an color image in grayscale
img = cv2.imread('C:\\video\pxp_blue.jpg')
img[10,10] =[0,0,0]
ball = img[0:70,0:80]
img[0:70,80:160] = ball
# ball = img[0:70, 0:80]
# cv2.imshow('ball', ball)

# img[73:180,0:70] = ball
# cv2.imshow('image', img)
# print img.shape
# print img.dtype
# img[10,10] = (255, 255, 255)
# cv2.imwrite('pixel_255.png',img)
# print img
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
# cv2.imwrite('cv2_gen.png',img)