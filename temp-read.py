from machine import Pin
import time
import onewire
import ds18x20

ow = onewire.OneWire(Pin(15))
ds = ds18x20.DS18X20(ow)
p15 = Pin(16, Pin.OUT)


devices = ds.scan()
print('found devices:', devices)

while True:
    ds.convert_temp()
    time.sleep_ms(750)
    temp = ds.read_temp(devices[0])
    if(temp > 30.0):
        p15.value(1)
    else:
        p15.value(0)
        
    for device in devices:
        print("Device: {}".format(device))
        print("Temperature= {}".format(ds.read_temp(device)))

