# Digital Control of X9C103S POT

Aim is to Digitally control the POT and exploring its functionality
The POT has the following control signals

## Mode Selection (From Datasheet)

| ~CSbar | ~INC | U/~D | Mode |
| --- | --- | --- | --- |
| L | Negative Edge | H | Wiper Up |
| L | Negative Edge | L | Wiper Down | 
| Positive Edge | H | X | Store Wiper Position | 
| H | X | X | Standby Current | 
| Positive Edge | L | X | No Store, Return to Standby | 

>[!warning]
>
>Supply Voltage Operational Limits:  $5V\ \pm 10\%$

## IMPORTANT: Timings

Any Change to $\bar{CS}$ needs to occur $> 20 ms$ 

|Parameter|Min|Typ|Max|Units|
| --- | --- | --- | --- | --- |
| CS to INC setup | 100 | | | |
| INC HIGH to U/D change | 100 | | | |


