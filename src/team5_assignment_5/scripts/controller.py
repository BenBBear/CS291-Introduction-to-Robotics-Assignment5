#!/usr/bin/env python
import rospy
import pici
import serial
import curses
import constant as C
from std_msgs.msg import Int8,Bool



    
def start_controller():
    screen = curses.initscr()
    curses.noecho()
    curses.curs_set(0)
    screen.keypad(1)
    
    songPub = rospy.Publisher ("/irobot/song", Bool, queue_size=10);
    movePub = rospy.Publisher("/irobot/move", Int8, queue_size=10);

        
    rospy.init_node('controller', anonymous=True)
    while not rospy.is_shutdown():
        screen.addstr("Press a key to controll iRobot")
        event = screen.getch()

        if event == curses.KEY_UP:            
            movePub.publish(C.MOVE_UP)
        elif event == curses.KEY_DOWN:
            movePub.publish(C.MOVE_DOWN)
        elif event == curses.KEY_LEFT:
            movePub.publish(C.MOVE_LEFT)
        elif event == curses.KEY_RIGHT:
            movePub.publish(C.MOVE_RIGHT)
        elif event == 115 or event == 83:
            songPub.publish(True)
        else:
            screen.addstr('\nThis is Not a Functional Key');
            
        screen.addstr('\n');

if __name__ == '__main__':
    start_controller();
