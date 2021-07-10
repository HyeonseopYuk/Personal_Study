import cv2
import cv2
import matplotlib.pyplot as plt

win_name = 'Alpha blending' # 창 이름
trackbar_name = 'fade' # 트랙바 이름

# 트랙바 이벤트 핸들러 함수

def onChange(x):
    alpha = x/100
    dst = cv2.addWeighted(img1, 1-alpha, img2, alpha, 0)
    cv2.imshow(win_name, dst)

# 합성영상읽기

img1 = cv2.imread('../img/man_face.jpg')
img2 = cv2.imread('../img/lion_face.jpg')

# 이미지 표시 및 트랙바 붙이기

cv2.imshow(win_name, img1)
cv2.createTrackbar(trackbar_name, win_name, 0, 100, onChange)

cv2.waitKey()
cv2.destroyAllWindows()