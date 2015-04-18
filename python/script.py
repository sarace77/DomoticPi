#!/usr/bin/env python
import webiopi
import datetime
import Adafruit_DHT

GPIO = webiopi.GPIO

devices_list = []
sensors_list = []
timers_list = []

all_status = ""

all_on = False
all_off = False

manual_disable_timers = True

dht_temperature = 0
humidity = 0
previous_s = 0

class ExtSensorDHT11:
    def __init__(self, pin):
        self.sensor = Adafruit_DHT.DHT11
        self.pin = pin
        self.type = "humidity"


class DeviceTimer:
    def __init__(self, index = -1, start = 0, stop = 0, enabled = False):
        self.index = index
        self.start = start
        self.stop = stop
        self.enabled = enabled

class SensorDevice:
    def __init__(self):
        self.meteo = webiopi.deviceInstance("bmp") 
        self.type = "meteo"

class SwitchDevice:
    def __init__(self, name="dispositivo", pin = 0, status = False):
        self.name = name
        self.pin = pin
        self.status = status
        GPIO.setFunction(self.pin, GPIO.OUT)
        if self.status:
            self.switchOn()
        else :
            self.switchOff()
    
    def switchOn(self):
        GPIO.digitalWrite(self.pin, GPIO.LOW)
        self.status = True
    
    def switchOff(self):
        GPIO.digitalWrite(self.pin, GPIO.HIGH)
        self.status = False
            
    def toggle(self):
        if self.status:
            self.switchOff()
        else :
            self.switchOn()
            
            
def setup():
    global devices_list
    global humidity
    global sensors_list
    global timers_list

    devices_list.append(SwitchDevice("Relay 0", 18, False))
    devices_list.append(SwitchDevice("Relay 1", 23, False))
    devices_list.append(SwitchDevice("Relay 2", 24, False))
    devices_list.append(SwitchDevice("Relay 3", 25, False))
    
    sensors_list.append(SensorDevice())
    sensors_list.append(ExtSensorDHT11(19))        
    
    timers_list.append(DeviceTimer(0, 43200, 64800))
    timers_list.append(DeviceTimer(1, 43200, 64800))
    timers_list.append(DeviceTimer(2, 43200, 64800))
    timers_list.append(DeviceTimer(3, 43200, 64800))   
   
    for j in range(0,2):
        for i in range(0,len(devices_list)) :
            devices_list[i].toggle()
            webiopi.sleep(0.1)
        webiopi.sleep(0.1)


def loop():
    global all_off
    global all_on
    global all_status
    global devices_list
    global dht_temperature
    global humidity
    global previous_s
    global sensors_list
    global timers_list   

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
                print ((now_s - previous_s), ":", humidity, dht_temperature)

    if all_on and not all_off:
        all_status = "On"
        for i in range(0, len(devices_list)) :
            if not devices_list[i].status:
                devices_list[i].switchOn()
    elif not all_on and all_off:    
        all_status = "Off"
        for i in range(0, len(devices_list)) :
            if devices_list[i].status:
                devices_list[i].switchOff()
    else:
        all_status = "Unknown"
        for i in range(0, len(timers_list)) :
            if timers_list[i].index >= 0 and timers_list[i].index < len(devices_list):
                if timers_list[i].enabled and now_s >= timers_list[i].start and now_s < timers_list[i].stop:
                    devices_list[timers_list[i].index].switchOn()
                elif timers_list[i].enabled and (now_s < timers_list[i].start or now_s >= timers_list[i].stop):
                    devices_list[timers_list[i].index].switchOff()

    
    for i in range(0, len(devices_list)) :
        if i == 0 :
            all_on = devices_list[i].status
            all_off = not devices_list[i].status
        all_on = all_on and devices_list[i].status
        all_off = all_off and (not devices_list[i].status)

                    
def destroy():
    for i in range(0, len(devices_list)) :
        devices_list[i].switchOff()
        

@webiopi.macro
def addTimer(dispositivo, start, stop, status):
    global devices_list
    global timers_list
    index_dispositivo = int(dispositivo)
    if index_dispositivo >= 0 and index_dispositivo < len(devices_list):
        start = int(start)
        stop = int(stop)
        if status == "On" or status == "on" or status == "ON":
            timers_list.append(DeviceTimer(index_dispositivo, start, stop, True))
        elif status == "Off" or status == "off" or status == "OFF":
            timers_list.append(DeviceTimer(index_dispositivo, start, stop, False))


@webiopi.macro
def disableTimer(index):
    global timers_list
    i = int(index)
    if i >= 0 and i < len(timers_list):
        timers_list[i].enabled = False


@webiopi.macro
def editTimer(id, dispositivo, start, stop, status):
    global devices_list
    global timers_list
    index_timer = int(id)
    index_dispositivo = int(dispositivo)
    if index_timer >= 0 and index_timer < len(timers_list):
      if index_dispositivo >= 0 and index_dispositivo < len(devices_list):
        timers_list[index_timer].index = index_dispositivo
        timers_list[index_timer].start = int(start)
        timers_list[index_timer].stop = int(stop)
        if status == "On" or status == "on" or status == "ON":
            timers_list[index_timer].enabled = True
        elif status == "Off" or status == "off" or status == "OFF":
            timers_list[index_timer].enabled = False

@webiopi.macro
def enableTimer(index):
    global timers_list
    i = int(index)
    if i >= 0 and i < len(timers_list):
        timers_list[i].enabled = True


@webiopi.macro
def getHumidity():
    global humidity
    if humidity is not None:
        return humidity
    else:
        return "None"


@webiopi.macro
def getStatus(index):
    global all_status
    global devices_list    
    if index == "All" or index == "all":
        return all_status
    i = int(index)        
    if i >= 0 and i < len(devices_list):
        if devices_list[i].status:
            return "On"
        else:
            return "Off"
    return "Unknown"


@webiopi.macro
def getTimerOff(index):
    global timers_list
    i = int(index)
    if i >= 0 and i < len(timers_list):
        return timers_list[i].stop
    return 0


@webiopi.macro
def getTimerOn(index):
    global timers_list
    i = int(index)
    if i >= 0 and i < len(timers_list):
        return timers_list[i].start
    return 0


@webiopi.macro
def getTimerStatus(index):
    global timers_list
    i = int(index)
    if i >= 0 and i < len(timers_list):
        if timers_list[i].enabled :
            return "On"
        else:
            return "Off"
    return "Unknown"


@webiopi.macro
def getUptime():
    from datetime import timedelta
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = int(float(f.readline().split()[0]))
        uptime_string = str(timedelta(seconds = uptime_seconds))        
    return uptime_string


@webiopi.macro
def removeTimer(index):
    global timers_list
    i = int(index)
    if i >= 0 and i < len(timers_list):
        timers_list.pop(i)


@webiopi.macro
def toggleRelay(index):
    global devices_list
    global timers_list
    
    global manual_disable_timers
    
    global all_status
    global all_on
    global all_off

    if index == "All" or index == "all":
        if all_on:
            all_on = False
            all_off = True
        else:
            all_on = True
            all_off = False
    else:
        i = int(index)
        all_on = False
        all_off = False
        if i >= 0 and i < len(devices_list):            
            devices_list[i].toggle()
            if manual_disable_timers:
                for j in range(0, len(timers_list)):
                    if timers_list[i].index == i:
                        timers_list[i].enabled = False
                
                
