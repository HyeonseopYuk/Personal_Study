# 마우스 이벤트로 동그라미 그리기

import cv2
title = 'mouse event' # 창 제목
img = cv2.imread('../img/blank_500.jpg')
cv2.imshow(title, img)

def onMouse(event,x,y, flags, param): # 마우스 콜백함수 구현 [함수 내부에서 사용하지 않더라도 5개의 인자는 모두 선언부에 기재 해야 함]
    print(event,x,y) # 파라미터 출력
    if event == cv2.EVENT_LBUTTONDOWN: # 왼쪽 버튼 눌렀을 경우
        cv2.circle(img,(x,y),30, (0,0,0), -1) # 지름이 30픽셀인 검은색 원을 해당 좌표에 그림
        cv2.imshow(title, img) # 그려진 이미지를 다시 표시

cv2.setMouseCallback(title, onMouse) # 마우스 콜백 함수를 GUI 윈도에 등록

while True:
    if cv2.waitKey(0) & 0xff ==27:
        break

cv2.destroyAllWindows()