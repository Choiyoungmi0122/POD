import cv2
import sys

img1 = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('cat.bmp', cv2.IMREAD_COLOR)

print('type(img1): ', type(img1))   #type(img1) : <class 'numpy.ndarray'>
print('img1.shape: ', img1.shape)   #img1.shape : (480, 640)
print('img2.shape: ', img2.shape)   #img2.shape : (480, 640, 3)
print('img2.dtype: ', img2.dtype)   #img2.dtype : uint8

h, w = img2.shape[:2]  #h: 480, w: 640
print('img2 size: {}  {}'.format(w, h))

if len(img1.shape)  == 2:
    print('img1 is a grayscale image')
elif len(img1.shape) == 3:
    print('img1 is a truecolor image')  

for y in range(h):      #for문으로 픽셀값 변경하는 작업은 매우 느리므로, 
    for x in range(w):     #픽셀 값 참조 방법만 확인하고 실제로는사용금지
        img1[y,x] = 255
        img2[y,x] = [0,0,255]
        #img1[:,:] = 255
        #img2[:,:] = (0,0,255)