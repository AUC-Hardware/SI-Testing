from machine import Pin, PWM
from time import sleep

pwm = PWM(Pin(15))

pwm.freq(100)

while True:
    for duty in range(65025):
        pwm.duty_u16(duty)
        sleep(0.001)
    for duty in range(65025, 0, -1):
        pwm.duty_u16(duty)
        sleep(0.001)