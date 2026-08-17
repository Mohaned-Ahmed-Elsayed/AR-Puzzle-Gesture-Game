#camera.py
import cv2
from config.settings import CAMERA_WIDTH, CAMERA_HEIGHT


class Camera:

    def __init__(self):
        self.cap = cv2.VideoCapture(0)

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT)

    def read(self):
        ret, frame = self.cap.read()

        if not ret:
            return None

        return cv2.flip(frame, 1)

    def release(self):
        self.cap.release()