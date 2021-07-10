import cv2
import matplotlib.pyplot as plt

img = cv2.imread('../img/girl.jpg')

plt.imshow(img[:,:,::-1]) # 이미지 컬러 채널 변경해서 표시
plt.xticks([])
plt.yticks([])
plt.savefig('jpg/plt_imshow_rgb.jpg')
plt.show()