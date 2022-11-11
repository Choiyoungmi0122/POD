import cv2

img = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

cv2.imshow('img', img)

while True:
    keycode = cv2.waitKey()
    if keycode == ord('i') or keycode == ord('I'):      #키보드로 입력을 받는데 해당 것들을 입력받으면
        img = ~img      # 반전실행 (원래 것에서 )
        cv2.imshow('image', img)
    elif keycode == 27:
        break
    
cv2.destroyAllWindows()