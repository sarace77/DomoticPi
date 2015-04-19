#!/usr/bin/env python
import webiopi
import datetime

GPIO = webiopi.GPIO

rotary_list = []

class RotaryDevice:
    def __init__(self, clk, data, ms):
        self.clk = clk
        self.data = data
        self.ms = ms
        GPIO.setFunction(self.clk, GPIO.IN)
        GPIO.setFunction(self.data, GPIO.IN)
        GPIO.setFunction(self.ms, GPIO.IN)

    def isRotating(self):
        return not GPIO.digitalRead(self.clk)
    
    def isRotatingClockWise(self):
        return self.isRotating() and GPIO.digitalRead(self.data)
    
    def isRotatingAntiClockWise(self):
        return self.isRotating() and (not GPIO.digitalRead(self.data))

rotary_list = []

def setup():
    global rotary_list    
    rotary_list.append(RotaryDevice(17,27,22))    
    

def loop():    
    for i in range(0, len(rotary_list)) :
        if rotary_list[i].isRotatingClockWise() :
            print "Rotary:", i, "Step +" 
        elif rotary_list[i].isRotatingAntiClockWise() :
            print "Rotary:", i, "Step -"
            
    webiopi.sleep(0.1) 

def destroy():
    print "Destroy"