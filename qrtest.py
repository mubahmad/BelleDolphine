import cv2 as cv
import numpy as np
import os
import time

# Create a QRCodeDetector object
detector = cv.QRCodeDetector()

# Function to detect and draw QR code bounding box
def detect_and_draw(frame):
    # Detect and decode QR code
    retval, points, straight_qrcode = detector.detectAndDecode(frame)

    # Check if QR code is detected
    if retval:
        # Convert points to integers if points are not None
        if points is not None:
            points = np.array(points, dtype=np.int32)
            print("QR Code detected:", retval)
            # Draw bounding box around the QR code
            frame = cv.polylines(frame, [points], isClosed=True, color=(140, 255, 0), thickness=6)
            
            # Save the frame to desktop
            save_frame_to_desktop(frame)

    return frame

# Function to try opening different camera indices
def try_cameras():
    camera_indices = [0,23]  # List of camera indices to try
    for index in camera_indices:
        cap = cv.VideoCapture(index)
        if cap.isOpened():
            print(f"Camera {index} opened successfully.")
        else:
            print(f"Failed to open camera {index}.")
    return None

# Function to save frame to desktop
def save_frame_to_desktop(frame):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"qr_detected_{timestamp}.jpg"
    filepath = os.path.join(desktop_path, filename)
    cv.imwrite(filepath, frame)
    print(f"Frame saved to {filepath}")

# Initialize video capture
cap = try_cameras()

if cap is None:
    print("No valid camera found.")
else:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Failed to capture frame")
            break

        # Detect and draw QR code bounding box
        frame_with_bbox = detect_and_draw(frame)

        # Instead of displaying, print the frame shape as a confirmation
        print("Captured frame dimensions:", frame_with_bbox.shape)

        # Break the loop if 'q' is pressed (this will only work if you have a way to send 'q')
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture
    cap.release()
    cv.destroyAllWindows()
