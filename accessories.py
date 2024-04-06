import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

# Blower
en_a = 24
in1 = 25
# Sweeper
en_b = 7
in3 = 8

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(en_a, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(en_b, GPIO.OUT)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)

def suck (x, power):
   try:
      
   # Create Infinite loop to read user input
      while(x):
         # Get user Input
            pwrB = GPIO.PWM(en_a, 100)
            pwrB.start(power)
         # To see users input
         # print(user_input) 
            GPIO.output(in1, GPIO.HIGH)
            print("Forward")
      GPIO.output(in1, GPIO.LOW)
    # If user press CTRL-C
   except KeyboardInterrupt:
          # Reset GPIO settings
         GPIO.cleanup()
         print("GPIO Clean up")


def sweep (x, power):
   try:
      
   # Create Infinite loop to read user input
      while(x):
         # Get user Input
            pwrS = GPIO.PWM(en_b, 100)
            pwrS.start(power)
         # To see users input
         # print(user_input) 
            GPIO.output(in3, GPIO.HIGH)
            print("Forward")
      GPIO.output(in3, GPIO.LOW)
    # If user press CTRL-C
   except KeyboardInterrupt:
          # Reset GPIO settings
         GPIO.cleanup()
         print("GPIO Clean up")
