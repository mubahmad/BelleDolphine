import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)


def reset_gpio():
    GPIO.cleanup()


def start_task():
    print("Start task")


def stop_task():
    print("Stop task")


def home_task():
    print("Home task")


def main():
    try:
        reset_gpio()
        while True:
            user_input = input("Enter 'start', 'stop', or 'home': ").strip().lower()

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
