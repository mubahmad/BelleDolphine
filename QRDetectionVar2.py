import cv2
import numpy as np
cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

while True:
    ghoush,img = cap.read()
    dat,loc,_ = detector.detectAndDecode(img)
    cv2.imshow('Bounding Box', img)
    if dat:
        print(dat)
        print(loc)
        points = np.array(loc, dtype=np.int32)
        # Draw bounding box around the QR code
        cv2.polylines(img, [points], isClosed=True, color=(0, 0, 0), thickness=6)
        # Display the image
        cv2.imshow('Bounding Box', img)
        cv2.waitKey(1)
        cv2.imwrite("Trial 5.png", img)
        break
    
cap.release()