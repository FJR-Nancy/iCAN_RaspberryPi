import motor
import colorSensor
import camera
from time import sleep

def route(num):
    mot = motor.Motor()
    mot.init()

    colSen = colorSensor.ColorSensor()
    cam = camera.Camera()

    while colSen.checkLight() != 'g':
        sleep(1)

    mot.forwards()

    while True:
        light = colSen.checkLight()
        if light == 'r':
            mot.stop()
            words = int(cam.detect())
            if words < num:
                mot.forwards()
            elif words > num:
                mot.backwards()            
            elif words == num:
                mot.left()
                sleep(1)
                print "Destination reached"   
                break
    mot.stop()    
    mot.exit()
