import numpy as np
import cv2
import copy
# Load an color image in grayscale
img = cv2.imread('C:\\video\pxp_BLUE.jpg')
flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
print flags
