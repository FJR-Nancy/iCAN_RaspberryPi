import smbus
import math

class ColorSensor:
    redThres = 20
    greenThres = 50
    
    bus = smbus.SMBus(1)
    # I2C address 0x29
    # Register address must be  OR'ed with 0x80
    bus.write_byte(0x29,0x80|0x12)
    ver = bus.read_byte(0x29)
    
    def checkLight(self):
        bus = self.bus
        # version # should be 0x44
        if self.ver != 0x44:
            print "Device not found\n"

        else:
            print "Device found\n"

            data = bus.read_i2c_block_data(0x29, 0)
            clear = data[1] << 8 | data[0]
            red = data[3] << 8 | data[2]
            green = data[5] << 8 | data[4]
            blue = data[7] << 8 | data[6]
            crgb = "C: %s, R: %s, G: %s, B: %s\n" % (clear, red, green, blue)
            print crgb

            sumrgb = red + green + blue
            r = float(red)/sumrgb *256
            g = float(green)/sumrgb *256
            b = float(blue)/sumrgb *256
            print " R: %s, G: %s, B: %s \n" % (r, g, b)

            h = math.acos((r-g+r-b)/(2*math.sqrt((r-g)*(r-g)+(r-b)*(g-b))))/math.pi*180
            print " H: %s \n" % h

            if(h < self.redThres):
                light =  'r'
                print "Red light"
            elif(h > self.redThres and h < self.greenThres):
                light = 'n'
            else:
                light = 'g'
                print "Green light"

            return light

