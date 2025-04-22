from machine import Pin
from time import sleep_ms, sleep
import uasyncio
import onewire
import ds18x20

PID_PIN: int = 15
TEMP_READ_PIN: int = 13
INT16_MAX: int = 65025

class TempReader:
    _ow = onewire.OneWire(Pin(TEMP_READ_PIN))
    _ds = ds18x20.DS18X20(_ow)
    _devices = None
    _startTempRead: bool = False
    
    def scan_devices(self):
        self._devices = self._ds.scan()
        if(self._devices):
            print('INFO: found devices:')
            for device in self._devices:
                print("Device: {}".format(device))
            return True
        else:
            print("WARN: No Devices have been found")
            return False
        
    def startTempRead(self):
        self._startTempRead = True
        
    def stopTempRead(self):
        self._startTempRead = False
        
    async def print_temp_readings(self):
        while(self._startTempRead):
            if (self._devices[0]):
                self._ds.convert_temp()
                for device in self._devices:
                    print("Device: {}".format(device))
                    print("Temperature= {}".format(self._ds.read_temp(device)))
            else:
                print("ERROR: No Devices to read from")
            await uasyncio.sleep_ms(250)

class PID:
    # In seconds
    period = 0

    _startPID = False
    _pid_pin = Pin(PID_PIN, Pin.OUT)
    
    # i in range 0 to 65025 signyfing duty cycle %
    async def pwm_controller_loop(self, i):
        while (self._startPID):
            self._pid_pin.on()
            await uasyncio.sleep((self.period)*(i/INT16_MAX))
            self._pid_pin.off()
            await uasyncio.sleep((self.period)*(1- i/INT16_MAX))

    def startPID(self):
        self._startPID = True

    def stopPID(self):
        self._startPID = False
    
async def main():
    pidController = PID()
    pidController.period = 1
    pidController.startPID()
    tempReader = TempReader()
    
    if (tempReader.scan_devices()):
        tempReader.startTempRead()
        uasyncio.create_task(tempReader.print_temp_readings())
        uasyncio.create_task(pidController.pwm_controller_loop(INT16_MAX/2))
    else:
        return
    
    await uasyncio.sleep(20)
    pidController.stopPID()

# run our entry point main()
uasyncio.run(main())



