from picamera2.picamera2 import Picamera2
import cv2

camera = Picamera2()
camera.start()

print("starting")

i = 0 
while True:
    frame = camera.capture_array()
    cv2.imwrite(f"./images/img{i}.png", frame)
    if cv2.waitKey(10) == ord("q"):
        break
    i += 1

camera.stop()