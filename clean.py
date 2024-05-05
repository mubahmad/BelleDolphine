import RPi.GPIO as GPIO
import time
import random
from movement import move

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)
cliff_pin = 23
collision_pin = 24
GPIO.setup(cliff_pin, GPIO.IN)
GPIO.setup(collision_pin, GPIO.IN)


# Function to generate random rotation time
def random_rotation_time():
    return random.uniform(0.2, 1.5)

# Main loop

# Check for cliff and collision
if GPIO.input(cliff_pin) or GPIO.input(collision_pin):
    move('c')
    move('s')
    time.sleep(0.5)
    move('c')  # Stop the robot
    rotation_time = random_rotation_time()
    # Generate a random direction
    direction = random.choice(['a', 'd'])
    move(direction)
    time.sleep(rotation_time)
else:
    move('w')

