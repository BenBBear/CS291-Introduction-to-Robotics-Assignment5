import serial, sys, time, math
from time import sleep
import pici
reload(pici)

# Open the Create's serial port
sPort = '/dev/ttyUSB0'
#sBaud = 9600
sBaud = 57600
ser = serial.Serial(sPort,sBaud, timeout=1.0)


# Start in Passive mode
# Have to give it the start commadn
pici.tx_bytelist(ser,[128])

# Go to full mode
pici.tx_bytelist(ser,[132])

# Create and play a two note song 
pici.tx_bytelist(ser,[140,0,2,48,32,36,16])
pici.tx_bytelist(ser,[141,0])
#sleep(0.1)
#ser.flushInput()
#ser.flushOutput()

sensorDict = pici.getSensorsAll(ser)
print sensorDict

# drive
#pici.drive(ser,100,100)
#pici.drive_straight(ser,200)
#pici.turn(ser,200,cw=False)
#pici.turn(ser,200)
pici.ledAdvancePlay(ser, True, False)
sleep(1.0)
pici.ledAdvancePlay(ser, False, True)
sleep(1.0)
pici.ledAdvancePlay(ser, True, True)
sleep(1.0)
pici.ledPower(ser, 255, 255)
sleep(1.0)
pici.ledPower(ser, 255, 128)
sleep(1.0)

# stop
pici.drive(ser,0,0)

sensorDict = pici.getSensorsAll(ser)
print sensorDict

# Create and play a two note song 
pici.tx_bytelist(ser,[140,0,2,36,32,48,16])
pici.tx_bytelist(ser,[141,0])

ser.close()




