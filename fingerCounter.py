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

ptime = 0

while True:

    success, img = cap.read()

    img = detector.findHands(img)
    lmList = detector.findPosition(img)

    if len(lmList) != 0:
        finger_num = 0
        if(lmList[4][1] > lmList[4][2]):
            finger_num += 1

        for fingerindex in range(1, 5):
            if lmList[fingers[fingerindex]][2] < lmList[fingers[fingerindex] - 2][2]:
                finger_num += 1

        print(finger_num)

    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    cv.putText(img, str(int(fps)), (20, 50), cv.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)



    cv.imshow('video', img)
    cv.waitKey(1)
