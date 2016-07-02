import cv2
import picamera
from PIL import Image
from pytesser import *

def detect():
    IMAGE_FILE = 'image.jpg'

    camera = picamera.PiCamera()
    camera.capture(IMAGE_FILE)

    while True:
        # load image
        img = Image.open(IMAGE_FILE)
        
        # detect words in image
        words = image_to_string(img).strip()
        print words
        
        camera.capture(IMAGE_FILE)
        
        if words != '' or cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    return words

