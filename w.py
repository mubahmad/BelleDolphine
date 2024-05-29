import RPi.GPIO as GPIO
from clean import clean, scan

GPIO.setmode(GPIO.BCM)


def reset_gpio():
    GPIO.cleanup()


def start_task():
    scan()
    print("Start task")


def stop_task():
    print("Stop task")


def home_task():
    print("Home task")


def main(input):
    try:
        reset_gpio()
        GPIO.output((14, 15, 18, 23, 4, 17, 27, 13, 5, 6, 3, 24, 25, 7, 8), GPIO.LOW)
        while True:
            user_input = input

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
