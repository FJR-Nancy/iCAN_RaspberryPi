import motor
from time import sleep

mot = motor.Motor()
mot.init()

mot.forwards()
sleep(1)

mot.backwards()
sleep(1)

mot.left()
sleep(1)

mot.right()
sleep(1)

mot.stop()
mot.exit()
