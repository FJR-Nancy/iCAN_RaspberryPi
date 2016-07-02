import motor
import camera

motor.init()

if camera.detect()=='146':
    motor.forwards()
elif camera.detect()=='289':
    motor.backwards()
elif camera.detect()=='367':
    motor.stop()
    
motor.exit()
