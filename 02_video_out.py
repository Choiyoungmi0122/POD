import cv2
import sys

cap = cv2.VideoCapture(0)

w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.mp4', fourcc, 20, (w,h))      #원래 avi였는데 안열려서 mp4 로 변경하였지만 그래도 안열림 차후 문제 해결 요망

while True:
    ret, frame = cap.read()
    
    # inversed = ~frame
    # out.write(inversed)
    
    cv2.imshow('frame', frame)
    # cv2.imshow('inversed', inversed)
    if cv2.waitKey(10) == 27:
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()