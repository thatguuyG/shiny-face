import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    #capture frame by frame
    ret, frame = cap.read()

    #display the resulting frame
    cv2.imshow('fame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

#release capture
cap.realease()
cv2.destroyAllWindows()