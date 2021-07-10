# 창 관리 API 사용하기

import cv2

file_path = '../img/girl.jpg'
img = cv2.imread(file_path)
img_gray = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE) # 이미지를 그레일 스케일로 읽기

cv2.namedWindow('origin', cv2.WINDOW_AUTOSIZE) # origin 이름으로 창 생성
cv2.namedWindow('gray', cv2.WINDOW_NORMAL) # gray 이름으로 창 생성

cv2.imshow('origin', img)
cv2.imshow('gray', img_gray)

cv2.moveWindow('origin', 0,0) # 창 위치
cv2.moveWindow('gray', 100, 100) # 창 위치 변경

cv2.waitKey(0)
cv2.resizeWindow('origin', 200, 200)
cv2.resizeWindow('gray', 100,100)

cv2.waitKey(0)
cv2.destoryWindow('gray') # gray 창 닫기

cv2.waitKey(0)
cv2.destoryAllWindows()

