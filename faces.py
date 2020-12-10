import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)

while(True):
    #capture frame by frame
    ret, frame = cap.read()

    #display the resulting frame
    cv2.imshow('fame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

#release capture
cap.release()
cv2.destroyAllWindows()