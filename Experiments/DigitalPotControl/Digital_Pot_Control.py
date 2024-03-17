from machine import Pin
import time
import rp2

# CS to INC setup
def tci():
    time.sleep_ms(5)

# UD to INC setup
def tdi():
    time.sleep_us(5)

# INC High to UD change
def tid():
    time.sleep_us(5)
    
# INC High and Low period
def tihl():
    #5 microseconds
    time.sleep_us(5)

# chip select
cs = Pin(14,mode=Pin.OUT,value=0)
tci()

# up down
ud = Pin(13,mode=Pin.OUT,value=1)
tdi()

# increment
inc = Pin(12,mode=Pin.OUT,value=1)
tid()


# This yields a pulse of 35 us which is counter intuitive
# for the time being this suits our use case
# TODO: change this into rp2 assembly instructions
def blink(pin):
    pin.toggle()
    tihl()
    
def wiperControl(increments,updownSelect):
    ud.value(updownSelect)
    tdi()
    for i in range(0,increments):
        time.sleep_ms(100)
        blink(inc)
        
        
#10k ohms and 101ohm step
#100 increments to max/min
wiperControl(70,1)

time.sleep(10)

wiperControl(70,0)


