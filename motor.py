import RPi.GPIO as GPIO

class Motor:
    motor1A = 18
    motor1B = 16
    motor1E = 22

    motor2A = 23
    motor2B = 21
    motor2E = 19

    gpio = GPIO
        
    def init(self):
        gpio = self.gpio
        gpio.setmode(GPIO.BOARD)
        gpio.setup(self.motor1A,GPIO.OUT)
        gpio.setup(self.motor1B,GPIO.OUT)
        gpio.setup(self.motor1E,GPIO.OUT)

        gpio.setup(self.motor2A,GPIO.OUT)
        gpio.setup(self.motor2B,GPIO.OUT)
        gpio.setup(self.motor2E,GPIO.OUT)

    def forwards(self):
        gpio = self.gpio
        gpio.output(self.motor1A,GPIO.HIGH)
        gpio.output(self.motor1B,GPIO.LOW)
        gpio.output(self.motor1E,GPIO.HIGH)

        gpio.output(self.motor2A,GPIO.HIGH)
        gpio.output(self.motor2B,GPIO.LOW)
        gpio.output(self.motor2E,GPIO.HIGH)
        print "Going forwards"

    def backwards(self):
        gpio = self.gpio
        gpio.output(self.motor1A,GPIO.LOW)
        gpio.output(self.motor1B,GPIO.HIGH)
        gpio.output(self.motor1E,GPIO.HIGH)

        gpio.output(self.motor2A,GPIO.LOW)
        gpio.output(self.motor2B,GPIO.HIGH)
        gpio.output(self.motor2E,GPIO.HIGH)
        print "Going backwards"

    def left(self):
        gpio = self.gpio
        gpio.output(self.motor1A,GPIO.HIGH)
        gpio.output(self.motor1B,GPIO.LOW)
        gpio.output(self.motor1E,GPIO.HIGH)

        gpio.output(self.motor2A,GPIO.LOW)
        gpio.output(self.motor2B,GPIO.LOW)
        gpio.output(self.motor2E,GPIO.LOW)
        print "Turn left"
        
    def right(self):
        gpio = self.gpio
        gpio.output(self.motor1A,GPIO.LOW)
        gpio.output(self.motor1B,GPIO.LOW)
        gpio.output(self.motor1E,GPIO.LOW)

        gpio.output(self.motor2A,GPIO.HIGH)
        gpio.output(self.motor2B,GPIO.LOW)
        gpio.output(self.motor2E,GPIO.HIGH)
        print "Turn right"

    def stop(self):
        gpio = self.gpio
        gpio.output(self.motor1E,GPIO.LOW)
        gpio.output(self.motor2E,GPIO.LOW)
        print "Now stop"

    def exit(self):
        gpio = self.gpio
        gpio.cleanup()


