import RPi.GPIO as GPIO
import time
import random
from movement import move

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
cliff_pin = 23
collision_R = 14
collision_C = 15
collision_L = 18
GPIO.setup(cliff_pin, GPIO.IN)
GPIO.setup(collision_R, GPIO.IN)
GPIO.setup(collision_C, GPIO.IN)
GPIO.setup(collision_L, GPIO.IN)


# Function to generate random rotation time
def random_rotation_time():
    return random.uniform(0.2, 1.5)


# Main loop
def clean():
    # Check for cliff and collision
    if not (GPIO.input(cliff_pin)) or GPIO.input(collision_C):
        move("c", 50)
        move("s", 50)
        time.sleep(0.5)
        move("c", 50)  # Stop the robot
        rotation_time = random_rotation_time()
        # Generate a random direction
        direction = random.choice(["a", "d"])
        move(direction, 50)
        time.sleep(rotation_time)
    elif GPIO.input(collision_L):
        while GPIO.input(collision_L):
            move("d", 50)
    elif GPIO.input(collision_R):
        while GPIO.input(collision_R):
            move("a", 50)
    else:
        move("w", 70)