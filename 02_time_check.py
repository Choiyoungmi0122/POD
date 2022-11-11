import cv2
import sys

img = cv2.imread('hongkong.jpg')

tm=cv2.TickMeter()
tm.start()

edge = cv2.Canny(img, 50, 150)

tm.stop()

print('Elapsed time: {}ms.'.format(tm.getTimeMilli()))