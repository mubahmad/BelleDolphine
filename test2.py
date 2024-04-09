import RPi.GPIO as GPIO
import time
from clean import clean

GPIO.setmode(GPIO.BCM)

# Assuming the IR sensor is connected to GPIO 23
cliff = 23
GPIO.setup(cliff, GPIO.IN)

try:
    while True:
        clean()
except KeyboardInterrupt:
    print("Program terminated")
finally:
    GPIO.cleanup()  # Clean up all GPIO
