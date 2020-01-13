import numpy as np
import cv2

while(True):

    capture  = cv2.VideoCapture('video.np4')

    ret, frame = capture.read()
    cv2.imshow('Show Frame', frame);

    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()