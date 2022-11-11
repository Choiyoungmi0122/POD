import cv2
import numpy as np

img = np.full((400,400,3), 255, np.uint8)

cv2.line(img,(50,50), (200,50),(0,0,255),5) #일직선으로 가는 굵은 선으로 빨간샥
cv2.line(img,(50,60), (150,160), (0,0,128))     #45도 회전한 직선으로 앞의 선보다 얇음

cv2.rectangle(img,(50,200,150,100),(0,255,0),2)     #굵기가 2인 사각형으로 초록색
cv2.rectangle(img,(70,220),(180,280),(0,128,0),-1)      #선굵기 -1이면 가득 채우기이며 사각형임

cv2.circle(img, (300,100),30,(255,255,0),-1,cv2.LINE_AA)        #작은 원으로 안을 가득채운
cv2.circle(img, (300,100),60,(255,0,0),3,cv2.LINE_AA)           #더 큰원

pts = np.array([[250,200],[300,200],[350,300],[250,300]])      #배열을 이용해 좌표찍음([왼쪽위],[오른쪽 위]..)순으로 적으며 하나 삭제하면 그에 맞게 도형의 모습 자체가 바뀜
# cv2.polylines(img,[pts],True,(255,0,255),2)


text = 'Hello? OpenCv ' + cv2.__version__
cv2.putText(img,text,(50,350), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,225),1,cv2.LINE_AA)

cv2.imshow("img", img)

cv2.waitKey()
cv2.destroyAllWindows()
