import cv2
  
print('Begin connect...')
cam = cv2.VideoCapture(0)
#cam = cv2.VideoCapture('/dev/video0')
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)
cam.set(cv2.CAP_PROP_FPS, 50)
#cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))

print('Begin grab...')
while(True):
    ret, frame = cam.read()
    cv2.imshow('frame', frame)
    if (cv2.waitKey(1) & 0xFF) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()