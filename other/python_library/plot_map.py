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
cmap = pics.cMap("./maps/maze_zig.txt")

ff = plt.figure(1)
picv.plotCmap(cmap)
plt.show()
ff.savefig('maze_zig.png',dpi=300)

