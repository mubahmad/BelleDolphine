import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin where the servo is connected
SERVO_PIN = 3

# Set up the GPIO pin for PWM (Pulse Width Modulation)
GPIO.setup(SERVO_PIN, GPIO.OUT)
pwm = GPIO.PWM(SERVO_PIN, 50)  # 50Hz PWM frequency

# Start PWM with a duty cycle of 0 (servo not moving)
pwm.start(0)

def set_servo_angle(servo_pin, angle):
    """Set the angle of the servo motor."""
    duty_cycle = 2 + (angle / 18)  # Convert angle to duty cycle
    pwm.ChangeDutyCycle(duty_cycle)
    time.sleep(1)  # Allow the servo to reach the position
    pwm.ChangeDutyCycle(0)

def move_servo_based_on_condition(condition):
    """Move servo to 90 degrees if condition is True, otherwise to 180 degrees."""
    if condition:
        set_servo_angle(SERVO_PIN, 120)
    else:
        set_servo_angle(SERVO_PIN, 190)

# Example usage with infinite loop
try:
    while True:
        move_servo_based_on_condition(True)
        time.sleep(1)  # Wait for 1 second
        move_servo_based_on_condition(False)
        time.sleep(1)  # Wait for 1 second
finally:
    pwm.stop()
    GPIO.cleanup()
