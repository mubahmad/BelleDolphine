import RPi.GPIO as GPIO
import random
from movement import move
import time
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

def clean(wet, blow, rotate):
    mop(wet)
    # suck(blow, 100)
    # sweep(rotate, 70)
    # Check for cliff and collision
    if (GPIO.input(cliff_pin)) or not GPIO.input(collision_C):
        print("moving backwards")
        move("s", 50)
        time.sleep(2)
        print("rotating")
        rotation_time = random.uniform(1,4)
        # Generate a random direction
        direction = random.choice(["a", "d"])
        move(direction, 50)
        time.sleep(rotation_time)
        print("stopped rotating")
    elif not GPIO.input(collision_L):
        print("object in left")
        move("d", 50)
    elif not GPIO.input(collision_R):
        print("object in right")
        move("a", 50)
    else:
        print("clear")
        move("w", 10)

def scan():
    # Check for cliff and collision
    if (GPIO.input(cliff_pin)) or not GPIO.input(collision_C):
        print("moving backwards")
        move("s", 50)
        time.sleep(2)
        print("rotating")
        rotation_time = random.uniform(1,4)
        # Generate a random direction
        direction = random.choice(["a", "d"])
        move(direction, 50)
        time.sleep(rotation_time)
        print("stopped rotating")
    elif not GPIO.input(collision_L):
        print("object in left")
        move("d", 50)
    elif not GPIO.input(collision_R):
        print("object in right")
        move("a", 50)
    else:
        print("clear")
        move("w", 50)