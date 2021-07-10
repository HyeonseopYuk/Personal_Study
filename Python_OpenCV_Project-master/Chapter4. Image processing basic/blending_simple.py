# 알파 블렌딩

import cv2
import numpy as np
import matplotlib.pyplot as plt

# 연산에 사용할 이미지 읽기
img1 = cv2.imread('../img/wing_wall.jpg')
img2 = cv2.imread('../img/yate.jpg')

# 이미지 덧셈
img3 = img1 + img2
img4 = cv2.add(img1,img2)

imgs = {'img1' : img1, 'img2': img2,
        'img1+img2' : img3, 'cv2.add(img1,img2)' : img4}

# 이미지 출력
for i, (k,v) in enumerate(imgs.items()):
    plt.subplot(2,2,i+1)
    plt.imshow(v[:,:,::-1])
    plt.title(k)
    plt.xticks([]);plt.yticks([])
plt.show()