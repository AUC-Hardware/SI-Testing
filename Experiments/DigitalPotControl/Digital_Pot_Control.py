import utime
from machine import Pin

p20 = Pin(20, Pin.OUT)

# period in seconds
def riseAndFall(pin, period):
    pin.on()
    utime.sleep(period) 
    
    
riseAndFall(p20, 5)