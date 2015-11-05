#!/usr/bin/env python
import rospy
import pici
import serial
import constant as C
from std_msgs.msg import Int8,Bool
import sys



VELOCITYCHANGE = 200
ANGULARCHANGE = 200


def start_driver(sPort):
    sBaud = 57600
    ser = serial.Serial(sPort,sBaud, timeout=1.0)

    def topic_song_callback(msg):
        if msg.data:
            pici.playSongStart(ser);
        else:
            pici.playSongStop(ser);    

    def topic_move_callback(msg):
        d = msg.data        
        if d == C.MOVE_DOWN:
            pici.drive_straight(ser,-VELOCITYCHANGE);
        if d == C.MOVE_UP:
            pici.drive_straight(ser,VELOCITYCHANGE);
        if d == C.MOVE_LEFT:
            pici.turn(ser,ANGULARCHANGE,cw=False)
        if d == C.MOVE_RIGHT:
            pici.turn(ser,ANGULARCHANGE,cw=True)
        
        

    
    rospy.init_node('driver', anonymous=True)
    rospy.Subscriber("/irobot/song", Bool, topic_song_callback);
    rospy.Subscriber("/irobot/move", Int8, topic_move_callback);
    rospy.spin()
     

     
if __name__ == '__main__':
    if len(sys.argv) < 2:
        start_driver('/dev/ttyUSB0');
    else:
        start_driver(sys.argv[1]);
        
