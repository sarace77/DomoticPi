#!/usr/bin/env python
import smbus
import webiopi

TSL2591_VISIBLE                         = 2     # channel 0 - channel 1
TSL2591_INFRARED                        = 1     # channel 1
TSL2591_FULLSPECTRUM                    = 0     # channel 0     
TSL2591_ADDR                            = 0x29
TSL2591_READBIT                         = 0x01
TSL2591_COMMAND_BIT                     = 0xA0  # bits 7 and 5 for 'command normal'
TSL2591_CLEAR_BIT                       = 0x40  #Clears any pending interrupt (write 1 to clear)
TSL2591_WORD_BIT                        = 0x20  #1 = read/write word (rather than byte)
TSL2591_BLOCK_BIT                       = 0x10  #1 = using block read/write
TSL2591_CONTROL_RESET                   = 0x80
TSL2591_ENABLE_POWERON                  = 0x01
TSL2591_ENABLE_POWEROFF                 = 0x00
TSL2591_ENABLE_AEN                      = 0x02
TSL2591_ENABLE_AIEN                     = 0x10
TSL2591_GAIN_LOW                        = 0x00  #low gain (1x)
TSL2591_GAIN_MED                        = 0x10  #medium gain (25x)
TSL2591_GAIN_HIGH                       = 0x20  #medium gain (428x)
TSL2591_GAIN_MAX                        = 0x30  #max gain (9876x)
TSL2591_INTEGRATIONTIME_100MS           = 0x00
TSL2591_INTEGRATIONTIME_200MS           = 0x01
TSL2591_INTEGRATIONTIME_300MS           = 0x02
TSL2591_INTEGRATIONTIME_400MS           = 0x03
TSL2591_INTEGRATIONTIME_500MS           = 0x04
TSL2591_INTEGRATIONTIME_600MS           = 0x05
TSL2591_LUX_DF                          = 408.0
TSL2591_LUX_COEFB                       = 1.64  #CH0 coefficient 
TSL2591_LUX_COEFC                       = 0.59  #CH1 coefficient A
TSL2591_LUX_COEFD                       = 0.86  #CH2 coefficient B
TSL2591_REGISTER_ENABLE                 = 0x00
TSL2591_REGISTER_CONTROL                = 0x01
TSL2591_REGISTER_THRESHHOLDL_LOW        = 0x02
TSL2591_REGISTER_THRESHHOLDL_HIGH       = 0x03
TSL2591_REGISTER_THRESHHOLDH_LOW        = 0x04
TSL2591_REGISTER_THRESHHOLDH_HIGH       = 0x05
TSL2591_REGISTER_INTERRUPT              = 0x06
TSL2591_REGISTER_CRC                    = 0x08
TSL2591_REGISTER_ID                     = 0x0A
TSL2591_REGISTER_CHAN0_LOW              = 0x14
TSL2591_REGISTER_CHAN0_HIGH             = 0x15
TSL2591_REGISTER_CHAN1_LOW              = 0x16
TSL2591_REGISTER_CHAN1_HIGH             = 0x17

class TSL2591:
    def __init__(self):
        self.bus =          smbus.SMBus(1) 
        self.address        = TSL2591_ADDR
        self.channel        = TSL2591_FULLSPECTRUM
        self.gain           = TSL2591_GAIN_HIGH
        self.integration    = TSL2591_INTEGRATIONTIME_500MS
        self.sensorID       = self.read8(0x12)
        self.enable()
    
    def calculateLux(self, ch0, ch1):
        atime = 100.0
        again = 1.0
        if (ch0 == 0xFFFF) or (ch1 == 0xFFFF):
            return 0
        if self.integration == TSL2591_INTEGRATIONTIME_200MS:
            atime = 200.0
        elif self.integration == TSL2591_INTEGRATIONTIME_300MS:
            atime = 300.0
        elif self.integration == TSL2591_INTEGRATIONTIME_400MS:
            atime = 400.0
        elif self.integration == TSL2591_INTEGRATIONTIME_500MS:
            atime = 500.0
        elif self.integration == TSL2591_INTEGRATIONTIME_600MS:
            atime = 600.0
        
        if self.gain == TSL2591_GAIN_MED:
            again = 25.0
        elif self.gain == TSL2591_GAIN_HIGH:
            again = 428.0
        elif self.gain == TSL2591_GAIN_MAX:
            again = 9876.0
                   
        cpl = (atime * again) / TSL2591_LUX_DF;   
        lux1 = (ch0 - (TSL2591_LUX_COEFB * ch1)) / cpl
        lux2 = ((TSL2591_LUX_COEFC * ch0) - (TSL2591_LUX_COEFD * ch1)) / cpl
        
        if lux1 > lux2:
            return lux1 * 20
        
        return lux2 * 20
        
    def disable(self):
        self.write8(TSL2591_COMMAND_BIT | TSL2591_REGISTER_ENABLE, TSL2591_ENABLE_POWEROFF)

    def enable(self):
        self.write8(TSL2591_COMMAND_BIT | TSL2591_REGISTER_ENABLE, TSL2591_ENABLE_POWERON | TSL2591_ENABLE_AEN | TSL2591_ENABLE_AIEN)
        self.setTiming(self.integration)
        self.setGain(self.integration, self.gain)

    def getLuminosity(self, channel):
        lux = 0;
        delay = self.getTiming()/1000
        webiopi.sleep(delay*120)
        ir = self.read16(TSL2591_COMMAND_BIT | TSL2591_REGISTER_CHAN1_LOW)        
        full = self.read16(TSL2591_COMMAND_BIT | TSL2591_REGISTER_CHAN0_LOW)
        visible = full - ir
        if channel == TSL2591_FULLSPECTRUM:
            return full
        elif channel == TSL2591_INFRARED:
            return ir
        elif channel == TSL2591_VISIBLE:
            return visible
        return 0
    
    def getGain(self):
        return self.gain
    
    def getTiming(self):
        return self.integration
    
    def read8(self, register):
        return self.bus.read_byte_data(self.address, register)
    
    def read16(self, register):
        return self.bus.read_word_data(self.address, register)
    
    def setGain(self, integration, gain):
        self.gain           = gain
        self.integration    = integration
        self.write8(TSL2591_COMMAND_BIT + TSL2591_REGISTER_CONTROL, integration | gain);  
    
    def setTiming(self, integration):
        self.integration    = integration
        self.write8(TSL2591_COMMAND_BIT + TSL2591_REGISTER_CONTROL, integration);  

    def write8(self, register, value):
        self.bus.write_byte_data(self.address, register, value)        
        
lumDevices = []
luminosity = 0

def setup():
    global lumDevices
    lumDevices.append(TSL2591())
    
def loop():
    global luminosity
    full = lumDevices[0].getLuminosity(TSL2591_FULLSPECTRUM)
    ir = lumDevices[0].getLuminosity(TSL2591_INFRARED)
    luminosity = lumDevices[0].calculateLux(full, ir)
    webiopi.sleep(1.0)
    
def destroy():
    lumDevices[0].disable()       


@webiopi.macro
def getLuminosity():
    global luminosity
    return luminosity

