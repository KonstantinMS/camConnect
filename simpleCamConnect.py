"""
Простой модуль для захвата и отображения видео с камеры.

Использует библиотеку OpenCV для работы с видеопотоком.
"""

import cv2
import sys

# Константы для настройки захвата видео
WIDTH = 800  # Ширина кадра
HEIGHT = 600  # Высота кадра
FRAME_RATE = 50  # Частота кадров
CODEC = 'MJPG'  # Кодек для сжатия видео
DEV = '/dev/video0'  # Путь к устройству камеры


def setup_camera():
    """
    Настройка подключения к камере в зависимости от операционной системы.

    Для Linux используется API V4L2, для Windows - DirectShow.
    """
    print('Begin connect...')
    if sys.platform == 'linux':
        cam = cv2.VideoCapture(DEV, cv2.CAP_V4L2)
    else:
        cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    return cam


def configure_capture(cam):
    """
    Настраивает параметры захвата видео.

    Устанавливает ширину, высоту, частоту кадров и кодек.
    """
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
    cam.set(cv2.CAP_PROP_FPS, FRAME_RATE)
    cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*tuple(CODEC)))


def capture_and_display(cam):
    """
    Захватывает видеопоток и отображает его в окне.

    Продолжает захватывать кадры до нажатия клавиши 'q'.
    """
    print('Begin grab...')
    while True:
        ret, frame = cam.read()
        cv2.imshow('frame', frame)

        if (cv2.waitKey(1) & 0xFF) == ord('q'):
            break


def main():
    cam = setup_camera()
    configure_capture(cam)
    capture_and_display(cam)

    # Освобождаем ресурсы
    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()