
import cv2
import mediapipe as mp
import time

import handtrackingmodul


pTime = 0
cTime = 0
cap = cv2.VideoCapture(1)
detector = handtrackingmodul.handDetection()

while True:
    success, img = cap.read()
    img = detector.findHand(img)
    lmList = detector.findPostion(img)
    if len(lmList) != 0:
        print(lmList[4])

    # show fps
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 255), 3)

    cv2.imshow('Image', img)
    cv2.waitKey(1)
