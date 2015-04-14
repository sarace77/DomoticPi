import webiopi
import datetime

GPIO = webiopi.GPIO

class timer:
	def __init__(self, start = 0, stop = 0, isEnabled = False):
		self.start = start;
		self.stop = stop
		self.isEnabled = isEnabled
	def getStart(self):
		hh = int(self.start/3600)
		mm = int(self.start - hh * 3600)/60
		ss = int(self.start - hh * 3600 - mm * 60)
		return str(hh, ":", mm, " ", ss)
	def getStop(self):
		hh = int(self.stop/3600)
		mm = int(self.stop - hh * 3600)/60
		ss = int(self.stop - hh * 3600 - mm * 60)
		return str(hh, ":", mm, " ", ss)
	def fromString(self, timestring = 0, type = "start"):
		sep_hm = -1
		sep_ms = -1
		while i < len(timestring):
			if timestring[i] == ":":
				sep_hm = i
			elif timestring[i] == " ":
				sep_ms = i
			i = i + 1
		if sep_hm != -1 and sep_ms != -1 :
			hh = int(timestring[0:sep_hm])
			mm = int(timestring[sep_hm + 1: sep_ms])
			ss = int(timestring[sep_ms + 1: len(timestring)])
			if type == "start" or type == "Start" :
				self.start = hh * 3600 + mm * 60 + ss
			elif type == "stop" or type == "Stop" :
				self.stop = hh * 3600 + mm * 60 + ss
		
class dispositivo:
	def __init__(self, name = "relay", pin = 0, status = True):
		self.name = name
		self.status = status
		GPIO.setFunction(pin, GPIO.OUT)
	def getName():
		return name
	def getStatus(self):
		if self.status :
			return "On"
		return "Off"
	def switchOn(self):
		if not self.status:
			GPIO.digitalWrite(RELAY0, GPIO.LOW)
			self.status = True
	def switchOff(self):		
		if self.status:
			GPIO.digitalWrite(RELAY0, GPIO.HIGH)
			self.status = False
	def toggle(self):
		if self.status:
			self.switchOff()
		else:
			self.switchOn()
		

relay0 = dispositivo("relay0", 22)		
relay1 = dispositivo("relay1", 27)		
relay2 = dispositivo("relay2", 17)		
relay3 = dispositivo("relay3", 4)		

RELAY0 = 22
RELAY1 = 27
RELAY2 = 17
RELAY3 = 4

STATUS0 = "Off"
STATUS1 = "Off"
STATUS2 = "Off"
STATUS3 = "Off"

STATUS_ALL = "Off"

TIME_R0_ON = 43200
TIME_R1_ON = 43200
TIME_R2_ON = 43200
TIME_R3_ON = 43200

TIME_R0_OFF = 64800
TIME_R1_OFF = 64800
TIME_R2_OFF = 64800
TIME_R3_OFF = 64800

TIMER_R0_ENABLED = False
TIMER_R1_ENABLED = False
TIMER_R2_ENABLED = False
TIMER_R3_ENABLED = False

def setup():
#	GPIO.setFunction(RELAY0, GPIO.OUT)
#	GPIO.setFunction(RELAY1, GPIO.OUT)
#	GPIO.setFunction(RELAY2, GPIO.OUT)
#	GPIO.setFunction(RELAY3, GPIO.OUT)

#	GPIO.digitalWrite(RELAY0, GPIO.HIGH)
#	GPIO.digitalWrite(RELAY1, GPIO.HIGH)
#	GPIO.digitalWrite(RELAY2, GPIO.HIGH)
#	GPIO.digitalWrite(RELAY3, GPIO.HIGH)
#	webiopi.sleep(0.1)	
#	GPIO.digitalWrite(RELAY0, GPIO.LOW)
#	webiopi.sleep(0.1)	
#	GPIO.digitalWrite(RELAY1, GPIO.LOW)
#	webiopi.sleep(0.1)	
#	GPIO.digitalWrite(RELAY2, GPIO.LOW)
#	webiopi.sleep(0.1)	
#	GPIO.digitalWrite(RELAY3, GPIO.LOW)
#	webiopi.sleep(0.1)	
#	GPIO.digitalWrite(RELAY3, GPIO.HIGH)
#	webiopi.sleep(0.1)	
#	GPIO.digitalWrite(RELAY2, GPIO.HIGH)
#	webiopi.sleep(0.1)	
#	GPIO.digitalWrite(RELAY1, GPIO.HIGH)
#	webiopi.sleep(0.1)	
#	GPIO.digitalWrite(RELAY0, GPIO.HIGH)

def loop():
	global STATUS0
	global STATUS1
	global STATUS2
	global STATUS3
	global STATUS_ALL

	global TIME_R0_ON
	global TIME_R1_ON
	global TIME_R2_ON
	global TIME_R3_ON
	
	global TIME_R0_OFF
	global TIME_R1_OFF
	global TIME_R2_OFF
	global TIME_R3_OFF
	
	global TIMER_R0_ENABLED
	global TIMER_R1_ENABLED
	global TIMER_R2_ENABLED
	global TIMER_R3_ENABLED

	STATUS_ALL = "Unknown"
	
	now = datetime.datetime.now()
	now_s = now.hour * 3600 + now.minute * 60 + now.second

	if ((TIMER_R0_ENABLED == True) and (now_s >= TIME_R0_ON) and (now_s < TIME_R0_OFF)):  
		STATUS0 = "On"
	elif ((TIMER_R0_ENABLED == True) and ((now_s < TIME_R0_ON) or (now_s >= TIME_R0_OFF))):
		STATUS0 = "Off"

	if ((TIMER_R1_ENABLED == True) and (now_s >= TIME_R1_ON) and (now_s < TIME_R1_OFF)):  
		STATUS1 = "On"
	elif ((TIMER_R1_ENABLED == True) and ((now_s < TIME_R1_ON) or (now_s >= TIME_R1_OFF))):
		STATUS1 = "Off"

	if ((TIMER_R2_ENABLED == True) and (now_s >= TIME_R2_ON) and (now_s < TIME_R2_OFF)):  
		STATUS2 = "On"
	elif ((TIMER_R2_ENABLED == True) and ((now_s < TIME_R2_ON) or (now_s >= TIME_R2_OFF))):
		STATUS2 = "Off"

	if ((TIMER_R3_ENABLED == True) and (now_s >= TIME_R3_ON) and (now_s < TIME_R3_OFF)):  
		STATUS3 = "On"
	elif ((TIMER_R3_ENABLED == True) and ((now_s < TIME_R3_ON) or (now_s >= TIME_R3_OFF))):
		STATUS3 = "Off"

	if ((STATUS0 == "On") and (STATUS1 == "On") and (STATUS2 == "On") and (STATUS3 == "On")):
		STATUS_ALL = "On"
	elif ((STATUS0 == "Off") and (STATUS1 == "Off") and (STATUS2 == "Off") and (STATUS3 == "Off")):
		STATUS_ALL = "Off"
					
	if (STATUS0 == "On"):
		GPIO.digitalWrite(RELAY0, GPIO.LOW)
	elif (STATUS0 == "Off"):
		GPIO.digitalWrite(RELAY0, GPIO.HIGH)

	if (STATUS1 == "On"):
		GPIO.digitalWrite(RELAY1, GPIO.LOW)
	elif (STATUS1 == "Off"):
		GPIO.digitalWrite(RELAY1, GPIO.HIGH)

	if (STATUS2 == "On"):
		GPIO.digitalWrite(RELAY2, GPIO.LOW)
	elif (STATUS2 == "Off"):
		GPIO.digitalWrite(RELAY2, GPIO.HIGH)

	if (STATUS3 == "On"):
		GPIO.digitalWrite(RELAY3, GPIO.LOW)
	elif (STATUS3 == "Off"):
		GPIO.digitalWrite(RELAY3, GPIO.HIGH)


	webiopi.sleep(0.5)

def destroy():
	GPIO.digitalWrite(RELAY0, GPIO.HIGH)
	GPIO.digitalWrite(RELAY1, GPIO.HIGH)
	GPIO.digitalWrite(RELAY2, GPIO.HIGH)
	GPIO.digitalWrite(RELAY3, GPIO.HIGH)

@webiopi.macro
def disableTimer(number):
	global TIMER_R0_ENABLED
	global TIMER_R1_ENABLED
	global TIMER_R2_ENABLED
	global TIMER_R3_ENABLED

	if (int(number) == 0):
		TIMER_R0_ENABLED = False 

	if (int(number) == 1):
		TIMER_R1_ENABLED = False 

	if (int(number) == 2):
		TIMER_R2_ENABLED = False 
	
	if (int(number) == 3):
		TIMER_R3_ENABLED = False 
	

@webiopi.macro
def enableTimer(number):
	global TIMER_R0_ENABLED
	global TIMER_R1_ENABLED
	global TIMER_R2_ENABLED
	global TIMER_R3_ENABLED

	if (int(number) == 0):
		TIMER_R0_ENABLED = True 

	if (int(number) == 1):
		TIMER_R1_ENABLED = True 

	if (int(number) == 2):
		TIMER_R2_ENABLED = True 
	
	if (int(number) == 3):
		TIMER_R3_ENABLED = True 


@webiopi.macro
def getStatus(number):
	if (number == "0"):
		return STATUS0
	if (number == "1"):
		return STATUS1
	if (number == "2"):
		return STATUS2
	if (number == "3"):
		return STATUS3
	if (number == "All"):
		return STATUS_ALL
	return "Off"

@webiopi.macro
def getTimerOff(number):
	if (number == "0"):
		return TIME_R0_OFF
	if (number == "1"):
		return TIME_R1_OFF
	if (number == "2"):
		return TIME_R2_OFF
	if (number == "3"):
		return TIME_R3_OFF
	return 0

@webiopi.macro
def getTimerOn(number):
	if (number == "0"):
		return TIME_R0_ON
	if (number == "1"):
		return TIME_R1_ON
	if (number == "2"):
		return TIME_R2_ON
	if (number == "3"):
		return TIME_R3_ON
	return 0


@webiopi.macro
def getTimerStatus(number):
	print (number)
	if (number == "0"):
		if (TIMER_R0_ENABLED):
			return "On"
		else :
			return "Off"
	
	if (number == "1"):
		if (TIMER_R1_ENABLED):
			return "On"
		else :
			return "Off"
	
	if (number == "2"):
		if (TIMER_R2_ENABLED):
			return "On"
		else :
			return "Off"
	
	if (number == "3"):
		if (TIMER_R3_ENABLED):
			return "On"
		else :
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
def setTimer0Off(timer):
	global TIME_R0_OFF
	TIME_R0_OFF = int(timer)


@webiopi.macro
def setTimer1Off(timer):
	global TIME_R1_OFF
	TIME_R1_OFF = int(timer)


@webiopi.macro
def setTimer2Off(timer):
	global TIME_R2_OFF
	TIME_R2_OFF = int(timer)


@webiopi.macro
def setTimer3Off(timer):
	global TIME_R3_OFF
	TIME_R3_OFF = int(timer)


@webiopi.macro
def setTimer0On(timer):
	global TIME_R0_ON
	TIME_R0_ON = int(timer)


@webiopi.macro
def setTimer1On(timer):
	global TIME_R1_ON
	TIME_R1_ON = int(timer)


@webiopi.macro
def setTimer2On(timer):
	global TIME_R2_ON
	TIME_R2_ON = int(timer)


@webiopi.macro
def setTimer3On(timer):
	global TIME_R3_ON
	TIME_R3_ON = int(timer)


@webiopi.macro
def toggleRelay(number):
	global STATUS0
	global STATUS1
	global STATUS2
	global STATUS3
	global STATUS_ALL
	global TIMER_R0_ENABLED
	global TIMER_R1_ENABLED
	global TIMER_R2_ENABLED
	global TIMER_R3_ENABLED

	if (number == "0"):
		if (STATUS0 == "On"):
			STATUS0 = "Off"
		else :
			STATUS0 = "On"
		TIMER_R0_ENABLED = False
		return STATUS0
	elif (number == "1"):
		if (STATUS1 == "On"):
			STATUS1 = "Off"
		else :
			STATUS1 = "On"
		TIMER_R1_ENABLED = False
		return STATUS1
	elif (number == "2"):
		if (STATUS2 == "On"):
			STATUS2 = "Off"
		else :
			STATUS2 = "On"
		TIMER_R2_ENABLED = False
		return STATUS2
	elif (number == "3"):
		if (STATUS3 == "On"):
			STATUS3 = "Off"
		else :
			STATUS3 = "On"
		TIMER_R3_ENABLED = False
		return STATUS3
	elif (number == "All"):
		if (STATUS_ALL == "On"):
			STATUS0 = "Off"
			STATUS1 = "Off"
			STATUS2 = "Off"
			STATUS3 = "Off"
			STATUS_ALL = "Off"
		else :
			STATUS0 = "On"
			STATUS1 = "On"
			STATUS2 = "On"
			STATUS3 = "On"
			STATUS_ALL = "On"
		return STATUS_ALL

	return "Unknown"

