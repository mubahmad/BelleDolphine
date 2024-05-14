import RPi.GPIO as GPIO
from clean import clean

######## SETUP
GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)

GPIO.output(14, GPIO.LOW)
GPIO.output(15, GPIO.LOW)
GPIO.output(18, GPIO.LOW)
GPIO.output(23, GPIO.LOW)
GPIO.output(4, GPIO.LOW)
GPIO.output(17, GPIO.LOW)
GPIO.output(27, GPIO.LOW)
GPIO.output(13, GPIO.LOW)
GPIO.output(5, GPIO.LOW)
GPIO.output(6, GPIO.LOW)
GPIO.output(3, GPIO.LOW)
GPIO.output(24, GPIO.LOW)
GPIO.output(25, GPIO.LOW)
GPIO.output(7, GPIO.LOW)
GPIO.output(8, GPIO.LOW)


####### Functions

def reset_gpio():
    GPIO.cleanup()


def start_task():
    clean(True, True, False, 20)
    print("Start task")


def stop_task():
    print("Stop task")


def home_task():
    print("Home task")


def main():
    try:
        reset_gpio()
        while True:
            user_input = input("Enter 'start', 'stop', or 'home': ")

            if user_input == "start":
                start_task()
            elif user_input == "stop":
                stop_task()
            elif user_input == "home":
                home_task()
            else:
                print("Invalid input. Please enter 'start', 'stop', or 'home'.")

    except KeyboardInterrupt:
        reset_gpio()


if __name__ == "__main__":
    main()
