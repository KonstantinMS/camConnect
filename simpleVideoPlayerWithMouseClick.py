import cv2

# Путь к файлу видео
PATH = 'video.mp4'
STEP = 10

def mouse_handler(event, x, y, flags, param):
    """
    Обработчик событий мыши.

    :param event: Тип события (например, клик левой кнопкой)
    :param x: Координата X курсора
    :param y: Координата Y курсора
    :param flags: Дополнительные флаги
    :param param: Дополнительный параметр
    """
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Клик по координатам: ({x}, {y})")


# Открываем видеопоток из файла
PATH = PATH.strip().replace('\\', '/')
cap = cv2.VideoCapture(PATH)

# Создаем окно для отображения видео
cv2.namedWindow("Video")

# Устанавливаем обработчик событий мыши
cv2.setMouseCallback("Video", mouse_handler)

# Флаг паузы и счетчики кадров
is_paused = False
last_frame = None
current_frame = 0

while True:
    if not is_paused:
        # Читаем следующий кадр
        ret, frame = cap.read()

        if not ret:
            # Если конец видео достигнут, выходим из цикла
            break

        last_frame = frame
        current_frame += 1

    # Отображаем последний прочитанный кадр
    if last_frame is not None:
        cv2.imshow("Video", last_frame)

    # Ожидание нажатия клавиши
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):
        # Выход при нажатии 'q'
        break
    elif key == ord(' '):
        # Переключение паузы
        is_paused = not is_paused
        print(f"Видео {'остановлено' if is_paused else 'возобновлено'}")
    elif key == ord('a'):
        # Перемотка назад на 10 кадров
        new_position = max(0, current_frame - STEP)
        cap.set(cv2.CAP_PROP_POS_FRAMES, new_position)
        current_frame = new_position
        _, last_frame = cap.read()
        print(f"Перемотано назад на {STEP} кадров. Текущий кадр: {current_frame}")
    elif key == ord('d'):
        # Перемотка вперед на 10 кадров
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        new_position = min(total_frames - 1, current_frame + STEP)
        cap.set(cv2.CAP_PROP_POS_FRAMES, new_position)
        current_frame = new_position
        _, last_frame = cap.read()
        print(f"Перемотано вперед на {STEP} кадров. Текущий кадр: {current_frame}")

# Освобождаем ресурсы
cap.release()
cv2.destroyAllWindows()