from machine import Pin
from time import sleep_ms, sleep
import uasyncio
import onewire
import ds18x20

PID_PIN: int = 15
TEMP_READ_PIN: int = 13
INT16_MAX: int = 65025
DEFAULT_SAMPLING_RATE: int = 250

class TempReader:
    _ow = onewire.OneWire(Pin(TEMP_READ_PIN))
    _ds = ds18x20.DS18X20(_ow)
    _devices = None
    _startTempRead: bool = False
    currentReadTemp: None | float = None

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

    async def print_temp_readings_loop(self):
        while(self._startTempRead):
            if (self._devices):
                self._ds.convert_temp()
                for device in self._devices:
                    print("Device: {}".format(device))
                    print("Temperature= {}".format(self._ds.read_temp(device)))
            else:
                print("ERROR: No Devices to read from")
            await uasyncio.sleep_ms(250)

    async def update_temp_readings_loop(self):
        while(self._startTempRead):
            if (self._devices):
                self._ds.convert_temp()
                self.currentReadTemp = self._ds.read_temp(self._devices[0])
            else:
                print("ERROR: No Devices to read from")
            await uasyncio.sleep_ms(250)


# some of the code Ported and modified from Phil's Lab C implementation of PID controller
# https://www.youtube.com/watch?v=zOByx3Izf5U&t=160s
class PID:
    ## PWM attributes
    period = 0

    _startPID = False
    _pid_pin = Pin(PID_PIN, Pin.OUT)
    ##

    def __init__(
            self,
            Kp = 1,
            Ki = 0,
            Kd = 0,
            tau = 0,
            limMin = 0,
            limMax = 0,
            T = 250,
            integrator = 0,
            prev_error = 0,
            differentiator = 0,
            prev_measurement = 0,
            out = 0
        ):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self._tau = tau
        self._limMin = limMin
        self._limMax = limMax
        self._T = T

        # control variables
        self._integrator = integrator
        self._prev_error = prev_error
        self._differentiator = differentiator
        self._prev_measurement = prev_measurement
        self.out = out

    def pid_update(self, setpoint: float, measurement: float):
        # error signal calculation #
        error: float = setpoint - measurement

        # proportional component #
        proportional: float = self.Kp * error

        # intergral component #
        self._integrator = self._integrator + 0.5 * self._Ki * self._T * (error + self._prev_error)

        # Integrator anti windup #
        # Since integral component can go over other channels
        # we clamp it
        limMinF : float
        limMaxF : float

        if (self._limMax > proportional):
            limMaxF = self._limMax - proportional
        else:
            limMaxF = 0.0

        if (self._limMin > proportional):
            limMinF = self._limMin - proportional
        else:
            limMinF = 0.0

        if (self._integrator > limMaxF):
            self._integrator = limMaxF
        elif (self._integrator < limMinF):
            self._integrator = limMinF

        # Derivative band limited differentiation
        self._differentiator = (2.0 * self.Kd * (measurement - self._prev_measurement)) + (2.0 * self._tau - self._T * self._differentiator) / (2.0 * self._tau + self._T)

        self.out = proportional + self._integrator + self._differentiator

        self._prev_error = error
        self._prev_measurement = measurement

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
    pidController = PID(1, 0 ,0, 0, 0, 100, 250, 0, 0 ,0 ,0, 23)
    pidController.period = 1
    pidController.startPID()
    tempReader = TempReader()

    if (tempReader.scan_devices()):
        tempReader.startTempRead()
        uasyncio.create_task(pidController.pwm_controller_loop(INT16_MAX/2))
        uasyncio.create_task(tempReader.update_temp_readings_loop())
        uasyncio.create_task(tempReader.print_temp_readings_loop())
    else:
        return

    while True:
        if (tempReader.currentReadTemp is not None):
            pidController.pid_update(40, tempReader.currentReadTemp)
        print(pidController.out)
        await uasyncio.sleep_ms(40)

# run our entry point main()
uasyncio.run(main())
