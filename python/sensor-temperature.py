import webiopi
GPIO = webiopi.GPIO

def setuip():
	bmp = webiopi.deviceInstance("bmp")

def loop():
	bmp = webiopi.deviceInstance("bmp")
	celsius = bmp.getCelsius()
	print("Temperature: ", celsius)
	webiopi.sleep(1)

def destroy():
	bmp = webiopi.deviceInstance("bmp")



	
	
	
