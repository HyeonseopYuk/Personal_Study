# 관심영역 지정

'''
Numpy를 이용하여 관심영역 지정시 주의해야할 사항 두 가지

첫째, 일반적으로 도형을 코드에서 표현할 때 폭(Width) 높이(height) 순으로 하는 경향이 있다.
하지만 Numpy 배열은 행(Row), 열(Column)순으로 접근하므로 반드시 높이(height), 폭(Width) 순으로 지정해야한다.

둘째, Numpy 배열의 슬라이싱과 Python의 리스트의 슬라이싱 방식이 다르다.
파이썬의 리스트 슬라이싱은 새로운 리스트 객체를 반환하는 데 반해, Numpy 슬라이싱은 원본의 참조를 반환한다.
Numpy 배열의 객체는 슬라이싱 연산해서 얻은 결과의 값을 수정하면 슬라이싱 하기 전의 원본 배열 객체에도 똑같이 값이 달라진다.
만약 원본과는 무관한 새로운 작업을 하고자 한다면 슬라이싱 결과에 복제본을 생성해서 작업해야함 : copy()
'''

import cv2
import numpy as np

img = cv2.imread('../img/sunset.jpg')

x=320;y=150; w=50; h=50 # roi 좌표
roi = img[y:y+h, x:x+w] # roi지정

print(roi.shape) # roi shape, (50,50,3)
cv2.rectangle(roi, (0,0), (h-1,w-1), (0,255,0)) # roi에 사각형 그리기
cv2.imshow("img",img)

cv2.waitKey(0)
cv2.destroyAllWindows()