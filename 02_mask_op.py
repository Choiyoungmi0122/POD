import cv2
import sys

#IMREAD_COLOR 이미지 파일을 컬러로 읽고, default값 이다.
#IMREAD_GRAYSCALE 이미지를 GRAYSCALE 로 읽는다.
#cv2.IMREAD_UNCHANGED 이미지 파일을 alpha channel까지 포함하여 읽는다.   -> 원본사용을 한다.,..?

# src = cv2.imread('airplane.bmp', cv2.IMREAD_COLOR)
# mask = cv2.imread('mask_plane.bmp', cv2.IMREAD_GRAYSCALE)
# dst = cv2.imread('field.bmp', cv2.IMREAD_COLOR)

# # if src is None or mask is None or dst is None:
# #     print("Image load falied!")
# #     sys.exit()
    
    
# cv2.copyTo(src, mask, dst)

# # dst[mask > 0] = src[mask > 0]

# # cv2.imshow('src', src)
# # cv2.imshow('mask', mask)
# cv2.imshow('dst', dst)

# cv2.waitKey()
# cv2.destroyAllWindows()


cat = cv2.imread('cat.bmp', cv2.IMREAD_COLOR)
logo = cv2.imread('opencv-logo-white.png', cv2.IMREAD_UNCHANGED)

alpha = logo[:,:,3]       #alpha는 알파 채널로 만든 alpha 영상
logo = logo[:,:,:-1]     #logo는 b,g,r 3 채널로 구성된 컬러영상 마지막 채널만 남김...?
h,w = alpha.shape[:2]
crop = cat[10:10+h,10:10+w] #logo, alpha 와 같은 큰기의 부분 영상 추출


cv2.copyTo(logo, alpha, crop)
cv2.imshow('cat', cat)          # 왜 cat 에 저장되는 거지...?

cv2.waitKey()
cv2.destroyAllWindows()