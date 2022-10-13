import os
import glob
import cv2
import sys

# file_list = os.listdir('.\\images')
# img_files = [os.path.join('.\\images', file)
#              for file in file_list if file.endswith('.jpg')]

#glob.glob() 사용방법
img_files=glob.glob('./images/*.jpg')       #\\이렇게 하면 경로를 찾지 못함 -> /주의

if not img_files:       #img_files 아예 존재하지 않다면 출력 후 바로 sys종료
    print("There are no jpg files in 'images' folder")
    sys.exit()
    
    
#전체화면으로 'image'창 생성    
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('image', cv2.WND_PROP_FULLSCREEN,
                    cv2.WINDOW_FULLSCREEN )


#무한루프
cnt=len(img_files)
idx=0

while True:
    img=cv2.imread(img_files[idx])
    
    if img is None:
        print("Image load failed!")
        break
    
    #창크기가 맘에 들지 않아 변경 시도
    #cv2.moveWindow(img,40,30)    ->   TypeError: Can't convert object to 'str' for 'winname'
    cv2.imshow('image', img)
    if cv2.waitKey(1000)>=0:
        break
    
    idx+=1
    if idx>=cnt:
        idx=0