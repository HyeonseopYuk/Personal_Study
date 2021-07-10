# HSV, HSI, HSL
'''

Hue(색상), Saturation(채도), Value(명도)
Hue(색상), Saturation(채도), Intensity(밀도)
Hue(색상), Saturation(채도), Lightness(명도)

'''

import cv2
import numpy as np

# BGR 컬러 스페이스로 원색 픽셀 생성

red_bgr = np.array([[[0,0,255]]], dtype=np.uint8) # 빨간색 값만 갖는 픽셀
green_bgr = np.array([[[0,255,0]]], dtype=np.uint8) # 초록색 값만 갖는 픽셀
blue_bgr = np.array([[[255,0,0]]], dtype=np.uint8) # 파란색 값만 갖는 픽셀
yellow_bgr = np.array([[[0,255,255]]], dtype=np.uint8) # 노란색 값만 갖는 픽셀

# BGR 컬러 스페이스를 HSV 컬러 스페이스로 변환

red_hsv = cv2.cvtColor(red_bgr, cv2.COLOR_BGR2HSV)
green_hsv = cv2.cvtColor(green_bgr, cv2.COLOR_BGR2HSV)
blue_hsv = cv2.cvtColor(blue_bgr, cv2.COLOR_BGR2HSV)
yellow_hsv = cv2.cvtColor(yellow_bgr, cv2.COLOR_BGR2HSV)

# HSV로 변환한 픽셀 출력
print('red:', red_hsv)
print('green:', green_hsv)
print('blue:', blue_hsv)
print('yellow:', yellow_hsv)