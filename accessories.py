import RPi.GPIO as GPIO

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


def suck(state, power):
    pwrB = GPIO.PWM(en_a, 100)  # Set PWM frequency to 100 Hz
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
    pwrS = GPIO.PWM(en_b, 100)
    pwrS.start(0)
    if state:
        pwrS.ChangeDutyCycle(power)  # Start sucking with the specified power
        GPIO.output(in3, GPIO.HIGH)
        print("sweep")
    else:
        pwrS.ChangeDutyCycle(0)  # Stop sucking
        GPIO.output(in3, GPIO.LOW)
        print("not sweeping")


def mop(state):
    srv = GPIO.PWM(servo_pin, 100)
    if state:  # Move to position 1 (e.g., True)
        srv.start(2.5)  # Duty cycle for position 1
    else:  # Move to position 2 (e.g., False)
        srv.start(7.5)  # Duty cycle for position 2
