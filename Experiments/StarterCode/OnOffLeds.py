from machine import Pin
import time

led1 = Pin('18', Pin.OUT)
led2 = Pin('LED', Pin.OUT)
led3 = Pin(20, Pin.OUT)

led1.value(1)
led2.value(1)
led3.value(1)

time.sleep(5)

led1.value(0)
led2.value(0)
led3.value(0)