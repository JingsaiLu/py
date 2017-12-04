# import numpy as np
import cv2
import copy
# Load an color image in grayscale
cv_logo = cv2.imread('opencv_logo.jpg')
print cv_logo.shape
nxp_logo = cv2.imread('nxp-logo.jpg')
nxp_logo = cv2.resize(nxp_logo, (500,463),interpolation=cv2.INTER_AREA)
# nxp_logo.resize(463,500,3,interpolation=cv2.INTER_AREA)
print nxp_logo.shape
dest = cv2.addWeighted(nxp_logo,0.3,cv_logo,0.7,0)
cv2.imshow('image',dest)
cv2.waitKey(0)
cv2.destroyAllWindows()
