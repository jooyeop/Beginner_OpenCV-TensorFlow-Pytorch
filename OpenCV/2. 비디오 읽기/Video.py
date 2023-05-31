import cv2 
 
# Create a video capture object, in this case we are reading the video from a file
# 비디오 캡처 객체를 만듭니다. 이 경우 비디오를 파일에서 읽습니다.
vid_capture = cv2.VideoCapture('Resources/Cars.mp4')
 
if (vid_capture.isOpened() == False):
  print("Error opening the video file")
# Read fps and frame count
# 비디오의 fps와 프레임 수를 읽습니다.
else:
  # Get frame rate information
  # You can replace 5 with CAP_PROP_FPS as well, they are enumerations
  # 5번은 fps를 의미합니다.
  fps = vid_capture.get(5)
  print('Frames per second : ', fps,'FPS')
 
  # Get frame count
  # You can replace 7 with CAP_PROP_FRAME_COUNT as well, they are enumerations
  # 7번은 프레임 수를 의미합니다.
  frame_count = vid_capture.get(7)
  print('Frame count : ', frame_count)
 
while(vid_capture.isOpened()):
  # vid_capture.read() methods returns a tuple, first element is a bool 
  # and the second is frame
  ret, frame = vid_capture.read()
  if ret == True:
    cv2.imshow('Frame',frame)
    # 20 is in milliseconds, try to increase the value, say 50 and observe
    key = cv2.waitKey(20)
     
    if key == ord('q'):
      break
  else:
    break
 
# Release the video capture object
vid_capture.release()
cv2.destroyAllWindows()


import cv2

# 비디오 캡처 객체를 만듭니다. 이 경우 비디오를 파일에서 읽습니다.
vid_cap = cv2.VideoCapture('video.mp4')

if (vid_cap.isOpened() == False):
    print("Error opening video stream or file")
    # 비디오의 fps와 프레임 수를 읽습니다.
    fps = int(vid_cap.get(5)) # 5번은 fps를 의미합니다.
    print('Frame Rate : ', fps)
    
    # 비디오의 프레임 수를 읽습니다.
    frame_count = vid_cap.get(7) # 7번은 프레임 수를 의미합니다.
    print('Frame Count : ', frame_count)