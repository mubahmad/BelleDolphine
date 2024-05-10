import RPi.GPIO as GPIO
import time
from clean import scan

try:
    while True:
        scan()
except KeyboardInterrupt:
    print("Program terminated")
finally:
    GPIO.cleanup()  # Clean up all GPIO
