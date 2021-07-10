import cv2
import numpy as np

# 연산에 사용할 배열 생성

a = np.array([[1,2]], dtype= np.uint8)
b = np.array([[10,20]], dtype= np.uint8)

# 두번째 요소가 0인 마스크 배열 생성
mask = np.array([[1,0]], dtype= np.uint8)

# 누적 할당과의 비교 연산
c1 = cv2.add(a,b, None, mask)
print(c1)
c2 = cv2.add(a,b,b, mask)
print(c2)