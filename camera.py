import cv2
import picamera
from PIL import Image
from pytesser import *
#import pytesser

class Camera:
    IMAGE_FILE = 'image.jpg'
    cam = picamera.PiCamera()

    def detect(self):
        camera = self.cam
        while True:
            # load image
            camera.capture(self.IMAGE_FILE)
            img = Image.open(self.IMAGE_FILE)
            
            # detect words in image
            words = image_to_string(img).strip()
            #txt = pytesser.image_to_string(img,"eng",pytesser.PSM_SINGLE_CHAR)
            
            if words != '' or cv2.waitKey(1) & 0xFF == ord('q'):
                print words
                return words

        

