# SI-Testing

> Spring 2024, Dr. Shalan

**Goal:** is to provide a circuit capable of testinga chip under changing voltage and temperature. 
- for temperature, we are using a thermoelectric cooler. as a *sub goal* we need to supply with an ideal controlling (PWM) signal to be able to vary the temperature rapidly

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
### Second Digital Potentiometer : X9C103S

Datasheet: [https://u.pcloud.link/publink/show?code=XZEJx00Z2zHjB7IoRRXOGcCnvikJS4BVzfdy](https://u.pcloud.link/publink/show?code=XZcJRX0ZARyeeIvch2VLE2VBvFsLeyBOw4zV)
Example: https://electropeak.com/learn/interfacing-x9c103s-10k-digital-potentiometer-module-with-arduino/

- Is used to vary the voltage on the chip
- 0-10kΩ with 100 steps
- Up to ±5V across the potentiometer end-points

---
### Temperature Sensor : DS18B20 Waterproof Temperature Sensor

Datasheet: https://u.pcloud.link/publink/show?code=XZfujk0ZSR5hogIrCKkFY19oXnh8zp0lHThX

- Will provide temperature input to the PICO from the Thermoelectric cooler to be given to the PID

---
### Thermometer : TP101 

Datasheet: https://u.pcloud.link/publink/show?code=XZfujk0ZSR5hogIrCKkFY19oXnh8zp0lHThX

- Measuring Temperature Range: -50 to 300 degrees (-58 to 572 Fahrenheit)

---
### Thermometer with probe: TPM-10  

Datasheet: https://u.pcloud.link/publink/show?code=XZfujk0ZSR5hogIrCKkFY19oXnh8zp0lHThX

- Temperature range: -50°C~ 110°C
- Temperature accuracy: ±1°C
- Resolution: 0.1°C

---
### Voltage Regulator: LM317

Datasheet: https://u.pcloud.link/publink/show?code=XZqG0X0ZURodwRRACp8z1VfRVn5GCHM6Uq97

It will be used to assist with voltage control. See the voltage control circuit diagram for more details

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
