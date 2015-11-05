'''
Simple control example - goes straight until it hits a wall then turns
'''
import serial, sys, time, math
from time import sleep
import pici
reload(pici)

# Open the Create's serial port
sPort = '/dev/ttyUSB1'
sBaud = 9600    # wireless
#sBaud = 57600  # wired, Create default
ser = serial.Serial(sPort,sBaud, timeout=1.0)

# Start - start, full mode, lights and song
pici.start(ser)

# stop driving, play stop song, turn off play light
pici.stop(ser)

ser.close()




