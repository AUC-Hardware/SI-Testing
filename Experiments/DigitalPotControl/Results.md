
- LED gradually goes up in brightness and gradually decreased in brightness

### Important notes

On the Osilliscope the resulting square wave generated from iterating on `blink()` function had a bigger cycle time than expected.

We should change the use of `time` lib and utilise the use of the RP2 assembly to have acute control over the delay.
