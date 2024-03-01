# SI-Testing

> Spring 2024, Dr. Shalan

**Goal:** is to provide a circuit capable of testinga chip under changing voltage and temperature. 
- for temperature, we are using a thermoelectric cooler. as a *sub goal* we need to supply with an ideal controlling (PWM) signal to be able to vary the temperature rapidly

## Current Circuit Schematic


![SIcirc drawio (1) drawio](https://github.com/AUC-Hardware/SI-Testing/assets/96356943/2838022a-a774-4877-bd7d-3ab0b5a9d476)

---

### Raspberry Pi Pico W

Getting Started: https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/1

Documentation: https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html

### Relay Switch : 

Datasheet:

### Peltier : 

Datasheet: 

### Digital Potentiometer :

Datasheet:

>[!NOTE] 
>
> Optional circuitry \
> **High Power Resistor**
> - is used to reduce current on the thermoelectric cooler if normal operating current is too high for our need 
> 
> **H-Bridge** 
> - mainly for experimentation 
> - is used to be able to switch the polarity on the thermoelectric cooler so we could switch cooling and heating 
