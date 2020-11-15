# coding=UTF-8
import cv2

def facealarm():
    capture = cv2.VideoCapture = cv2.VideoCapture ( 0 )#注意相机的编号
    face_detector = cv2.CascadeClassifier ("haarcascade_frontalface_alt.xml" )

    i = 0
    while True:
        ret, img = capture.read ()
        img = cv2.flip ( img, 1 )
        gray = cv2.cvtColor ( img, cv2.COLOR_BGR2GRAY )
        faces = face_detector.detectMultiScale ( gray, 1.1, 2 )#人脸识别
        if (len(faces)>0):
            i=i+1
        if(i>1):
            break
    capture.release()
    cv2.destroyAllWindows()
if(__name__=='__main__'):
    facealarm ()