import RPi.GPIO as GPIO
import time

# Set up GPIO using BCM numbering
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for the H-bridge
enb_pin = 7
in3_pin = 8

# Set up GPIO pins for the H-bridge
GPIO.setup(enb_pin, GPIO.OUT)
GPIO.setup(in3_pin, GPIO.OUT)

# Create PWM object for motor speed control
motor_pwm = GPIO.PWM(enb_pin, 100)  # PWM with frequency 100Hz


def sweep_motor():
    # Move the motor forward
    GPIO.output(in3_pin, GPIO.HIGH)

    # Start PWM with 50% duty cycle
    motor_pwm.start(50)


# Cleanup GPIO on exit
def cleanup():
    GPIO.cleanup()


# Example usage
while True:
    try:
        sweep_motor()
    except KeyboardInterrupt:
        cleanup()  # Cleanup GPIO on Ctrl+C
