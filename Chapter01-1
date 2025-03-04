# OpenCV를 사용하여 이미지를 불러오고 화면에 출력
# 원본 이미지와 그레이스케일로 변환된 이미지를 나란히 표시

import cv2 as cv
import sys 
import numpy as np


img = cv.imread('soccer.jpg')

if img is None:
    sys.exit('파일이 존재하지 않습니다.')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)      # BGR 컬러 영상을 명암 영상으로 변환
gray_3ch = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)

print(img[0, 0, 0], img[0,0,1], img[0,0,2])     # B, G, R

result = np.hstack((img, gray_3ch))

cv.imshow('Result', result)
cv.waitKey()
cv.destroyAllWindows()

print(type(img))
print(img.shape)
