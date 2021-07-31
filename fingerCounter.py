import cv2 as cv
import numpy as np
import time
import handTrackingModule as htm

wcam, hcam = 640, 480

cap = cv.VVideoCapture(0)
cap.set(3, wcam)
cap.set(4, hcam)

detector = htm.handDetector()

ptime = 0

while True:
    success, img = cap.read()

    img = detector.findHands(img)
    lmList = detector.findPosition(img)
