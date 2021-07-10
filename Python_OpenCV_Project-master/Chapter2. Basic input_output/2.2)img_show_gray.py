# 이미지 파일을 그레이 스케일로 화면에 표시

import cv2

img_file = '../img/girl.jpg'
img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)

if img is not None:
    cv2.imwrite('jpg/img_show_gray.jpg', img)
    cv2.imshow('IMG', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print("No Image file")
