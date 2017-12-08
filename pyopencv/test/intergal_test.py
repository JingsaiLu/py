import cv2
import numpy as np
filename = 'c:\\video\\pxp_blue.jpg'
im = cv2.imread(filename)
h,w = im.shape[:2]
# flood fill example
diff = (6,6,6)
mask = np.zeros((h+2,w+2),np.uint8)
cv2.floodFill(im,mask,(10,10), (255,255,0),diff,diff)
# show the result in an OpenCV window
cv2.imshow('im',im)
cv2.waitKey()
