from picamera2.picamera2 import Picamera2
import cv2
import numpy as np

def grabFrame(camera):
    frame = camera.capture_array()
    frame =cv2.flip(frame, 0)
    return frame
    