import cv2
import matplotlib.pyplot as plt

img = cv2.imread('../img/girl.jpg')
plt.imshow(img)
plt.savefig('jpg/plt_imshow.jpg')
plt.show()