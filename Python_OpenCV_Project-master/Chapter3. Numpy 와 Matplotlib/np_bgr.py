import cv2
import numpy as np



img = np.zeros((120,120,3), dtype= np.uint8) # 120 * 120 2차원 배열 생성, 3채널 컬러 이미지
img[25:35, :] = [255,0,0] # 25~35행 파란색 할당
img[55:65, :] = [0,255,0] # 55~65행 초록색 할당
img[85:95, :] = [0,0,255] # 85~95행 빨간색 할당
img[:, 35:45] = [255,255,0] # 모든 행, 35~45열에 하늘색 할당
img[:, 75:85] = [255,0,255] # 모든 행, 75~85열에 분홍색 할당

cv2.imwrite('./jpg/np_bgr.jpg', img)
cv2.imshow('BGR', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
