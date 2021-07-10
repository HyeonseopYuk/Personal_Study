import cv2
import numpy as np
import matplotlib.pyplot as plt

# 이미지를 그레이 스케일로 읽기

img = cv2.imread('../img/gray_gradient.jpg', cv2.IMREAD_GRAYSCALE)

# Numpy 연산으로 바이너리 이미지 만들기
thresh_np = np.zeros_like(img)
thresh_np[img >127] = 255

# OpenCV 함수로 바이너리 이미지 만들기
ret, thresh_cv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
print(ret) # 127.0, 바이너리 이미지에 사용된 경계값 반환

# 원본과 결과물 출력
imgs = {'Original' : img, 'NumPy API': thresh_np, 'cv2.threshold': thresh_cv}
for i, (key, value) in enumerate(imgs.items()):
    plt.subplot(1,3, i+1)
    plt.imshow(value, cmap='gray')
    plt.xticks([]); plt.yticks([])

plt.show()

