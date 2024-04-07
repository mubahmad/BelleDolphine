import cv2 as cv
import numpy as np

# Create a QRCodeDetector object
detector = cv.QRCodeDetector()

# Function to detect and draw QR code bounding box
def detect_and_draw(frame):
    # Detect and decode QR code
    retval, points, straight_qrcode = detector.detectAndDecode(frame)

    # Check if QR code is detected
    if retval:
        # Convert points to integers
        points = np.array(points, dtype=np.int32)
        print(retval)
        # Draw bounding box around the QR code
        cv.polylines(frame, [points], isClosed=True, color=(140, 255, 0), thickness=6)

    return frame

# Initialize video capture
cap = cv.VideoCapture(0)  # Use 0 for the default camera

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame")
        break

    # Detect and draw QR code bounding box
    frame_with_bbox = detect_and_draw(frame)

    # Display the resulting frame
    cv.imshow('QR Code Detection', frame_with_bbox)

    # Break the loop if 'q' is pressed
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture
cap.release()
cv.destroyAllWindows()