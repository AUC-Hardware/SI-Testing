# SI-Testing

> Spring 2024, Dr. Shalan

**Goal:** is to provide a circuit capable of testinga chip under changing voltage and temperature. 
- for temperature, we are using a thermoelectric cooler. as a *sub goal* we need to supply with an ideal controlling (PWM) signal to be able to vary the temperature rapidly

## Current Circuit Schematic

![SIcirc drawio (1) drawio](https://github.com/AUC-Hardware/SI-Testing/assets/96356943/2838022a-a774-4877-bd7d-3ab0b5a9d476)

>[!WARNING]
>
> Raspberry Pico pins are arbitrary in this diagram, consult the pinout diagram when connecting the pico

---

### Raspberry Pi Pico W

Getting Started: https://projects.raspberrypi.org/en/projects/getting-started-with-the-pico/1

Documentation: https://www.raspberrypi.com/documentation/microcontrollers/raspberry-pi-pico.html

#### Pinout Diagram
![image](https://github.com/AUC-Hardware/SI-Testing/assets/96356943/914f1f24-ece7-4f83-a233-6fb2200a05f4)

Our digital Microcontroller
- Will host ``micropython`` code to execute and control the circuitry
  - The code will have the PID which controlls the PWM signal 

---
### Relay Switch : To be documented

Datasheet:

- is used to protect the Pico from the Temperature varying circuitry
- The PWM signal is suppled to it

---
### Peltier : TEC1-12706

Datasheet: https://www.alldatasheet.com/datasheet-pdf/pdf/227422/ETC2/TEC1-12706.html
> A better datasheet or reference is needed

Thermoelectric cooler
- is used to cary the temperature on the chip
- $12V$, $6A$
- switches heating and cooling sides when current direction is switched 

---
### Digital Potentiometer : MCP4131-103E/P

Datasheet: https://u.pcloud.link/publink/show?code=XZEJx00Z2zHjB7IoRRXOGcCnvikJS4BVzfdy

Volatile Memory Digital Potentiometer
- Is used to vary the voltage on the chip
- Has memory to remember the latest resistance setting

---
### Temperature Sensor : To be documented

Datasheet:

- Will provide temperature input to the PICO from the Thermoelectric cooler to be given to the PID

---

>[!NOTE] 
>
> Optional circuitry \
> **High Power Resistor**
> - is used to reduce current on the thermoelectric cooler if normal operating current is too high for our need 
> 
> **H-Bridge** 
> - mainly for experimentation 
> - is used to be able to switch the polarity on the thermoelectric cooler so we could switch cooling and heating 
