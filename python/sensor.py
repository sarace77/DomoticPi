#!/usr/bin/env python
import webiopi
import datetime
import Adafruit_DHT

GPIO = webiopi.GPIO

class ExtSensorDHT11:
    def __init__(self, pin):
        self.sensor = Adafruit_DHT.DHT11
        self.pin = pin
        self.type = "humidity"


class RGBLed:
    def __init__(self, redPin, greenPin, bluePin):
        self.redPin = redPin
        self.greenPin = greenPin
        self.bluePin = bluePin
        GPIO.setFunction(redPin, GPIO.OUT)
        GPIO.setFunction(greenPin, GPIO.OUT)
        GPIO.setFunction(bluePin, GPIO.OUT)
        GPIO.digitalWrite(self.redPin, GPIO.LOW)
        GPIO.digitalWrite(self.greenPin, GPIO.LOW)
        GPIO.digitalWrite(self.bluePin, GPIO.LOW)

    def redOn(self):
        GPIO.digitalWrite(self.redPin, GPIO.HIGH)

    def redOff(self):
        GPIO.digitalWrite(self.redPin, GPIO.LOW)

    def greenOn(self):
        GPIO.digitalWrite(self.greenPin, GPIO.HIGH)

    def greenOff(self):
        GPIO.digitalWrite(self.greenPin, GPIO.LOW)

    def blueOn(self):
        GPIO.digitalWrite(self.bluePin, GPIO.HIGH)

    def blueOff(self):
        GPIO.digitalWrite(self.bluePin, GPIO.LOW)


class SensorDevice:
    def __init__(self):
        self.meteo = webiopi.deviceInstance("bmp") 
        self.type = "meteo"


leds_list = []
sensors_list = []

dht_temperature = 0
humidity = 0

previous_s = 0

        
def setup():
    global humidity
    global leds_list
    global sensors_list

    sensors_list.append(SensorDevice())
    sensors_list.append(ExtSensorDHT11(19))        
    
    leds_list.append(RGBLed(12,16,20))
    for i in range(0, len(leds_list)) :
        leds_list[i].redOn()
        webiopi.sleep(0.1)
        leds_list[i].greenOn()
        webiopi.sleep(0.1)
        leds_list[i].blueOn()
        webiopi.sleep(0.1)
        leds_list[i].blueOff()
        webiopi.sleep(0.1)
        leds_list[i].greenOff()
        webiopi.sleep(0.1)
        leds_list[i].redOff()
    

def loop():
    global dht_temperature
    global humidity
    global leds_list
    global previous_s
    global sensors_list


    now = datetime.datetime.now()
    now_s = now.hour * 3600 + now.minute * 60 + now.second
    
    pressure_list = []
    temperature_list = []
       
    for i in range(0, len(sensors_list)):
        if sensors_list[i].type == "meteo":
            pressure_list.append(sensors_list[i].meteo.getHectoPascal())
            temperature_list.append(sensors_list[i].meteo.getCelsius())
        elif sensors_list[i].type == "humidity":
            if (now_s - previous_s) >= 300:
                humidity, dht_temperature = Adafruit_DHT.read_retry(sensors_list[i].sensor, sensors_list[i].pin)
                previous_s = now_s


    if float(temperature_list[0]) >= 15.0 and float(temperature_list[0]) <= 25.0 : 
        leds_list[0].greenOn()
    else :
        leds_list[0].greenOff() 

    if float(temperature_list[0]) >= 24.0 :
        leds_list[0].redOn()
    else :
        leds_list[0].redOff() 

    if float(temperature_list[0]) <= 21.0 :
        leds_list[0].blueOn()
    else :
        leds_list[0].blueOff() 

    webiopi.sleep(0.5)

def destroy():
    for i in range(0, len(leds_list)) :
        leds_list[i].blueOff()
        leds_list[i].greenOff()
        leds_list[i].redOff()



@webiopi.macro
def getHumidity():
    global humidity
    if humidity is not None:
        return humidity
    else:
        return "None"



