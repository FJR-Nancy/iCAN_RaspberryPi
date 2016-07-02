import cv2
from pytesser import *
from PIL import Image
from time import sleep

IMAGE_FILE = 'mister_fruits.jpg'

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

rval, frame = vc.read()

while True:

  if frame is not None:
     cv2.imshow("preview", frame)
     cv2.imwrite(IMAGE_FILE, frame)
     # load image
     img = Image.open(IMAGE_FILE)

     # detect words in image
     words = image_to_string(img).strip()
     print words

  rval, frame = vc.read()

  if cv2.waitKey(1) & 0xFF == ord('q'):
     break

  sleep(5)