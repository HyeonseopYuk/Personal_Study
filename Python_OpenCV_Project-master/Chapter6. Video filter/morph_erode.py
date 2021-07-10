import cv2
import numpy as np

img = cv2.imread('../img/morph_dot.png')

# 구조화 요소 커널, 사각형 (3X3)생성
k = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
# 침식연산적용
erosion = cv2.erode(img, k)

# 결과출력
merged = np.hstack((img, erosion))
cv2.imshow('Erode', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()