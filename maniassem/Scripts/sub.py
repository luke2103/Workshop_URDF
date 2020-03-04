#!/usr/bin/env python
import rospy
import pickle as pk
from std_msgs.msg import String
from beginner_tutorials.msg import custom_array
from builtins import input
import socket
import sys


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard {},{},{}".format(data.array1[0],data.array1[1],data.array1[2]))
    #msg = encodeData(data.array1)
    #assert isinstance(msg, str)
    #msg= msg.encode()
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener')

    rospy.Subscriber("chatter",custom_array, callback)

    # spin() simply keeps python from exiting until this node is stopped
    print "outside loop"
    while not rospy.is_shutdown():
            print "inside loop"	
            rospy.spin()

if __name__ == '__main__':
    listener()
