# OpenCV로 이미지 크기 조정에 대해 알아봅시다 . 이미지 크기를 조정하려면 지정된 배율 인수를 고려하여 각 축(높이 및 너비)을 따라 크기를 조정하거나 원하는 높이 및 너비만 설정하십시오.  

# 이미지 크기를 조정할 때:

# 크기가 조정된 이미지에서도 동일하게 유지하려면 이미지의 원래 종횡비(즉, 너비와 높이)를 염두에 두는 것이 중요합니다.
# 이미지 크기를 줄이려면 픽셀을 다시 샘플링해야 합니다. 
# 이미지 크기를 늘리려면 이미지를 재구성해야 합니다. 즉, 새 픽셀을 보간해야 합니다.
# 이러한 작업을 수행하기 위해 다양한 보간 기술이 사용됩니다. OpenCV에서는 여러 방법을 사용할 수 있으며 선택은 일반적으로 특정 응용 프로그램에 따라 다릅니다.

# 모듈 가져 오기
import cv2
import numpy as np

# 이미지 읽기
    # imread()함수를 사용하여 이미지를 읽습니다.
image = cv2.imread('cat.jpg')

    # 이미지 크기를 조정하기 위해 원래 크기를 알아야 합니다.
    # shape 메소드를 사용하여 이미지의 높이와 너비를 알 수 있습니다.
    # image.shape 메소드는 (높이, 너비, 채널)을 반환합니다.
    # size() 함수를 사용하여도 높이와 너비를 알 수 있습니다. / image.size().width , image.size().height
h,w,c = image.shape
print('높이: ', h , '너비: ', w, '채널: ', c)
    # 여기서 주목해야 할 한 가지 중요한 점은 OpenCV가 이미지의 모양을높이 * 너비 * 채널형식을 제공하는 반면 일부 다른 이미지 처리 라이브러리는 너비, 높이 형식을 제공합니다.
    # 여기에는 논리적인 이유가 있습니다.
    # OpenCV를 사용하여 이미지를 읽으면 NumPy 배열로 표시됩니다.
    # 그리고 일반적으로 항상 배열의 모양을 참조합니다.
    # 행 * 열(높이를 나타내는 행과 너비를 나타내는 열).
    # 따라서 모양을 얻기 위해 OpenCV로 이미지를 읽을 때도 동일한 NumPy 배열 규칙이 적용됩니다.
    # 그리고 다음과 같은 형태로 모양을 얻습니다. 높이 * 너비 * 채널.

# 크기 조정 함수 구문
    # OpenCV 함수 구문 / resize() 함수를 사용하여 이미지 크기를 조정할 수 있습니다.
    # 1.원본 이미지 / 2. 크기 조정된 이미지의 원하는 크기
    # resize(src, dsize[, dst[, fx[, fy[, interpolation]]]])
    # src: 입력 이미지(필수 입력 이미지이며, 입력이미지의 경로가 포함된 문자열이 될 수도 있습니다.)
    # dsize: 출력 이미지 크기(가로, 세로) / (가로, 세로) 튜플
    # fx: 가로축으로의 비율
    # fy: 세로축으로의 비율
    # interpolation:  이미지 크기를 조정하는 다양한 방법에 대한 옵션
# 이미지 크기 조정
down_width = 300
down_height = 200
down_points = (down_width, down_height)
resize_down = cv2.resize(image, down_points, interpolation=cv2.INTER_LINEAR)

# 이미지 크기 늘리기
up_width = 600
up_height = 400
up_points = (up_width, up_height)
resize_up = cv2.resize(image, up_points, interpolation=cv2.INTER_LINEAR)

# OpenCV imshow() 함수를 사용하여 모든 이미지를 표시
cv2.imshow('down_image', resize_down)
cv2.waitKey()
cv2.imshow('up_image', resize_up)
cv2.waitKey()
cv2.destroyAllWindows()
    #한 가지 주의할 점은 너비와 높이에 대한 명시적인 값을 정의하여 크기를 조정하면 결과 이미지가 왜곡된다는 것입니다. 즉, 이미지의 종횡비가 그대로 유지되지 않습니다.

# 배율 인수를 사용하여 이미지 크기 조정
    # 배율 인수가 무엇인가 ?
    # 스케일링 팩터 또는 스케일 팩터는 일반적으로 일부 수량을 확장하거나 곱하는 숫자
    # 종횡비를 그대로 유지하고, 디스플레이 품질을 유지하는데 도움이 됩니다.
    # 따라서 이미지를 확대하거나 축소해도 이미지가 왜곡되지 않습니다.
# 스케일링 팩터를 사용하여 이미지 크기 조정
scale_up_x = 1.5
scale_up_y = 1.5
# 다운 스케일링 팩터 : 싱글
scale_down = 0.6

scaled_f_down = cv2.resize(image, None, fx=scale_down, fy=scale_down, interpolation=cv2.INTER_LINEAR)
scaled_f_up = cv2.resize(image, None, fx=scale_up_x, fy=scale_up_y, interpolation=cv2.INTER_LINEAR)
    # 수평 및 수직 축을 따라 새로운 배율 인수를 정의할 수 있습니다.
    # 배율 인수를 정의하면 너비와 높이에 대한 새 포인트가 필요하지 않습니다. 따라서 우리 dsize는 None.
    
# 시각화
cv2.imshow('scaled_f_down', scaled_f_down)
cv2.waitKey()
cv2.imshow('scaled_f_up', scaled_f_up)
cv2.waitKey()

# 다른 보간 방법으로 크기 조정
    # 크기 조정 목적에 따라 다른 보간 방법이 사용됩니다.
    # INTER_AREA:
        # INTER_AREA 리샘플링을 위해 픽셀 영역 관계를 사용합니다. 이미지 크기 축소(수축)에 가장 적합합니다. 이미지를 확대할 때 사용하는 INTER_NEAREST방법입니다.
    # INTER_CUBIC:
        # 이미지 크기를 조정하기 위해 바이큐빅 보간법을 사용합니다. 새 픽셀의 크기를 조정하고 보간하는 동안 이 방법은 이미지의 4×4 인접 픽셀에 적용됩니다.
        # 그런 다음 16픽셀의 가중치 평균을 사용하여 보간된 새 픽셀을 만듭니다.
    # INTER_LINEAR:
        # 이 방법은 보간과 다소 유사합니다 INTER_CUBIC. 그러나 와 달리 INTER_CUBIC보간된 픽셀의 가중 평균을 얻기 위해 2×2 인접 픽셀을 사용합니다.
    # INTER_NEAREST:
        # 이 INTER_NEAREST방법은 보간에 가장 가까운 이웃 개념을 사용합니다. 이것은 보간을 위해 이미지에서 인접한 하나의 픽셀만 사용하는 가장 간단한 방법 중 하나입니다.
res_inter_nearest = cv2.resize(image, None, fx= scale_down, fy= scale_down, interpolation= cv2.INTER_NEAREST)
res_inter_linear = cv2.resize(image, None, fx= scale_down, fy= scale_down, interpolation= cv2.INTER_LINEAR)
res_inter_area = cv2.resize(image, None, fx= scale_down, fy= scale_down, interpolation= cv2.INTER_AREA)

vertical= np.concatenate((res_inter_nearest, res_inter_linear, res_inter_area), axis = 0)
cv2.imshow('Inter Nearest :: Inter Linear :: Inter Area', vertical)