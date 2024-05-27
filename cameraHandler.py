from picamera2.picamera2 import Picamera2
import cv2
import numpy as np

def grabFrame(camera):
    frame = camera.capture_array()
    frame =cv2.flip(frame, 0)
    width = int(frame.shape[1] * 0.75)
    height = int(frame.shape[0] * 0.75)
    
    # Resize the image
    frame   = cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian Blur
    blurred = cv2.GaussianBlur(gray, (9, 9), 0)
    
    # Apply adaptive thresholding
    thresholded = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                        cv2.THRESH_BINARY, 11, 2)
    once=True
    if once:
        cv2.imwrite("process5.png", thresholded)
        once=False

    return thresholded
    