import sys
import cv2

cap = cv2.VideoCapture(0)       #기본 카메라 장치 열기


#카메라 프레임 크기 출력
print("Frame width:",
      int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print("Frame heigth: ",
      int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    # inversed = ~frame #흑백으로 
    
    
    cv2.imshow('frame', frame) 
    # cv2.imshow('inversed', inversed)        #흑백버전
    
    if cv2.waitKey(10) ==27:
        break
    
cap.release()
cv2.destroyAllWindows()

