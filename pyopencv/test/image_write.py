# import numpy as np
import cv2

# Load an color image in grayscale
img = cv2.imread('../nxp-logo.png',0)

cv2.imwrite('cv2_gen.png',img)