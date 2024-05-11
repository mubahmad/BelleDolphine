import cv2
import numpy as np
from time import time, sleep
import RPi.GPIO as GPIO
import random
from clean import clean

# Cleanup GPIO
def cleanup_gpio():
    GPIO.cleanup()

# Function to detect and draw QR code bounding box
def detect_and_draw(frame, rooms, start_time):
    detector = cv2.QRCodeDetector()
    retval, points, straight_qrcode = detector.detectAndDecode(frame)
    if retval:
        room_id = int(retval)
        if room_id in rooms:
            points = np.array(points, dtype=np.int32)
            cv2.polylines(frame, [points], isClosed=True, color=(140, 255, 0), thickness=6)
            print(f"Room ID: {room_id}, Name: {rooms[room_id]['name']}, Cleaned: {'Yes' if rooms[room_id]['cleaned'] else 'No'}")
            move("F", 50)  # Move forward with power 50
            sleep(2)
            clean(room_id, rooms)
            rooms[room_id]['cleaned'] = True
            move("S", 0)  # Stop
            start_time = time()  # Start the timer
    return frame, start_time

# Function to clean the room
def clean(room_id, rooms):
    print("Cleaning the room...")
    # Implement cleaning logic
    if room_id == 1:
        # Suck in the living room
        suck(True, power=50)
    else:
        # Sweep in other rooms
        sweep(True, power=50)
    # Integrate sensor-based cleaning logic
    clean(wet=True, blow=True, rotate=True)
    # Update room status
    rooms[room_id]['cleaned'] = True
    print("Room cleaned!")

# Function to check if the cleaning time has elapsed
def cleaning_timer_elapsed(start_time):
    elapsed_time = time() - start_time
    return elapsed_time >= 300  # 300 seconds = 5 minutes

# Main function
#def main():
    cap = cv2.VideoCapture(0)  # Use 0 for the default camera
    rooms = {
        1: {"name": "Living Room", "cleaned": False},
        2: {"name": "Kitchen", "cleaned": False},
        3: {"name": "Bedroom 1", "cleaned": False},
        4: {"name": "Bedroom 2", "cleaned": False},
        5: {"name": "Bathroom", "cleaned": False},
    }
    start_time = None  # Initialize start time
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to capture frame")
                break
            if start_time and cleaning_timer_elapsed(start_time):
                # Stop cleaning after 5 minutes
                move("S", 0)  # Stop cleaning
                start_time = None  # Reset start time
            else:
                frame_with_bbox, start_time = detect_and_draw(frame, rooms, start_time)
            cv2.imshow('QR Code Detection', frame_with_bbox)
            cv2.waitKey(1)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        cleanup_gpio()
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
