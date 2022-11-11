import cv2
import sys
import numpy as np

#두개의 동영상 열기
v1 = cv2.VideoCapture('video1.mp4')
v2 = cv2.VideoCapture('video2.mp4')

if not v1.isOpened() or not v2.isOpened():
    print('video open failed!')
    sys.exit()
    
#두 동영상크기, pfs 같다고
frame_v1 = round(v1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_v2 = round(v2.get(cv2.CAP_PROP_FRAME_COUNT))
fps = v1.get(cv2.CAP_PROP_FPS)

#48프레임 첫번째 영상의 2초, 두번째 영상 2초 겹쳐서 효과 줌
effect_frames = int(fps*2)

print("frame_v1 : ", frame_v1)
print("frame_v2 : ", frame_v2)
print('FPS : ', fps)

#프레임간 시간 간격
delay = int(1000/fps)

w = round(v1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(v1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

#출력 동영상 객체 생성
out = cv2.VideoWriter('output.avi', fourcc,fps,(w,h))

#1번 동영상 복사
for i in range(frame_v1 - effect_frames):       #뒤에 2초 남겨두고 앞부분만 저장
    ret1, frame1 = v1.read()
    
    if not ret1:
        print("frame read error!")
        sys.exit()
        
    out.write(frame1)
    print(".", end="")
    
    cv2.imshow('output', frame1)
    cv2.waitKey(delay)
    
#1번 도영상 뒷부분과 2번 동영상 앞부분 합성
for i in range(effect_frames):      #48번
    ret1, fraem1 = v1.read()
    ret2, frame2 = v2.read()
    
    if not ret1 or not ret2:
        print("frame read error!")
        sys.exit()
    
    #합성, 짤라내기 위한 변수, w 넓이를 48로 나눔
    dx = int((w/effect_frames)*i)
    
    frame = np.zeros((h,w,3), dtype=np.uint8)       #프레임 하나 생성
    frame[:,0:dx,:] = frame2[:,0:dx,:]      #0부터 dx 까지는 영상2
    frame[:,dx:w,:] = frame1[:,dx:w,:]       #dx부터 끝까지 영상 1
    
    # alpha = i/effect_frames
    # frame = cv2.addWeighted(frame1,1,-alpha, frame2, alpha, 0)
    
    #프레임 저장
    out.write(frame)
    print(".", end="")
    
    cv2.imshow('output', frame)
    cv2.waitKey(delay)
    
#2번 동영상 복사
for i in range(effect_frames, frame_v2):
    ret2, frame2 = v2.read()
    
    if not ret2:
        print("frame read error!")
        sys.exit()
        
    out.write(frame2)
    print(".", end="")
    
    cv2.imshow('output', frame2)
    cv2.waitKey(delay)    

print("|noutput.avi file is successfully generated!")

v1.release()
v2.release()
out.release()
cv2.destroyAllWindows()
