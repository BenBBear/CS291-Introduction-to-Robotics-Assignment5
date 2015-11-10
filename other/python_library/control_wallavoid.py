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

# Loop for some amount of time
t0 = time.time()
tEnd = 1800
while ( (time.time()-t0) < tEnd):
    sensorDict = pici.getSensorsAll(ser)
    print sensorDict
    if not sensorDict:
        print "Error!  Appears that the Create is off?"
    else:
        # If we hit a bump - backup and turn for some time
        if (sensorDict['bump_left'] or 
            sensorDict['bump_right'] or
            sensorDict['virtual_wall']):
            print "Bump!"
            pici.drive(ser,-200,-200)
            sleep(1.0)

    pici.drive_straight(ser,500)
    sleep(0.1)

# stop driving, play stop song, turn off play light
pici.stop(ser)

ser.close()




