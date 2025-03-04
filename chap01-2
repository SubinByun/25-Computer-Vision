# 웹캠을 사용하여 실시간 비디오 스트림을 가져온다.
# 각 프레임에서 Canny Edge Detection을 적용하여 에지를 검출하고 원본 영상과 함께 출력

import cv2 as cv
import sys
import numpy as np


cap = cv.VideoCapture(0, cv.CAP_DSHOW)      # 카메라와 연결 시도

if not cap.isOpened():
    sys.exit("카메라 연결 실패")



while True:
    ret, frame = cap.read()
    if not ret:
        print('프레임 획득에 실패하여 루프를 나갑니다.')
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    canny = cv.Canny(gray,50, 150)

    canny_3ch = cv.cvtColor(canny, cv.COLOR_GRAY2BGR)
    result = np.hstack((frame, canny_3ch))

    cv.imshow('Result', result)


    key = cv.waitKey(1)
    if key == ord('q'):
        break



cap.release()       # 카메메라와 연결을 끊음
cv.destroyAllWindows()
