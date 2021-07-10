import cv2, numpy as np

img1 = cv2.imread('../img/taekwonv1.jpg')
img2 = cv2.imread('../img/figures.jpg')
gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# ORB 디스크립터 추출기 생성
detector = cv2.ORB_create()
# 각 영상에 대해 키 포인트와 디스크립터 추출
kp1, desc1 = detector.detectAndCompute(gray1, None)
kp2, desc2 = detector.detectAndCompute(gray2, None)

# BFMatcher 생성, 해밍 거리, 상호 체크
matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
# 매칭 계산
matches = matcher.match(desc1,desc2)
# 매칭결과그리기
res = cv2.drawMatches(img1, kp1, img2, kp2, matches, None,\
                      flags = cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

cv2.imshow('BFMatcher + ORB',res)
cv2.waitKey()
cv2.destroyAllWindows()
