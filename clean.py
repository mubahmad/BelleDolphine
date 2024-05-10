import RPi.GPIO as GPIO
import random
from movement import move
from accessories import mop, suck, sweep

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
    return random.uniform(20, 150)


def clean(wet, blow, rotate):
    mop(wet)
    suck(blow, 100)
    sweep(rotate, 70)
    # Check for cliff and collision
    if (GPIO.input(cliff_pin)) or not GPIO.input(collision_C):
        move("c", 50)
        # move("s", 50)
        # time.sleep(0.5)
        # move("c", 50)  # Stop the robot
        rotation_time = random_rotation_time()
        # Generate a random direction
        direction = random.choice(["a", "d"])
        move(direction, 50)
        # time.sleep(rotation_time)
    elif not GPIO.input(collision_L):
        print("object in left")
        move("d", 50)
    elif not GPIO.input(collision_R):
        print("object in right")
        move("a", 50)
    else:
        print("clear")
        move("w", 50)
