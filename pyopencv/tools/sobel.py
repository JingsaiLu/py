import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse

imgDir = 'c://video'
retDir = './'
imgNmae = 'pxp_blue.jpg'

def parse_args():
    parser = argparse.ArgumentParser(description='Generate gray image.')
    parser.add_argument('--i', type=str, default = "/".join([imgDir,imgNmae]), help = 'image file path')
    args = parser.parse_args()
    return vars(args)    


def main():
    args = parse_args()
    grayImg = cv2.imread(args['i'], 0)
    sobelImg = cv2.Sobel(grayImg,ddepth=cv2.cv.CV_8U,dx=0,dy=1,ksize = 1)
    sobelImg = cv2.Sobel(grayImg,ddepth=cv2.cv.CV_8U,dx=1,dy=0,ksize = 1)

    # edges = cv2.Canny(grayImg,100,200)
    plt.subplot(131),plt.imshow(grayImg)
    plt.subplot(132),plt.imshow(grayImg)
    plt.subplot(133),plt.imshow(sobelImg)

    cv2.imwrite('sobel.jpg', sobelImg)
    wm = plt.get_current_fig_manager()
    wm.window.state('zoomed')
    plt.show()

if __name__ == '__main__':
    main()