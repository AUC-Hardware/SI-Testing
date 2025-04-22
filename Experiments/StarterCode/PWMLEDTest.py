from machine import Pin, PWM
from time import sleep_ms

pwm = PWM(Pin(15))

pwm.freq(100)

while True:
    for duty in range(65025, 0, 5000):
        pwm.duty_u16(duty)
        sleep_ms(1000)
    for duty in range(65025, 0, -5000):
        pwm.duty_u16(duty)
        sleep_ms(1000)