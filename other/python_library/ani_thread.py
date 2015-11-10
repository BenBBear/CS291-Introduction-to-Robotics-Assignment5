import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle, Wedge, Polygon
from matplotlib.collections import PatchCollection
import threading as thrd
import pics
reload(pics)
import pici
reload(pici)

def update_create(num,ser,cc):
    cc.center = ser.X, ser.Y
    return cc, 

def ani(ser):
    fig1 = plt.figure()
    ax = fig1.add_subplot(111,aspect='equal')
    plt.ylim((-2,2))
    plt.xlim((-2,2))
    cc = Circle((0,0),radius=0.1)
    ax.add_patch(cc)
    
    c_ani = animation.FuncAnimation(fig1, update_create, 10, 
                                    fargs = (ser,cc), interval = 200,
                                    blit=False)
    
    plt.show()

def start(ser):
    tt = thrd.Thread(target=ani, args=(ser,))
    tt.daemon = True
    tt.start()
    return tt
