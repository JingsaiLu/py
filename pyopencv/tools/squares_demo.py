#! usr/bin/python
#coding=utf-8

# import numpy as np
import cv2
import numpy as np
from matplotlib import pyplot as plt


def angle_cos(p0, p1, p2):
    d1, d2 = (p0-p1).astype('float'), (p2-p1).astype('float')
    return abs( np.dot(d1, d2) / np.sqrt( np.dot(d1, d1)*np.dot(d2, d2) ) )

def find_squares(img):
    img = cv2.GaussianBlur(img, (5, 5), 0)
    squares = []
    for gray in cv2.split(img):
        for thrs in xrange(0, 255, 26):
            if thrs == 0:
                bin = cv2.Canny(gray, 0, 50, apertureSize=5)
                bin = cv2.dilate(bin, None)
            else:
                retval, bin = cv2.threshold(gray, thrs, 255, cv2.THRESH_BINARY)
            contours, hierarchy = cv2.findContours(bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
            for cnt in contours:
                cnt_len = cv2.arcLength(cnt, True)
                cnt = cv2.approxPolyDP(cnt, 0.02*cnt_len, True)
                if len(cnt) == 4 and cv2.contourArea(cnt) > 1000 and cv2.isContourConvex(cnt):
                    cnt = cnt.reshape(-1, 2)
                    max_cos = np.max([angle_cos( cnt[i], cnt[(i+1) % 4], cnt[(i+2) % 4] ) for i in xrange(4)])
                    if max_cos < 0.1:
                        squares.append(cnt)
    return squares

def imshow_key(img):
        cv2.namedWindow('temp',cv2.WINDOW_NORMAL)        
        cv2.imshow('temp', img)
        ch = 0xFF & cv2.waitKey()
        if ch == 27:
            cv2.destroyAllWindows()
            exit()
        return ch

def caculate_area(squares):
    for square in squares:
        print square
        xysum = np.sum(square, 1)
        # print xysum.max()
        # xysum = np.array([100,2,3,4])
        maxp = np.where(xysum == xysum.max())
        minp = np.where(xysum == xysum.min())
        # print maxp, minp
        # print .max().index



if __name__ == '__main__':

    img = cv2.imread('../pxp_blue.jpg')
    img = cv2.GaussianBlur(img, (5, 5), 0)
    squares = []
    for gray in cv2.split(img):
        # imshow_key(gray)        
        for thrs in xrange(0, 255, 104):
            if thrs == 0:
                bin = cv2.Canny(gray, 0, 50, apertureSize=5)
                bin = cv2.dilate(bin, None)
            else:
                retval, bin = cv2.threshold(gray, thrs, 255, cv2.THRESH_BINARY)
            # imshow_key(bin)
            contours, hierarchy = cv2.findContours(bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
            # print contours
            for cnt in contours:
                cnt_len = cv2.arcLength(cnt, True)
                cnt = cv2.approxPolyDP(cnt, 0.02*cnt_len, True)
                if len(cnt) == 4 and cv2.contourArea(cnt) > 1000 and cv2.isContourConvex(cnt):
                    cnt = cnt.reshape(-1, 2)
                    max_cos = np.max([angle_cos( cnt[i], cnt[(i+1) % 4], cnt[(i+2) % 4] ) for i in xrange(4)])
                    if max_cos < 0.1:
                        squares.append(cnt)
    # squares = find_squares(img)

    caculate_area(squares)
    for i in xrange(len(squares)):
        print squares[i][0, 0]
        dis_iamge = img.copy()
        cv2.drawContours( dis_iamge, [squares[i]], -1, (0, 0, 255), 3 )
        cv2.namedWindow('squares',cv2.WINDOW_NORMAL)        
        cv2.imshow('squares', dis_iamge)

        # cv2.resizeWindow('squares', 600,600)
        # plt.subplot(121),plt.imshow(dis_iamge)
        # plt.title('Dis Image'), plt.xticks([]), plt.yticks([])
        # wm = plt.get_current_fig_manager()
        # wm.window.state('zoomed')
        # plt.show()
        ch = 0xFF & cv2.waitKey()
        if ch == 27:
            cv2.destroyAllWindows()
            break






    # from glob import glob
    # for fn in glob('../pxp*.jpg'):
    #     img = cv2.imread(fn)
    #     squares = find_squares(img)
    #     cv2.drawContours( img, squares, -1, (0, 255, 0), 3 )
    #     cv2.imshow('squares', img)
    #     ch = 0xFF & cv2.waitKey()
    #     if ch == 27:
    #         break
    # cv2.destroyAllWindows()
