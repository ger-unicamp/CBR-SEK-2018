#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

# Connect EV3 color sensor and check connected.

cl = ColorSensor()
assert cl.connected, "Connect a color sensor to any sensor port"

# Put the color sensor into COL-REFLECT mode
# to measure reflected light intensity.
# In this mode the sensor will return a value between 0 and 100
cl.mode='COL-COLOR'

while True:
    if c1.value()=='0':
        print('none')
        delay(5)
    elif c1.value()=='1':
        print('black')
    elif c1.value()=='2':
        print('blue')
    elif c1.value()=='3':
        print('green')
    elif c1.value()=='4':
        print('yellow')
    elif c1.value()=='5':
        print('red')
    elif c1.value()=='6':
        print('white')
    elif c1.value()=='7':
        print('brown')

# I get max 80 with white paper, 3mm separation
# and 5 with black plastic, same separation
