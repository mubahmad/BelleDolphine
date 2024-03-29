import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

power = 100
speed = 0.073
travelRatio = power*speed/100

# Right Motor
in1 = 17
in2 = 27
en_a = 4
# Left Motor
in3 = 5
in4 = 6
en_b = 13


GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(en_a,GPIO.OUT)

GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en_b,GPIO.OUT)

pwrL=GPIO.PWM(en_a,100)
pwrR=GPIO.PWM(en_b,100)
pwrL.start(75)
pwrR.start(75)

GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
GPIO.output(in3,GPIO.LOW)





def move (x):
   

# Wrap main content in a try block so we can  catch the user pressing CTRL-C and run the
# GPIO cleanup function. This will also prevent the user seeing lots of unnecessary error messages.
   try:
   # Create Infinite loop to read user input
      while(True):
         # Get user Input
         

         # To see users input
         # print(user_input)

         if x == 'w':
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)

            GPIO.output(in3,GPIO.HIGH)
            GPIO.output(in4,GPIO.LOW)

            print("Forward")

            sleep (2)

            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.LOW)

         elif x == 's':
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)

            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.HIGH)
            print('Back')

            sleep (2)

            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.LOW)

         elif x == 'd':
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)

            GPIO.output(in3,GPIO.HIGH)
            GPIO.output(in4,GPIO.LOW)
            print('Right')

            sleep (0.5)

            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.LOW)

         elif x == 'a':
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)

            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.HIGH)
            print('Left')
            
            sleep (0.5)

            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.LOW)

         # Press 'c' to exit the script
         elif x == 'c':
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.LOW)

            GPIO.output(in4,GPIO.LOW)
            GPIO.output(in3,GPIO.LOW)
            print('Stop')

   # If user press CTRL-C
   except KeyboardInterrupt:
   # Reset GPIO settings
    GPIO.cleanup()
   print("GPIO Clean up")
