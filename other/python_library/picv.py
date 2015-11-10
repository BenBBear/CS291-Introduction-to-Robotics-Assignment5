'''
Visualization using matplotlib
'''
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle, Wedge, Polygon
from matplotlib.collections import PatchCollection
import threading as thrd
from math import *
import pics
reload(pics)
import pici
reload(pici)



def plotWall(wall,virtwall=False):
    plt.hold(True)
    
    if virtwall:
        ltype = 'g-'
    else:
        ltype = 'k-'
    plt.plot([wall.x1, wall.x2], [wall.y1, wall.y2], ltype, lw=2)
        

def plotCmap(cmap):
    for wall in cmap.walls:
        plotWall(wall)
    for vwall in cmap.virtwalls:
        plotWall(vwall,virtwall=True)
    plt.xlabel('X [m]')
    plt.ylabel('Y [m]')
    plt.title(cmap.name)
'''
These functions are for the animation of the create
'''
def update_hline(ser,hline):
    x1 = ser.X
    y1 = ser.Y
    dx = (ser.L*1e-3)/2   # radius of roomba
    x2 = x1+dx*cos(ser.A*pi/180)
    y2 = y1+dx*sin(ser.A*pi/180)
    hline[0].set_data([x1, x2],[y1, y2])
    return 

def update_create(num,ser,cc,hline):
    cc.center = ser.X, ser.Y
    update_hline(ser,hline)
    return cc, hline

def ani(ser,cmap):
    fig1 = plt.figure()
    ax = fig1.add_subplot(111,aspect='equal')
    if cmap is not None:
        plotCmap(cmap)

    # expand the scale slightly
    aa = plt.axis()
    aa = list(aa)
    for ii in range(len(aa)):
        aa[ii]=aa[ii]*1.1
    plt.axis(aa)
        
    #plt.ylim((-6,6))
    #plt.xlim((-6,6))
    # Cicle for roomba
    cc = Circle((0,0),radius=(ser.L*1e-3)/2, facecolor='blue',lw=2, alpha=0.5)
    ax.add_patch(cc)
    # plot line at heading
    hline = plt.plot([0,0],[0,0],'w-',lw=2)
    print(type(hline))
    update_hline(ser,hline)

    c_ani = animation.FuncAnimation(fig1, update_create, 10, 
                                    fargs = (ser,cc,hline), interval = 200,
                                    blit=False)
    plt.show()

def ani_start(ser,cmap=None):
    tt = thrd.Thread(target=ani, args=(ser,cmap))
    tt.daemon = True
    tt.start()
    return tt

    

