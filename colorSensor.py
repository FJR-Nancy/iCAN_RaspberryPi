import Adafruit_TCS34725
import smbus
import math

class ColorSensor:
    tcs = Adafruit_TCS34725.TCS34725()
    redThres = 15
    greenThres = 50
    
    
    def checkLight(self):
        tcs = self.tcs
        r, g, b, c = tcs.get_raw_data()
        #print('Color: red={0} green={1} blue={2} clear={3}'.format(r, g, b, c))

        r = float(r)/c *256
        g = float(g)/c *256
        b = float(b)/c *256
        #print " R: %s, G: %s, B: %s" % (r, g, b)

        h = math.acos((r-g+r-b)/(2*math.sqrt((r-g)*(r-g)+(r-b)*(g-b))))/math.pi*180
        #print " H: %s " % h

        if(h < self.redThres):
            light =  'r'
            #print "Red light"
        elif(h > self.redThres and h < self.greenThres):
            light = 'n'
        else:
            light = 'g'
            #print "Green light"

        #print "\n"
        return light

