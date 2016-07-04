import motor
import colorSensor
import camera
from time import sleep

mot = motor.Motor()
mot.init()

colSen = colorSensor.ColorSensor()
cam = camera.Camera()

mot.forwards()
time = 0

while time < 5:
    #mot.forwards()
    light = colSen.checkLight()
    if light == 'r':
        mot.stop()
        words = cam.detect()
        if words =='146':
            mot.backwards()
        elif words =='289':
            mot.left()
        elif words=='367':
            mot.right()
        sleep(1)
        time = time + 1

        light = colSen.checkLight()
        if light == 'g':
            mot.forwards()
            sleep(1)
            time = time + 1 
    
mot.stop()    
mot.exit()
