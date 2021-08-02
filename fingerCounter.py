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
base_point = 0

while True:

    finger_num = 0
    success, img = cap.read()

    img = detector.findHands(img)
    lmList = detector.findPosition(img)

    if len(lmList) != 0:
        basex, basey = lmList[base_point][1], lmList[base_point][2]

        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        x3, y3 = lmList[12][1], lmList[12][2]
        x4, y4 = lmList[16][1], lmList[16][2]
        x5, y5 = lmList[20][1], lmList[20][2]


        xdif1 = x2 - basex
        xdif2 = x3 - basex
        xdif3 = x4 - basex
        xdif4 = x5 - basex
        xdift = x1 - basex

        #print("xdif1 = ", xdif1, ", xdif2 = ", xdif2, ", xdif3 = ", xdif3, ", xdif4 = ", xdif4, ", xdif thumb = ", xdift)

        if(xdif1 > 60):
            finger_num += 1
        if(xdif2 > 10):
            finger_num += 1
        if(xdif3 > -40):
            finger_num += 1
        if(xdif4 > -85):
            finger_num += 1
        if(xdift > 100):
            finger_num += 1

        print(finger_num)





    cv.imshow('video', img)
    cv.waitKey(1)
