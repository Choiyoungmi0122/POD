import cv2
import numpy as np

img1 = np.empty((480, 640), dtype = np.uint8)   #gratscale image
img2 = np.zeros((480, 640, 3), dtype=np.uint8)  #color image
img3 = np.ones((480, 640), dtype=np.uint8) * 255    #white
img4 = np.full((480, 640, 3), (0, 255,255), dtype=np.uint8)  #yellow

#이상태로 run하면 당연히 안돼지...
#imshow해서 나오게 해야함
#cv2.imshow('img1', img1)        #왜 회색이 아닌 검은화면이 뜰까...?
#cv2.imshow('img2', img2)
#cv2.imshow('img3', img3)
#cv2.imshow('img4', img4)
# cv2.waitKey()
# cv2.destroyAllWindows()

#영상복사
img1 = cv2.imread('HappyFish.jpg')

img2 = img1[40:120, 30:150]  #numpy.ndarrat 의 슬라이싱 
img3 = img1[40:120, 30:150].copy()

img2.fill(0)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)

cv2.waitKey()
cv2.destroyAllWindows()