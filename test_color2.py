import motor
import colorSensor
import camera
from time import sleep

mot = motor.Motor()
mot.init()

colSen = colorSensor.ColorSensor()

while True:
    sleep(1)
    light = colSen.checkLight()
    '''
    if light == 'r':
        #mot.backwards()
        mot.stop()      
    elif light == 'g':
        mot.forwards()
    '''
