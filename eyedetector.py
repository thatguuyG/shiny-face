import numpy as np
import cv2

faceCascade = cv2.CascadeClassifier('cascades/data/haarcascade_eye.xml')
cap = cv2.VideoCapture(0)
cap.set(3,640) #set width
cap.set(4,480) #set height

while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces =faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.6,
        minNeighbors=5,
        minSize=(20,20)
    )

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
    cv2.imshow('video', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press esc to quit
        break

cap.release()
cv2.destroyAllWindows()