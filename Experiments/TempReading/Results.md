# DS18B20 Temprature reading experiment

## Description

This was a simple experiment to test the reading of the temprature from the DS18B20 temprature sensor to the pico microcontroller.

## Method

The libraries used was the onewire library and the DS18x20 library. Together, we are able to interface our DS18B20 device and read temprature from it. The pin used to read temprature was PIN 15, which was connected to the DQ on the temprature sensor. VDD was supplied from the pico as 3.3V and GND was also from the pico.


## Results

PICO was able to accuratly read temprature.