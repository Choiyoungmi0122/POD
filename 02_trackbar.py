import cv2
import numpy as np
import sys

#뭔가 안된다. 위에 트랙바를 클릭하면 창이 꺼지고 다른 값으 넣어봐도 검은 색밖에 뜨질 않는데 무슨일..?

def on_level_change(pos):
    value = pos*16
    if value >=255:
        value = 255
        
    img[:] = value
    cv2.imshow('image', img)
    
    
img = np.zeros((480, 640), np.uint8)

cv2.namedWindow('image')
cv2.createTrackbar('level', 'image', 0,16,on_level_change)

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()