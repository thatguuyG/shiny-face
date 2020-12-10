import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap.set(3,640)#set width
cap.set(4,480)#set height

while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1) #flip the cam, it straightens it for mine
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',frame)
    #gray image
    cv2.imshow('gray', gray)

    k = cv2.waitKey(30) & 0xff
    if k == 27 : #press escape to quit
        break

cap.release()
cv2.destroyAllWindows()