# OpenCV 라이브러리 가져오기
import cv2

# 파일에서 비디오 읽기
# VideoCapture(path, apiPreference)
# path: 읽을 비디오 파일 경로
# apiPreference: 사용할 비디오 코덱을 지정
vid_capture = cv2.VideoCapture('videos/video.mp4')

# isOpened() 메서드를 사용하여 비디오 파일이 성공적으로 열렸는지 확인하기
# isOpened() 메서드는 비디오 파일이 열렸으면 True, 열리지 않았으면 False를 반환
# 비디오 파일이 성공적으로 열렸다고 가정하면 get() 메서드를 사용하여 비디오 파일의 속성을 가져올 수 있음

if (vid_capture.isOpened() == False):
  print('Error: 비디오 파일을 열 수 없습니다.')
else:
  # get() 메서드를 사용하여 비디오 파일의 속성을 가져옴
  fps = int(vid_capture.get(5))
  print('FPS:', fps)

  # 비디오 파일의 프레임 수를 가져옴
  frame_count = vid_capture.get(7)
  print('Frame Count:', frame_count)
  
# 이미지 프레임을 읽을 준비가 되었음.
# 루프를 생성하고, 비디오 스트림에서 한 번에 하나의 프레임을 읽음
# 비디오 스트림에서 프레임을 읽을 때마다 비디오 파일의 모든 프레임을 읽을 때까지 루프를 반복
# vid_capture.read() 메서드를 사용하여 비디오 스트림에서 프레임을 읽음, 첫 번째 요소는 프레임을 읽었는지 여부를 나타내는 불리언 값, 두 번째 요소는 튜플 형식의 프레임을 반환
# 첫 번째 요소가 True이면 프레임이 성공적으로 읽혔음을 의미
# 읽을 프레임이 있는 경우 imshow() 메서드를 사용하여 프레임을 표시, waitKey() 메서드를 사용하여 프레임을 표시하는 시간을 지정, q 키를 누르면 루프를 중지
while(vid_capture.isOpened()):
  # 비디오 스트림에서 프레임을 읽음 그리고 프레임이 성공적으로 읽혔는지 확인
  ret, frame = vid_capture.read()
  if ret == True:
    # 프레임을 표시
    cv2.imshow('Frame', frame)
    # 25ms 동안 키 입력을 대기
    # q 키를 누르면 루프를 중지
    q = cv2.waitKey(25)
    if q == ord('q'): # ord() 메서드를 사용하여 문자를 ASCII 코드로 변환
      break
    else:
      break
    
# vid_capture 비디오 스트림이 완전히 처리되었으면 release() 메서드를 사용하여 비디오 스트림을 닫음
# 사용자가 조기에 루프를 종료하면 destroyAllWindows() 메서드를 사용하여 모든 창을 닫음
vid_capture.release()
cv2.destroyAllWindows()

# 이미지 시퀀스 읽기
# 이미지 시퀀스에서 이미지 프레임을 처리하는 것은 비디오 스트림에서 프레임을 처리하는것과 매우 유사, 읽고 있는 이미지 파일을 지정하기만 하면 됨
# vid_capture 개체를 계속 사용, 비디오 파일을 지정하는 대신 이미지 시퀀스를 지정
# %04d는 4자리 시퀀스 명명규칙 (0000, 0001, 0002, 0003, ...), %02d는 2자리 시퀀스 명명규칙 (video00.jpg, video01.jpg, video02.jpg, video03.jpg, ...)
vid_capture = cv2.VideoCapture('videos/video%04d.jpg')

# 웹 캠에서 비디오 읽기
# 웹 캠에서 비디오를 읽는 것은 이미지 시퀀스에서 비디오를 읽는 것과 매우 유사
# OpenCV에는 다양한 입력인수를 허용하는 편의를 위해 여러가지 오버로드 함수가 있음
# 비디오 파일이나, 이미지시퀀스의 소스 위치를 지정하는 대신 비디오 캡처 장치 인덱스를 제공
# 시스템에 내장형 웹캠이 있는 경우 카메라의 장치 인덱스는 0
# 시스템에 여러 개의 웹캠이 있는 경우 장치 인덱스는 0, 1, 2, 3, ... 순서로 할당
vid_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# CAP_DSHOW는 DirectShow (via videoInput) 백엔드를 사용하여 비디오 캡처 장치를 열도록 지정, 필수는 아님

#동영상 작성
# 모든소스에서 가져온 프레임을 하나의 비디오 파일로 저장
# 메서드를 사용하여 이미지 프레임 높이와 너비를 검색 get()
# 비디오 스트림을 메모리로 읽기 위해 비디오 캡처 개체를 초기화
# 비디오 작성기 개체 생성
# 비디오 기록기 개체를 사용하여 비디오 스트림을 저장
frame_width = int(vid_capture.get(3))
frame_height = int(vid_capture.get(4))
frame_size = (frame_width, frame_height)
fps = 20