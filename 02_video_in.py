import sys
import cv2

cap = cv2.VideoCapture('video1.mp4')

fps = round(cap.get(cv2.CAP_PROP_FPS))
deleay = round(1000/fps)

while True:
    ret, frame = cap.read()
    
    # inversed = ~frame 
    
    cv2.imshow('frame', frame)
    # cv2.imshow('inversed', inversed)
    
    if cv2.waitKey(deleay) == 27:
        break
    
cap.release()
cv2.destroyAllWindows()