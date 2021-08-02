import cv2 as cv
import numpy as np
import time
import handTrackingModule as htm

wcam, hcam = 640, 480

cap = cv.VideoCapture(0)
cap.set(3, wcam)
cap.set(4, hcam)

detector = htm.handDetector()

ptime = 0
fingers = [4, 8, 12, 16, 20]

finger_num = 0

while True:
    success, img = cap.read()

    img = detector.findHands(img)
    lmList = detector.findPosition(img)

    if len(lmList) != 0:
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[0][1], lmList[0][2]

        xdif, ydif = x1-x2, y1-y2
        #print(xdif, ydif)
        if(xdif > 110):
            print("hand open")
        else:
            print("hand closed")



    cv.imshow('video', img)
    cv.waitKey(1)
