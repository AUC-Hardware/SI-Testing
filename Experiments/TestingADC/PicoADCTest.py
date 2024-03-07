import machine
import utime

myReading = machine.ADC(0)

while True:
    myValue = myReading.read_u16()
    print(myValue/65535*3.3)
    utime.sleep(0.1)
