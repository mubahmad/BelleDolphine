import RPi.GPIO as GPIO
import random
from movement import move
import time
from accessories import mop, suck, sweep
from cameraHandler import grabFrame
from qrHandler import ratio_and_center_of_quadrilateral_area_to_image , getInRoom
from time import sleep
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
retval=-1
ratio=0.0
center=-1.0
def scan(speed,camera):


    frame=grabFrame(camera)
    retval, ratio, center = ratio_and_center_of_quadrilateral_area_to_image(frame)
    
    if retval:
        print('qr first')
        move('c',20)
        sleep(1)
        move('w',20)
        sleep(0.7)
        # while center>0.15 or center <-0.15:
        # # while False:    
        #     if center>0:
        #         print('going left')
        #         move('a',10)
        #     else:
        #         move('d',10)
        #         print('going right')
            
        #     frame=grabFrame(camera)
        #     while True:
        #         print(' loop')
        #         retval, ratio, center = ratio_and_center_of_quadrilateral_area_to_image(frame)
        #         if retval:
        #             print('qr in loop')
        #             break
        #     print(center)
        move('c',10)
        return 5
   
    
    else:
        return 4
        # print('no')
    # Check for cliff and collision
        # if (GPIO.input(cliff_pin)) or not GPIO.input(collision_C):
        #     print("moving backwards")
        #     move("s", 30)
        #     time.sleep(1)
        #     print("rotating")
        #     rotation_time = random.uniform(0.5,1.5)
        #     # Generate a random direction
        #     direction = random.choice(["a", "d"])
        #     move(direction, 30)
        #     time.sleep(rotation_time)
        #     print("stopped rotating")
        # elif not GPIO.input(collision_L):
        #     print("object in left")
        #     move("d", 30)
        # elif not GPIO.input(collision_R):
        #     print("object in right")
        #     move("a", 30)
        # else:
        #     print("clear")
        #     move("w", 10)
        return 0

# def scan():
#     # Check for cliff and collision
#     if (GPIO.input(cliff_pin)) or not GPIO.input(collision_C):
#         print("moving backwards")
#         move("s", 50)
#         time.sleep(2)
#         print("rotating")
#         rotation_time = random.uniform(1,4)
#         # Generate a random direction
#         direction = random.choice(["a", "d"])
#         move(direction, 50)
#         time.sleep(rotation_time)
#         print("stopped rotating")
#     elif not GPIO.input(collision_L):
#         print("object in left")
#         move("d", 50)
#     elif not GPIO.input(collision_R):
#         print("object in right")
#         move("a", 50)
#     else:
#         print("clear")
#         move("w", 50)