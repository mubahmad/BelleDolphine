import RPi.GPIO as GPIO
from time import sleep, time
import cv2 as cv
import numpy as np
from movement import move
from clean import clean

# GPIO pin definitions for movement
# Define your motor pins here

# motor1_pin1 = ...
# motor1_pin2 = ...
# motor2_pin1 = ...
# motor2_pin2 = ...

# Initialize GPIO for movement
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# Setup motor pins as output
# ...

# Initialize video capture for QR code detection
cap = cv.VideoCapture(0)  # Use 0 for the default camera

#Remeber to add the ir sensors readings 

rooms = {
    1: {"name": "Living Room", "cleaned": False},
    2: {"name": "Kitchen", "cleaned": False},
    3: {"name": "Bedroom 1", "cleaned": False},
    4: {"name": "Bedroom 2", "cleaned": False},
    5: {"name": "Bathroom", "cleaned": False},
    
}


def move_towards_door(x):
    if x == 'F':
        move(x) # to move Forward
        sleep(2)
    elif x == 'R':
        move(x) # to move Right
        sleep(2)
    elif x == 'L':
        move(x) # to move Left
        sleep(2)
    elif x == 'B':
        move(x) # to move Backward
        sleep(2)
    else:
        move(x) # stops    




# def clean(x):
#     if x == 'F':
#         move(x)  # to move Forw  
#     elif x == 'R':
#         move(x)  # to move Right
#         sleep(2)
#     elif x == 'L':
#         move(x)  # to move Left
#         sleep(2)
#     elif x == 'B':
#         move(x)  # to move Backward
#         sleep(2)
#     else:
#         move("S")  # stops
#     print("Cleaning the room...")
#     sleep(2)
#     print("Room cleaned!")



# Function to detect and draw QR code bounding box
def detect_and_draw(frame):
    # Create a QRCodeDetector object
    detector = cv.QRCodeDetector()
    
    # Detect and decode QR code
    retval, points, straight_qrcode = detector.detectAndDecode(frame)
    
    # Check if QR code is detected
    if retval:
        room_id = int(retval)
        if room_id in rooms:
            # Convert points to integers
            points = np.array(points, dtype=np.int32)
            
            # Draw bounding box around the QR code
            cv.polylines(frame, [points], isClosed=True, color=(140, 255, 0), thickness=6)
            
            # Display room information
            print("Room ID:", room_id)
            print("Room Name:", rooms[room_id]["name"])
            print("Cleaned:", "Yes" if rooms[room_id]["cleaned"] else "No")
            
            # Move towards the detected door
            move_towards_door("F")  # to move forward
            
            # Clean the room
            while check_time_to_look_again():
                clean()
            
            # Set the cleaned status to True
            rooms[room_id]["cleaned"] = True
            
            # Stop the robot after cleaning
            move_towards_door("S")
    
    return frame

# Function to check if it's time to look for the same QR code again
def check_time_to_look_again():
    current_time = time()
    for room_id, room_info in rooms.items():
        last_cleaned_time = room_info.get("last_cleaned_time", 0)
        if current_time - last_cleaned_time >= 300:  # 300 seconds = 5 minutes
            return True
    return False




# Main function
def main():
    try:
        while True:
            # Capture frame-by-frame for QR code detection
            ret, frame = cap.read()
            if not ret:
                print("Failed to capture frame")
                break

            # Detect and draw QR code bounding box
            frame_with_bbox = detect_and_draw(frame)

            # Display the resulting frame for QR code detection
            cv.imshow('QR Code Detection', frame_with_bbox)
            cv.waitKey(1)  # Required for imshow to work properly

            # Check if it's time to look for the same QR code again
            if check_time_to_look_again():
                print("Looking for the same QR code again...")
                # Clear last_cleaned_time for all rooms
                for room_info in rooms.values():
                    room_info.pop("last_cleaned_time", None)
                # Reset the timer
                start_time = time()

            sleep(1)  # Pause for a moment before checking for door again
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        # Cleanup GPIO
        GPIO.cleanup()
        # Release video capture
        cap.release()
        cv.destroyAllWindows()

if _name_ == "_main_":
    main()