import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here 
    GRAY = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    SEPIA = cv2.cvtColor(frame, cv2.CALIB_CB_ASYMMETRIC_GRID)
    RANDOM = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS_FULL)

    # Display the resulting frame
    cv2.imshow('Normal Frame', frame)
    cv2.imshow('Sepia', SEPIA)
    cv2.imshow('Random', RANDOM)
    cv2.imshow('gray', GRAY)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()

cv2.destroyAllWindows()
