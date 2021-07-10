import cv2
import numpy as np

img = cv2.imread('../img/house.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Fast 특징 검출기 생성
fast = cv2.FastFeatureDetector_create(50)
# 키 포인트 검출
keypoints = fast.detect(gray, None)
# 키 포인트 그리기
img = cv2.drawKeypoints(img, keypoints, None)
# 결과 출력
cv2.imshow('FAST', img)
cv2.waitKey()
cv2.destroyAllWindows()