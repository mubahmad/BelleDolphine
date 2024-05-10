import cv2
import numpy as np
import pyqrcode
import os

# Step 1: Generate and save 10 QR codes
qr_library_path = "qr_library"
os.makedirs(qr_library_path, exist_ok=True)

for i in range(1, 11):
    data = f"QR_Code_{i}"
    qr = pyqrcode.create(data)
    qr_path = os.path.join(qr_library_path, f"QR_Code_{i}.png")  # Naming convention
    qr.png(qr_path, scale=6)

# Step 2: Detect the QR codes from the library
cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

while True:
    ret, img = cap.read()
    if not ret:
        print("Failed to capture frame")
        break
    
    data, loc, _ = detector.detectAndDecode(img)
    cv2.imshow('Bounding Box', img)
    
    if data:
        print("Detected QR code:", data)
        print("Location:", loc)
        
        # Identify which QR code from the library is detected
        for i in range(1, 11):
            if f"QR_Code_{i}" in data:
                print("Detected QR code from library:", f"QR_Code_{i}")
                break
        
        points = np.array(loc, dtype=np.int32)
        cv2.polylines(img, [points], isClosed=True, color=(0, 0, 0), thickness=6)
        cv2.imshow('Bounding Box', img)
        cv2.waitKey(0)  # Press any key to capture the image with bounding box
        cv2.imwrite("detected_qr_code.png", img)  # Save the image
        break

cap.release()
cv2.destroyAllWindows()
