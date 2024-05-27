import RPi.GPIO as GPIO
import time
from picamera2.picamera2 import Picamera2
from clean import clean
from accessories import suck, sweep
from qrHandler import ratio_and_center_of_quadrilateral_area_to_image,getInRoom
from cameraHandler import grabFrame
from scan import scan , retval ,center,ratio
modeOfOperation=0
cleanTimes=0
try:
    firstTime=True
    camera = Picamera2()
    while True:
        if firstTime:
            try:                
                camera.start()  
                
                firstTime=False
            except:
                print('Camera could not start')
        if not firstTime:
            if modeOfOperation==0:
                modeOfOperation=scan(40,camera)
            elif modeOfOperation==1:
               modeOfOperation= getInRoom(retval,ratio,center)
            elif modeOfOperation==2:
                modeOfOperation= clean(True, True, False, 20)
                if cleanTimes>=50000:
                    modeOfOperation=0
            elif modeOfOperation==3:
                # home()
                print('home')
            
            
        
        # suck(True, 100)
        # sweep(True, 70)
        
except KeyboardInterrupt:
    print("Program terminated")
finally:
    camera.stop()
    GPIO.cleanup()  # Clean up all GPIO
