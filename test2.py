import RPi.GPIO as GPIO
import time
from picamera2.picamera2 import Picamera2
from clean import clean , scam
from accessories import suck, sweep
from qrHandler import ratio_and_center_of_quadrilateral_area_to_image,getInRoom
from cameraHandler import grabFrame
from scan import scan , retval ,center,ratio
import json
from movement import move

modeOfOperation=1
cleanTimes=0

# scan example and write to state
s='state.example.json'
# d='state.json'
# with open(s, 'r') as f:
#     data = json.load(f)
    
#     # Write to the destination JSON file
# with open(d, 'w') as f:
#     json.dump(data, f, indent=4)

try:
    firstTime=True
    camera = Picamera2()
    while True:
        # with open(d, 'r') as f:
        #     data = json.load(f)
        # modeOfOperation = data.get('currentModeOfOperation', None)

        # if modeOfOperation!=2:  
         if True:  
            # instead of true check state.json number  
            if firstTime:
                try:                
                    # camera.start()  

                    firstTime=False
                except:
                    print('Camera could not start')
            if not firstTime:
                if modeOfOperation==0:
                    modeOfOperation=scan(20,camera)
                    
                elif modeOfOperation==1:
                #    get it running
                   move('s',20)
                   time.sleep(1)
                   move('d',50)
                   time.sleep(1)
                   move('w',20)
                   time.sleep(2)
                   move('c',20)
                   time.sleep(1)
                   move('a',50)
                   time.sleep(0.5)
                   move('w',20)
                   time.sleep(2)
                   move('d',50)
                   time.sleep(0.3)
                   modeOfOperation= 2

                   print("going in")
                elif modeOfOperation==2:
                    modeOfOperation= clean(True, True, False, 20)
                    # stop
                    # GPIO.cleanup()
                    print('cleaning')
                    # if cleanTimes>=50000:
                        # modeOfOperation=0
                elif modeOfOperation==3:
                    # home()
                    modeOfOperation= getInRoom()
                    print('home')
                elif modeOfOperation==4:
                    modeOfOperation=scan(20,camera)
                elif modeOfOperation ==5:
                    move('c',20)
                elif modeOfOperation ==6:
                    modeOfOperation=scam()
                elif modeOfOperation ==7:
                    move('w',20)
                    time.sleep(0.7)
                    move('c',20)
                    time.sleep(1)
                    move('a',10)
                    time.sleep(0.5)
                    move('d',10)
                    time.sleep(0.5)
                    move('w',20)
                    time.sleep(0.7)
                    modeOfOperation=5



        
        # suck(True, 100)
        # sweep(True, 70)
        
except KeyboardInterrupt:
    print("Program terminated")
finally:
    camera.stop()
    GPIO.cleanup()  # Clean up all GPIO
