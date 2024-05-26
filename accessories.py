import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

# Blower
en_a = 24
in1 = 25
# Sweeper
en_b = 7
in3 = 8

# Servo
servo_pin = 3

GPIO.setmode(GPIO.BCM)

GPIO.setup(in1, GPIO.OUT)
GPIO.setup(en_a, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(en_b, GPIO.OUT)
GPIO.setup(servo_pin, GPIO.OUT)

GPIO.output(in1, GPIO.LOW)
GPIO.output(in3, GPIO.LOW)
GPIO.PWM(servo_pin, 50).start(0)

pwrB = GPIO.PWM(en_a, 100)  # Set PWM frequency to 100 Hz
pwrS = GPIO.PWM(en_b, 100)  # Set PWM frequency to 100 Hz
pwmSRV = GPIO.PWM(servo_pin, 50) #servo frequency



def suck(state, power):
    pwrB.start(0)  # Initialize with 0 power to stop sucking

    if state:
        pwrB.ChangeDutyCycle(power)  # Start sucking with the specified power
        GPIO.output(in1, GPIO.HIGH)
        print("sucking")
    else:
        pwrB.ChangeDutyCycle(0)  # Stop sucking
        GPIO.output(in1, GPIO.LOW)
        print("not sucking")

def sweep(state, power):
    pwrS.start(0)  # Initialize with 0 power to stop sucking

    if state:
        pwrS.ChangeDutyCycle(power)  # Start sucking with the specified power
        GPIO.output(in3, GPIO.HIGH)
        print("sweeping")
    else:
        pwrS.ChangeDutyCycle(0)  # Stop sucking
        GPIO.output(in3, GPIO.LOW)
        print("not sweeping")


def set_servo_angle(servo_pin, angle):
    """Set the angle of the servo motor."""
    duty_cycle = 2 + (angle / 18)  # Convert angle to duty cycle
    pwmSRV.ChangeDutyCycle(duty_cycle)
    pwmSRV.ChangeDutyCycle(0)

def mop(condition):
    """Move servo to 90 degrees if condition is True, otherwise to 180 degrees."""
    if condition:
        set_servo_angle(servo_pin, 120)
    else:
        set_servo_angle(servo_pin, 190)