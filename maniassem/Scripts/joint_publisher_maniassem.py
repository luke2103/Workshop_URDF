#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState
from std_msgs.msg import Header
import time

PI = 3.14159265359

def talker():
    joint1 = 0
    joint2 = 0
    joint3 = 0
    joint2 = joint2 - (PI/2)
    joint3 = joint3 - (PI/2)
    pub = rospy.Publisher('joint_states', JointState, queue_size=10)
    rospy.init_node('joint_publisher_maniassem')
    rate = rospy.Rate(10) # 10hz
    joint_str = JointState()
    joint_str.header = Header()

    time.sleep(1)

    joint_str.header.stamp = rospy.Time.now()
    joint_str.name = ['joint1', 'joint2', 'joint3']
    joint_str.position = [joint1, joint2, joint3]
    joint_str.velocity = []
    joint_str.effort = []
    pub.publish(joint_str)
    rospy.loginfo(joint_str)

    while not rospy.is_shutdown():
        joint1 = float(input("\njoint1: "))
        joint2 = float(input("joint2: "))
        joint3 = float(input("joint3: "))
        joint1 = PI*(joint1)/180
        joint2 = PI*(joint2)/180
        joint3 = PI*(joint3)/180
	joint2= joint2 - (PI/2)
	joint3 = joint3 - (PI/2)
        joint_str.header.stamp = rospy.Time.now()
        joint_str.name = ['joint1', 'joint2', 'joint3']
        joint_str.position = [joint1, joint2, joint3]
        joint_str.velocity = [0.5]
        joint_str.effort = [1]
        pub.publish(joint_str)
        rospy.loginfo(joint_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
