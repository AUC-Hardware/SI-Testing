# PicoADCTest

## Description

This was a simple experiment to test the PICO's ability to read an analog signal that ranges from 0 to 3.3V  (due to using the PICO's Vcc)

ADC has a 12-bit resolution, which means a range from 0 to 4095
In micro python this is mapped to a 16-bit value, which means the code wise it will range from 0 to 65535

## Method

Using ADC on pin 31 (GP 26), read voltage across a 10k Ohm mechanical potentiometer and compare readings to that of a multimeter.


## Results

PICO was able to accuratly read voltage such that it always matched the readings on our digital multimeter ( the M890G ).
