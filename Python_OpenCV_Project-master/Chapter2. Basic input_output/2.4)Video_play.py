# 동영상 파일 읽기

import cv2

video_file = "../img/big_buck.avi"
cap = cv2.VideoCapture(video_file) # 동영상 캡처 객체 생성
if cap.isOpened(): # 캡처 객체 초기화 확인
    while True:
        ret, img = cap.read() # 다음 프레임 읽기
        if ret:
            cv2.imshow(video_file, img) # 화면에 표시
            cv2.waitKey(25) # 25ms 지연 (40fps로 가정)
        else: # 다음 프레임을 읽을 수 없음
            break  # 재생 완료
else:
    print("Can't open video.")
cap.release()
cv2.destroyAllWindows()
