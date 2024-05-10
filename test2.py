import RPi.GPIO as GPIO
import time
from clean import clean

try:
    while True:
        clean(False, True, True)
except KeyboardInterrupt:
    print("Program terminated")
finally:
    GPIO.cleanup()  # Clean up all GPIO
