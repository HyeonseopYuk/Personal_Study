import cv2
import numpy as np
import matplotlib.pyplot as plt

# 이미지를 그레이 스케일로 읽기 및 출력하기

img= cv2.imread('../img/mountain.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('img',img)

# 히스토그램 계산 및 그리기
hist = cv2.calcHist([img],[0], None, [256], [0,256])
plt.plot(hist)

print(hist.shape) # 히스토그램의shape(256,1)
print(hist.sum(), img.shape) # 히스토그램의 총 합계와 이미지의 크기
plt.show()

