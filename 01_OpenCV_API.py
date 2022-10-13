import matplotlib.pyplot as plt
import cv2

#컬러영상출력
imgBGR = cv2.imread('cat.bmp')      #이미지입력                      #BGR사실 얘가 기준...
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)        #RGBdefault 

#COLOR_BGR2RGB 하는 이유는 opencv.imread() BGR로 읽으면 원본인 RTGB와 다른색으로  불러와지기 때문에 다시 변환을 시켜줌

plt.axis('off')             #픽셀의 눈금 없애기
#axis는 nump행렬계산시 유용  , sum과 axis = 0 이면 2차원 행렬이 있을때, (5,3)행렬에서 5개의 원소씩 다 더해짐
#axis = 1 이면 (5,3)에서 3이 합쳐지고 다섯개의 원소가 남는다.  3차원도 동일하게 0,1,2 가 존재 
plt.imshow(imgRGB)          #2차원 array를 받아 어떤식으로 색을 채울지 정하는,,, 이미지를 화면에 출력
plt.show()

#그레이스케일 영상 출력
imgGray = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

plt.axis('off')
plt.imshow(imgGray, cmap='gray')
plt.show()

#컬러영상 & 그레이스케일 영상 불러오기
imgBGR = cv2.imread('cat.bmp')      
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)
imgGray = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

#두 개의 영상을 함께 출력
plt.subplot(121), plt.axis('off'), plt.imshow(imgRGB)           #(121)1행 2열로 나누어 1열의 위치에 사진을 출력한다는 의미
plt.subplot(122), plt.axis('off'), plt.imshow(imgGray, cmap='gray')     #완전한 회색을 위해 cmap 사용
plt.show()