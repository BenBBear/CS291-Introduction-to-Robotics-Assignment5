import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle, Wedge, Polygon
from matplotlib.collections import PatchCollection
import time

import pics
reload(pics)
import pici
reload(pici)
#import picv
#reload(picv)

import logging, sys, time
from time import sleep
import threading as thrd
numeric_level = getattr(logging,"INFO")  # get numeric value for logging
logging.basicConfig(stream=sys.stdout, 
                        level=numeric_level,
                        format='%(levelname)s:%(message)s')

# Build a map
import picv
reload(picv)
cmap = pics.cMap("./maps/maze_L.txt")
# Build map by hand or give it a file name above
#cmap.add_wall(0.0,  0.5, 4.0,  0.5)
#cmap.add_wall(0.0, -0.5, 5.0, -0.5 )
#cmap.add_wall(4.0,  0.5, 4.0,  5.0)
#cmap.add_wall(5.0, -0.5, 5.0,  5.0 )

# Create the sim opject
ser = pics.Create(cmap=cmap)
ser.open()

# Start the animation thread
tt= picv.ani_start(ser,cmap)

# Loop for some amount of time
t0 = time.time()
tEnd = 60
while ( (time.time()-t0) < tEnd):
    sensorDict = pici.getSensorsAll(ser)
    #print sensorDict
    # If we hit a bump - backup and turn for some time
    if (sensorDict['bump_left'] and sensorDict['bump_right']):
        print "Backing up, turning left"
        pici.driveFwdAngVel(ser, -200, 1)
        sleep(1.0)
    elif sensorDict['bump_left']:
        print "Backing up, turning right"
        pici.driveFwdAngVel(ser, -200, -1)
        sleep(1.0)
    elif sensorDict['bump_right']:
        print "Backing up, turning left"
        pici.driveFwdAngVel(ser, -200, 1)
        sleep(1.0)
    print "Driving forwards"
    pici.drive_direct(ser,500,500)
    #pici.drive_straight(ser,500)
    sleep(0.1)

# allows the program to stop when you close the figure window
tt.join()
