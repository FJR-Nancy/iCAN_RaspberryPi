import motor
import color
import camera
from time import sleep

mot = motor.Motor()
mot.init()

colSen = color.ColorSensor()
light = colSen.checkLight()

if light == 'r':
    mot.backwards()
    #mot.stop()
    sleep(1)
elif light == 'g':
    mot.forwards()
    sleep(1)

cam = camera.Camera()
words = cam.detect()

if words =='146':
    mot.backwards()
    sleep(1)
elif words =='289':
    mot.left()
    sleep(1)
elif words=='367':
    mot.right()
    sleep(1)
    
mot.stop()    
mot.exit()
