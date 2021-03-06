'''
file: change_baud.py

Program to change the baud rate of the Create.

The default on startup for the Create is 57600, but the wireless devices we are suing only support 9600 baud, so on each startup we need to change the baudrate.
'''

import serial, sys, time, math
from time import sleep
import pici
reload(pici)

# Open a serial port at the default baud rate.
sPort = '/dev/ttyUSB1'
# Now try the slower baud rate
sBaud = 9600
ser = serial.Serial(sPort,sBaud)
# Start - start, full mode, lights and song
pici.start(ser)
sleep(1.0)
# Stop driving, turn off play light, song
pici.stop(ser)

ser.close()
