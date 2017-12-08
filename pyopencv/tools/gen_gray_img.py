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
    cv2.imwrite('_'.join(['gray', imgNmae]), grayImg)
   

if __name__ == '__main__':
    main()