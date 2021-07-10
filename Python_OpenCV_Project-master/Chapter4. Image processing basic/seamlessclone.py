import cv2
import numpy as np
import matplotlib.pyplot as plt

# 합성 대상 영상 읽기
img1 = cv2.imread('../img/drawing.jpg')
img2 = cv2.imread('../img/my_hand.jpg')

# 마스크 생성, 합성할 이미지 전체 영역을 255로 세팅
mask = np.full_like(img1, 255)

# 합성 대상 좌표 계산(img2의 중앙)
height, width = img2.shape[:2]
center = (width//2, height//2)

# seamlessClone으로 합성
normal = cv2.seamlessClone(img1, img2, mask, center, cv2.NORMAL_CLONE)
mixed = cv2.seamlessClone(img1, img2, mask, center, cv2.MIXED_CLONE)

# 결과 출력
cv2.imshow('normal', normal)
cv2.imshow('mixed', mixed)
cv2.waitKey()
cv2.destroyAllWindows()