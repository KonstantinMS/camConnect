import cv2

cam_w = 640
cam_h = 480
cam_fps = 50

print('Begin connect...')
cam = cv2.VideoCapture(0)
#cam = cv2.VideoCapture('/dev/video0')
cam.set(cv2.CAP_PROP_FRAME_WIDTH, cam_w)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, cam_h)
#cam.set(cv2.CAP_PROP_FPS, cam_fps)
#cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))

aim_x = cam_w // 2
aim_y = cam_h // 2
aim_size = 50
aim_thikness = 1
aim_color = (0, 0, 255)
step = 1


def print_coor():
    print(f'x = {aim_x}, y = {aim_y}')


print('Begin grab...')
while(True):
    ret, frame = cam.read()

    cv2.line(frame, (aim_x-aim_size, aim_y), (aim_x+aim_size, aim_y), aim_color, aim_thikness)
    cv2.line(frame, (aim_x, aim_y), (aim_x, aim_y+aim_size), aim_color, aim_thikness)
    cv2.putText(frame, f'x = {str(aim_x)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                   1, (0,0, 255), 1, cv2.LINE_AA)
    cv2.putText(frame, f'y = {str(aim_y)}', (10, 60), cv2.FONT_HERSHEY_SIMPLEX,
                   1, (0,0, 255), 1, cv2.LINE_AA)

    if ret:
        cv2.imshow('frame', frame)
    else:
        print("Error Drawing Frame")

    key = cv2.waitKeyEx(1)
    # if key != -1:
    #      print(key)
    if key == ord('q'):
        break
    # windows arrows
    elif key == 2621440:   #down
        aim_y += step
        print_coor()
    elif key == 2490368:  # up
        aim_y -= step
        print_coor()
    elif key == 2424832:  # left
        aim_x -= step
        print_coor()
    elif key == 2555904:  # right
        aim_x += step
        print_coor()
    elif ord('0') <= key <= ord('9'):
        step = key - ord('0')

cam.release()
cv2.destroyAllWindows()
