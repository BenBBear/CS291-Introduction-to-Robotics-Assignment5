#!/usr/bin/env python
import rospy
import pici
import serial
import constant as C
from std_msgs.msg import Int8,Bool
import sys



VELOCITYCHANGE = 200
ANGULARCHANGE = 200


def mprint(x):
    print "[Error in Driver.py]" + x


def start_driver(sPort):
    sBaud = 57600
    try:        
        ser = serial.Serial(sPort,sBaud, timeout=1.0)
        print("Connected to " + sPort + " successfully.")
    except serial.serialutil.SerialException as e:
        mprint("Not be able to to device:"+sPort)
        mprint("\nGet Error:"+str(e))
        return

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
    # mprint(str(sys.argv))
    if len(sys.argv) < 4:
        start_driver('/dev/ttyUSB0');
    else:
        start_driver(sys.argv[1]);
        
