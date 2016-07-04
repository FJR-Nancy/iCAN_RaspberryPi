import cv2
import picamera
from PIL import Image
from pytesser import *
from time import sleep

IMAGE_FILE = 'image.jpg'

camera = picamera.PiCamera()
camera.capture(IMAGE_FILE)

#cv2.namedWindow("preview")
#vc = cv2.VideoCapture(0)

while True:

    #cv2.imshow("preview", frame)
    #cv2.imwrite(IMAGE_FILE, frame)

    # load image
    img = Image.open(IMAGE_FILE)
    
    # detect words in image
    words = image_to_string(img).strip()
    print words
    
    camera.capture(IMAGE_FILE)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    sleep(5)

