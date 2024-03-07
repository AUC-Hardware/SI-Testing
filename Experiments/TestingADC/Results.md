# PicoADCTest

## Description

This was a simple experiment to test the PICO's ability to read an analog signal that ranges from 0 to 3.3V  (due to using the PICO's Vcc)

ADC has a 12 bit resolution which means a range from 0 to 4095
In micropython this is mapped to a 16 bit value whcih means code wise it will range from 0 to 65535

## Method

Using ADC on pin 31 (GP 26) read voltage across a 10k Ohm mechanical potentiaometer and compare readings to that of a multimeter.


## Results
