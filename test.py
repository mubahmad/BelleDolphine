import RPi.GPIO as GPIO
import time
from accessories import suck

GPIO.setmode(GPIO.BCM)

# Assuming the IR sensor is connected to GPIO 23
cliff = 23
GPIO.setup(cliff, GPIO.IN)

try:
    while True:
        if not GPIO.input(cliff):  # Assuming HIGH signal means IR is ON
            suck(True, 100)  # Replace 50 with the desired power level
        else:
            suck(False, 0)
except KeyboardInterrupt:
    print("Program terminated")
finally:
    suck.pwrB.stop()  # Stop the PWM
    GPIO.cleanup()  # Clean up all GPIO
