import RPi.GPIO as GPIO
import time
from clean import clean
from accessories import suck, sweep
try:
    while True:
        # suck(True, 100)
        # sweep(True, 70)
        
        clean(True, True, False, 20)
except KeyboardInterrupt:
    print("Program terminated")
finally:
    GPIO.cleanup()  # Clean up all GPIO
