# 이미지를 불러오고 사용자가 마우스로 클릭하고 드래그하여 관심영역(ROI)을 선택
# 선택한 영역만 따로 저장하거나 표시

import cv2 as cv
import sys

img = cv.imread('soccer.jpg')
if img is None:
    sys.exit('파일을 찾을 수 없습니다.')

ix, iy = -1, -1
drawing = False    # 드래그 중인지 여부
roi = None         # 추출된 ROI
orig_img = img.copy()  # 초기 이미지를 보관 (r 키로 리셋할 때 사용)

def draw(event, x, y, flags, param):
    global ix, iy, drawing, roi, img

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            temp = img.copy()
            cv.rectangle(temp, (ix, iy), (x, y), (0, 0, 255), 2)
            cv.imshow('Drawing', temp)

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        # 최종 사각형 그리기
        cv.rectangle(img, (ix, iy), (x, y), (0, 0, 255), 2)
        cv.imshow('Drawing', img)

        # ROI 추출 (좌표 정렬)
        x1, y1 = min(ix, x), min(iy, y)
        x2, y2 = max(ix, x), max(iy, y)
        roi = img[y1:y2, x1:x2]

        # 유효한 ROI라면 별도 창에 표시
        if roi.size > 0:
            cv.imshow('ROI', roi)

cv.namedWindow('Drawing')
cv.imshow('Drawing', img)
cv.setMouseCallback('Drawing', draw)

while True:
    key = cv.waitKey(1) & 0xFF
    if key == ord('q'):
        break

    # r 키 -> ROI 및 이미지를 리셋
    elif key == ord('r'):
        img = orig_img.copy()
        roi = None
        cv.imshow('Drawing', img)
        cv.destroyWindow('ROI')

    # s 키 -> ROI 저장
    elif key == ord('s'):
        if roi is not None and roi.size > 0:
            cv.imwrite('saved_roi.jpg', roi)
            print("ROI가 'saved_roi.jpg'로 저장되었습니다.")

cv.destroyAllWindows()
