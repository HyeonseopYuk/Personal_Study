import cv2
import numpy as np

isDragging = False # 마우스 드래그 상태 저장
x0,y0, w, h = -1,-1,-1,-1 # 영역 선택 좌표 저장
blue, red = (255,0,0), (0,0,255) # 색상 값

def onMouse(event, x,y, flags, param):
    global isDragging, x0,y0, img
    if event == cv2.EVENT_LBUTTONDOWN: # 왼쪽 버튼 누르고, 드래깅 시작
        isDragging = True
        x0 = x
        y0 = y
    elif event == cv2.EVENT_MOUSEMOVE:
        if isDragging:
            img_draw = img.copy()
            cv2.rectangle(img_draw, (x0,y0), (x,y), blue,2) # 드래그 진행 영역 표시
            cv2.imshow('img', img_draw)
    elif event == cv2.EVENT_LBUTTONUP:
        if isDragging:
            isDragging = False
            w = x-x0
            h= y-y0
            print("x:%d, y:%d, w:%d, h:%d" %(x0,y0,w,h))
            if w >0 and h>0:
                img_draw = img.copy() # 선택 영역에 사각형 그림을 표시할 이미지 복제
                # 선택 영역에 빨간색 사각형 표시
                cv2.rectangle(img_draw, (x0,y0), (x,y), red,2)
                cv2.imshow('img', img_draw) # 빨간색 사각형이 그려진 이미지 화면 출력
                roi = img[y0:y0+h, x0:x0+w]
                cv2.imshow('cropped', roi) # ROI 지정 영역을 새 창으로 표시
                cv2.moveWindow('cropped', 0,0) # 새 창을 화면 좌측 상단으로 이동
                cv2.imwrite('./jpg/cropped.jpg', roi)
                print("croped.")
            else:
                # 드래그 방향이 잘못된 경우 사각형 그림이 없는 원본 이미지 출력
                cv2.imshow('img',img)
                print("좌측 상단에서 우측 하단으로 영역을 드래그 하세요.")
img = cv2.imread('../img/sunset.jpg')
cv2.imshow('img',img)
cv2.setMouseCallback('img', onMouse)
cv2.waitKey()
cv2.destroyAllWindows()