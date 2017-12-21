#! usr/bin/python
#coding=utf-8


'''
Simply display the contents of the webcam with optional mirroring using OpenCV 
via the new Pythonic cv2 interface.  Press <esc> to quit.
'''

import cv2

def show_cam(mirror=False):
    cam = cv2.VideoCapture(0)
    while True:
        ret_val, img = cam.read()
        if mirror: 
            img = cv2.flip(img, 1)
        cv2.imshow('my webcam', img)
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    cam.release()
    cv2.destroyAllWindows()

def exit_with_esc():
    pass

def show_cam_with_save():
    videoCapture = cv2.VideoCapture(0)
    #获得码率及尺寸  
    fps = videoCapture.get(cv2.cv.CV_CAP_PROP_FPS)  
    print fps
    size = (int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),   
            int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))) 
    #指定写视频的格式, I420-avi, MJPG-mp4  
    videoWriter = cv2.VideoWriter('video_demo.avi', cv2.cv.CV_FOURCC('M', 'J', 'P', 'G'), 10, size)  
      
    #读帧  
    success, frame = videoCapture.read()  
      
    while success :  
        cv2.imshow("Video demo", frame) #显示   
        videoWriter.write(frame) #写视频帧  
        success, frame = videoCapture.read() #获取下一帧  
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    # videoWriter.close()
    videoCapture.release()
    cv2.destroyAllWindows()

def main():
    # show_cam(mirror=True)
    show_cam_with_save()

if __name__ == '__main__':
    main()