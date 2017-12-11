#! usr/bin/python
#coding=utf-8

# import numpy as np
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('c:/video/pxp_blue.jpg',0)
f = np.fft.fft2(img)
fshift = np.fft.fftshift(f)
magnitude_spectrum = 20*np.log(np.abs(fshift))
print magnitude_spectrum.dtype

plt.subplot(121),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(magnitude_spectrum, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.show()