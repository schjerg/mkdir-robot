from picamera import PiCamera
import time

camera = PiCamera()              # Initialize a camera object
#camera.resolution = (1024, 768) # Set the image resolution.
#camera.rotation = 180           # If your image is upside down, rotate it.
camera.start_preview()
time.sleep(2)                    # Camera warm-up time.
camera.capture('test.jpg')       # Specify image filename
camera.stop_preview()