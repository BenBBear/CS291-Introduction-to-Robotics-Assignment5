#!/usr/bin/env python
import rospy
import pici
import sys
import serial
import curses
import constant as C
from std_msgs.msg import Int8,Bool
import time


def mprint(x):
    print "[Error in Controller.py]" + str(x)


    
def start_controller():
    screen = curses.initscr()
    # screen = curses.newwin(20, 65, 0, 1)
    curses.noecho()
    curses.curs_set(0)
    screen.keypad(1)
    
    songPub = rospy.Publisher ("/irobot/song", Bool, queue_size=10);
    movePub = rospy.Publisher("/irobot/move", Int8, queue_size=10);
    
    
    rospy.init_node('controller', anonymous=True)
    time.sleep(1)
    screen.addstr("\nPress a key to controll iRobot :D")
    screen.addstr("\ns - play a song")
    screen.addstr("\nleft arrow - counter-clockwise rotate")
    screen.addstr("\nright arrow - clockwise rotate")
    screen.addstr("\nup arrow - move straight foward")
    screen.addstr("\ndown arrow - move straight backward")
    
    while not rospy.is_shutdown():
        try:
            screen.addstr("\n>> ")
            event = screen.getch()

            if event == curses.KEY_UP:            
                movePub.publish(C.MOVE_UP)
                screen.addstr("move fowards")
            elif event == curses.KEY_DOWN:
                movePub.publish(C.MOVE_DOWN)
                screen.addstr("move backwards")
            elif event == curses.KEY_LEFT:
                movePub.publish(C.MOVE_LEFT)
                screen.addstr("rotate counter-clockwise")
            elif event == curses.KEY_RIGHT:
                movePub.publish(C.MOVE_RIGHT)
                screen.addstr("rotate clockwise")
            elif event == 115 or event == 83:
                songPub.publish(True)
                screen.addstr("sing a song")
            else:
                screen.addstr('this is not a valid key');
        except:            
            screen.clear();
        

if __name__ == '__main__':
    start_controller();

