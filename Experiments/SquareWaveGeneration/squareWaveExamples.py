from machine import Pin, Timer
from rp2 import PIO, StateMachine, asm_pio
    
p15 = Pin(15, Pin.OUT)
timer = Timer()
p15.off()
def squareByToggle(timer):
    p15.toggle()    

@asm_pio(set_init=PIO.OUT_LOW)
def square():
    wrap_target()
    set(pins, 1)
    set(pins, 0)
    wrap()

choice = input("input choice\n 1) Assembly Statemachine Square Wave \n 2) Toggle Square Wave\n")

if(choice==1):
    sm = rp2.StateMachine(0, square, freq=2000, set_base=Pin(15))
    sm.active(1)
else:
    timer.init(freq=2000, mode=Timer.PERIODIC, callback=squareByToggle)