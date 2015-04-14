import webiopi
import datetime

GPIO = webiopi.GPIO

devices_list = []
timers_list = []

all_status = "Unknown"

all_on = False
all_off = False

manual_disable_timers = True

class DeviceTimer:
    def __init__(self, index = -1, start = 0, stop = 0, enabled = False):
        self.index = index
        self.start = start
        self.stop = stop
        self.enabled = enabled


class Dispositivo:
    def __init__(self, name="dispositivo", pin = 0, status = False):
        self.name = name
        self.pin = pin
        self.status = status
        GPIO.setFunction(self.pin, GPIO.OUT)
        if self.status:
            switchOn()
        else :
            switchOff()
    
    def switchOn(self):
        GPIO.digitalWrite(self.pin, GPIO.LOW)
        self.status = True
    
    def switchOff(self):
        GPIO.digitalWrite(self.pin, GPIO.HIGH)
        self.status = False
            
    def toggle(self):
        if self.status:
            switchOff()
        else :
            switchOn()
            
            
def setup():
    global devices_list
    global timers_list
    global all_on
    
    lista_dispostivi.append(Dispositivo("Relay 0"), 22, False)
    lista_dispostivi.append(Dispositivo("Relay 1"), 27, False)
    lista_dispostivi.append(Dispositivo("Relay 2"), 17, False)
    lista_dispostivi.append(Dispositivo("Relay 3"), 4, False)
    
    timers_list.append(DeviceTimer, 0, 43200, 64800)
    timers_list.append(DeviceTimer, 1, 43200, 64800)
    timers_list.append(DeviceTimer, 2, 43200, 64800)
    timers_list.append(DeviceTimer, 3, 43200, 64800)
    
    for j in range(0,2):
        for i in len(devices_list) :
            devices_list[i].toggle()
            webiopi.sleep(0.1)
        webiopi.sleep(0.1)


def loop():
    global devices_list
    global timers_list
    
    global all_status
    global all_on
    global all_off

    all_status = "Unknown"
    
    if (all_on or all_off) and (all_on != all_off):
        if all_on:
            all_status = "On"
            for i in len(devices_list) :
                if not devices_list[i].status:
                    devices_list[i].switchOn()
        else:
            all_status = "Off"
            for i in len(devices_list) :
                if devices_list[i].status:
                    devices_list[i].switchOff()
    else:        
        for i in len(timers_list):
            if timers_list[i].index >= 0 and timers_list[i].index < len(devices_list):
                if timers_list[i].enabled and now_s >= timers_list[i].start and now_s < timers_list[i].stop:
                    devices_list[timers_list[i].index].switchOn()
                elif timers_list[i].enabled and (now_s < timers_list[i].start and now_s >= timers_list[i].stop):
                    devices_list[timers_list[i].index].switchOff()
            

def destroy():
    for i in len(devices_list) :
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
        devices_list[index_timer].start = int(start)
        devices_list[index_timer].stop = int(stop)
        if status == "On" or status == "on" or status == "ON":
            devices_list[index_timer].enabled = True
        elif status == "Off" or status == "off" or status == "OFF":
            devices_list[index_timer].enabled = False


@webiopi.macro
def enableTimer(index):
    global timers_list
    i = int(index)
    if i >= 0 and i < len(timers_list):
        timers_list[i].enabled = True


@webiopi.macro
def getStatus(index):
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
        return timers_list[i].status
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
def setTimer0Off(timer):
    global timers_list
    timers_list[0].stop = int(timer)


@webiopi.macro
def setTimer1Off(timer):
    global timers_list
    timers_list[1].stop = int(timer)


@webiopi.macro
def setTimer2Off(timer):
    global timers_list
    timers_list[2].stop = int(timer)


@webiopi.macro
def setTimer3Off(timer):
    global timers_list
    timers_list[3].stop = int(timer)


@webiopi.macro
def setTimer0On(timer):
    global timers_list
    timers_list[0].start = int(timer)


@webiopi.macro
def setTimer1On(timer):
    global timers_list
    timers_list[1].start = int(timer)


@webiopi.macro
def setTimer2On(timer):
    global timers_list
    timers_list[2].start = int(timer)


@webiopi.macro
def setTimer3On(timer):
    global timers_list
    timers_list[3].start = int(timer)


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
                for j in len(timers_list):
                    if timers_list[i].index == i:
                        timers_list[i].enabled = false
                
            

