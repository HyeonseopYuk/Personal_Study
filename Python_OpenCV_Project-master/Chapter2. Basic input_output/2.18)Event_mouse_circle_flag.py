# 플래그를 이용한 동그라미 그리기

import cv2

title = 'mouse evemt' # 창 제목
img= cv2.imread('../img/blank_500.jpg')
cv2.imshow(title, img)

colors= {'black' : (0,0,0),
         'red' : (0,0,255),
         'blue' : (255,0,0),
         'green' :(0,255,0)} # 색상 미리 정의

def onMouse(event,x,y,flags,param): #마우스 콜백 함수 구현
    print(event, x,y, flags) # 파라미터 출력
    color = colors['black']
    if event == cv2.EVENT_LBUTTONDOWN: # 왼쪽 버튼을 누른 경우
        # 컨트롤 키와 시프트 키를 모두 누른 경우
        if flags & cv2.EVENT_FLAG_CTRLKEY and flags & cv2.EVENT_FLAG_SHIFTKEY:
            color = colors['green']
        elif flags & cv2.EVENT_FLAG_SHIFTKEY:
            color = colors['blue']
        elif flags & cv2.EVENT_FLAG_CTRLKEY:
            color = colors['red']
        # 지름 30크기의 검은색 원을 해당 좌표에 그림
        cv2.circle(img, (x,y), 30, color,-1)
        cv2.imshow(title, img)
cv2.setMouseCallback(title, onMouse) # 마우스 콜백 함수를 GUI 윈도에 등록

while True:
    if cv2.waitKey(0) & 0xff ==27:
        break
cv2.destroyAllWindows()