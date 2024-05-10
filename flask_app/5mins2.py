import cv2
import numpy as np
from time import time, sleep
import RPi.GPIO as GPIO
import random


en_a = 4
in1 = 17
in2 = 27
en_b = 13
in3 = 5
in4 = 6


blower_en = 24
blower_in = 25
sweeper_en = 7
sweeper_in = 8


# Initialize GPIO for movement, blower, and sweeper
def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1, GPIO.OUT)
    GPIO.setup(in2, GPIO.OUT)
    GPIO.setup(en_a, GPIO.OUT)
    GPIO.setup(in3, GPIO.OUT)
    GPIO.setup(in4, GPIO.OUT)
    GPIO.setup(en_b, GPIO.OUT)
    GPIO.setup(blower_in, GPIO.OUT)
    GPIO.setup(blower_en, GPIO.OUT)
    GPIO.setup(sweeper_in, GPIO.OUT)
    GPIO.setup(sweeper_en, GPIO.OUT)
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(blower_in, GPIO.LOW)
    GPIO.output(blower_en, GPIO.LOW)
    GPIO.output(sweeper_in, GPIO.LOW)
    GPIO.output(sweeper_en, GPIO.LOW)


# Function to move the robot
def move(direction, power):
    # Implement motor control logic
    try:
        pwrL = GPIO.PWM(en_a, 100)
        pwrR = GPIO.PWM(en_b, 100)
        pwrL.start(power)
        pwrR.start(power)
        if direction == "w":
            GPIO.output(in1, GPIO.HIGH)
            GPIO.output(in2, GPIO.LOW)
            GPIO.output(in3, GPIO.HIGH)
            GPIO.output(in4, GPIO.LOW)
        elif direction == "s":
            GPIO.output(in1, GPIO.LOW)
            GPIO.output(in2, GPIO.HIGH)
            GPIO.output(in3, GPIO.LOW)
            GPIO.output(in4, GPIO.HIGH)
        elif direction == "a":
            GPIO.output(in1, GPIO.HIGH)
            GPIO.output(in2, GPIO.LOW)
            GPIO.output(in3, GPIO.LOW)
            GPIO.output(in4, GPIO.HIGH)
        elif direction == "d":
            GPIO.output(in1, GPIO.LOW)
            GPIO.output(in2, GPIO.HIGH)
            GPIO.output(in3, GPIO.HIGH)
            GPIO.output(in4, GPIO.LOW)
        elif direction == "c":
            GPIO.output(in1, GPIO.LOW)
            GPIO.output(in2, GPIO.LOW)
            GPIO.output(in3, GPIO.LOW)
            GPIO.output(in4, GPIO.LOW)
    except KeyboardInterrupt:
        GPIO.cleanup()


# Cleanup GPIO
def cleanup_gpio():
    GPIO.cleanup()

# Function to detect and draw QR code bounding box
def detect_and_draw(frame, rooms):
    detector = cv2.QRCodeDetector()
    retval, points, straight_qrcode = detector.detectAndDecode(frame)
    if retval:
        room_id = int(retval)
        if room_id in rooms:
            points = np.array(points, dtype=np.int32)
            cv2.polylines(frame, [points], isClosed=True, color=(140, 255, 0), thickness=6)
            print(f"Room ID: {room_id}, Name: {rooms[room_id]['name']}, Cleaned: {'Yes' if rooms[room_id]['cleaned'] else 'No'}")
            move("F", power=50)  # Move forward with power 50
            sleep(2)
            clean(room_id, rooms)
            rooms[room_id]['cleaned'] = True
            move("S", power=0)  # Stop
    return frame

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
    sleep(2)
    print("Room cleaned!")
    # Your cleaning logic here, e.g., based on your provided code

# Function to control the blower (sucking)
def suck(x, power):
    pwrB = GPIO.PWM(blower_en, 100)  # Set PWM frequency to 100 Hz
    pwrB.start(0)  # Initialize with 0 power to stop sucking
    if x:
        pwrB.ChangeDutyCycle(power)  # Start sucking with the specified power
        GPIO.output(blower_in, GPIO.HIGH)
        print("Sucking...")
    else:
        pwrB.ChangeDutyCycle(0)  # Stop sucking
        GPIO.output(blower_in, GPIO.LOW)
        print("Not sucking")

# Function to control the sweeper
def sweep(x, power):
    pwrS = GPIO.PWM(sweeper_en, 100)
    pwrS.start(0)
    if x:
        pwrS.ChangeDutyCycle(power)  # Start sweeping with the specified power
        GPIO.output(sweeper_in, GPIO.HIGH)
        print("Sweeping...")
    else:
        pwrS.ChangeDutyCycle(0)  # Stop sweeping
        GPIO.output(sweeper_in, GPIO.LOW)
        print("Not sweeping")

# Main function
def main():
    setup_gpio()
    cap = cv2.VideoCapture(0)  # Use 0 for the default camera
    rooms = {
        1: {"name": "Living Room", "cleaned": False},
        2: {"name": "Kitchen", "cleaned": False},
        3: {"name": "Bedroom 1", "cleaned": False},
        4: {"name": "Bedroom 2", "cleaned": False},
        5: {"name": "Bathroom", "cleaned": False},
    }
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to capture frame")
                break
            frame_with_bbox = detect_and_draw(frame, rooms)
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
