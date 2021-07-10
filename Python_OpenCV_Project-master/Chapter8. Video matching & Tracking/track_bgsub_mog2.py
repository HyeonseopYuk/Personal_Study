import numpy as np, cv2

cap= cv2.VideoCapture('../img/walking.avi')
fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(1000/fps)
# 배경 제거 객체 생성
fgbg = cv2.createBackgroundSubtractorMOG2()
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    # 배경 제거 마스크 계산
    fgmask = fgbg.apply(frame)
    cv2.imshow('frame',frame)
    cv2.imshow('bgsub',fgmask)
    if cv2.waitKey(delay) & 0xff ==27:
        break
cap.release()
cv2.destroyAllWindows()