import cv2
import time
cap = cv2.VideoCapture(0)
while(1):
    start = time.time()
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('img001.jpg', gray)
    end = time.time()
    time.sleep(1)
    print(1 / (end - start))
