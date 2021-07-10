# 키 이벤트

import cv2

img_file = '../img/girl.jpg'
img = cv2.imread(img_file)
title='IMG'
x,y = 100,100

while True:
    cv2.imshow(title, img)
    cv2.moveWindow(title, x,y)
    key = cv2.waitKey(0) & 0xFF # 키보드 입력을 무한 대기, 8비트 마스크 처리
    print(key, chr(key))
    if key == ord('h'):  # 'h' 키이면 좌로 이동
        x -= 10
    elif key == ord('j'): #'j' 키이면 아래로 이동
        y += 10
    elif key == ord('k'): #'k' 키이면 위로 이동
        y -= 10
    elif key == ord('l'): #'l' 키이면 오른쪽으로 이동
        x += 10
    elif key == ord('q') & key ==27: # 'q' 이거나 'esc'이면 종료
        break
        cv2.destoryAllWindows()
    cv2.moveWindow(title,x,y) # 새로운 좌표로 창 이동