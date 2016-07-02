import cv2
from PIL import Image
from pytesser import *
from speech import Speech
from time import sleep

speech = Speech()

IMAGE_FILE = 'mister_fruits.jpg'

# loop forever
while True:

    # save image from webcam
    img = cv2.VideoCapture(0).read()[1]
    cv2.imwrite(IMAGE_FILE, img)

    # load image
    img = Image.open(IMAGE_FILE)

    # detect words in image
    words = image_to_string(img).strip()
    print words

    # annouce the arrival of Mr Puce!
    if (words == 'Mr Puce'):
        speech.text_to_speech("Watch out, here comes Mr Puce")

    sleep(5)