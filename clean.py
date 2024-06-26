import RPi.GPIO as GPIO
import random
from movement import move
import time
from accessories import mop, suck, sweep
# from test2 import modeOfOperation

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

def clean(blow, rotate, wet, speed):
    suck(blow, 100)
    sweep(rotate, 70)
    mop(wet)
    # Check for cliff and collision
    if (GPIO.input(cliff_pin)) or not GPIO.input(collision_C):
        print("moving backwards")
        move("s", speed)
        time.sleep(1)
        print("rotating")
        rotation_time = random.uniform(0.5,1.5)
        # Generate a random direction
        direction = random.choice(["a", "d"])
        move(direction, speed)
        time.sleep(rotation_time)
        print("stopped rotating")
    elif not GPIO.input(collision_L):
        print("object in left")
        move("d", speed+10)
    elif not GPIO.input(collision_R):
        print("object in right")
        move("a", speed+10)
    else:
        print("clear")
        move("w", speed)
    
    if GPIO.input(cliff_pin):
        move('c',4)
        suck(False, 100)
        sweep(False, 70)
        time.sleep(10)
        return 3
    else :
        return 2
    

def scam():
    # Check for cliff and collision
    if not GPIO.input(collision_C):
        print("moving backwards")
        move("s", 20)
        time.sleep(2)
        print("rotating")
        rotation_time = random.uniform(1,4)
        # Generate a random direction
        direction = random.choice(["a", "d"])
        move(direction, 20)
        time.sleep(rotation_time)
        print("stopped rotating")
    elif not GPIO.input(collision_L):
        print("object in left")
        move("d", 20)
    elif not GPIO.input(collision_R):
        print("object in right")
        move("a", 20)
    else:
        print("clear")
        move("w", 20)

    if GPIO.input(cliff_pin):
        move('c',4)
        suck(False, 100)
        sweep(False, 70)
        time.sleep(10)
        return 7
    else :
        return 6