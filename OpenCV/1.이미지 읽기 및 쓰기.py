# The python libraries numpy and cv2 need to be imported before reading an image.
import numpy as np
import cv2

# The function cv2.imread() is used to read an image.
img_color = cv2.imread('test.jpg',1)
img_grayscale = cv2.imread('test.jpg',0)
img_unchanged = cv2.imread('test.jpg',-1)


# The function cv2.imshow() is used to display an image in a window.
cv2.imshow('color image',img_color)
cv2.imshow('grayscale image',img_grayscale)
cv2.imshow('unchanged image',img_unchanged)

#Printing the image type and shape for Color Image
print(type(img_color))
print(img_color.shape)

# waitKey() waits for a key press to close the window and 0 specifies indefinite loop
cv2.waitKey(0)

# cv2.destroyAllWindows() simply destroys all the windows we created.
cv2.destroyAllWindows()

# The function cv2.imwrite() is used to write an image.
cv2.imwrite('grayscale.jpg',img_grayscale)


# 이미지 읽기 : cv2.imread()
# 이미지 보여주기 : cv2.imshow()
# 이미지 저장하기 : cv2.imwrite()

import cv2

# 이미지 읽기 1번 방법

img_color = cv2.imread('test.jpg', cv2.IMREAD_COLOR)
img_gray = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)
img_unchange = cv2.imread('test.jpg', cv2.IMREAD_UNCHANGED)

# 이미지 읽기 2번 방법

img_color = cv2.imread('test.jpg', 1)
img_gray = cv2.imread('test.jpg', 0)
img_unchange = cv2.imread('test.jpg', -1)

# 이미지 보여주기
cv2.imshow('Color', img_color)
cv2.imshow('Gray', img_gray)
cv2.imshow('Unchange', img_unchange)

# 키보드 입력 대기
cv2.waitKey(0)

# 모든 윈도우 창 닫기
cv2.destroyAllWindows()

# 이미지 저장하기
cv2.imwrite('test_gray.jpg', img_gray)