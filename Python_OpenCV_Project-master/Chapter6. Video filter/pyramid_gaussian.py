import cv2

img = cv2.imread('../img/girl.jpg')

# 가우시안 이미지 피라미드 축소
smaller = cv2.pyrDown(img) # img X 1/4
# 가우시안 이미지 피라미드 확대
bigger = cv2.pyrUp(img) # img X 4

# 결과출력
cv2.imshow('img',img)
cv2.imshow('pyDown', smaller)
cv2.imshow('pyrUp', bigger)
cv2.waitKey(0)
cv2.destroyAllWindows()