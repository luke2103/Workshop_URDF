#!/usr/bin/env python
import rospy
import pickle as pk
from std_msgs.msg import String
from beginner_tutorials.msg import custom_array

from sensor_msgs.msg import JointState
from std_msgs.msg import Header

import numpy as np
import math 
import time

pi_by_2 = math.pi/2
pi = math.pi
PI = 3.14159265359

##Variables
link1_length = 2.5
correction_factor = 0
link_length_1 = 12
link_length_2 = 9.5

def compute_angles(x,y,z):
	
	theta3 = (math.acos((x**2 + y**2 + (z-link1_length)**2)/((link_length_2**2)+(link_length_1**2)) - 1)) 

	#Condition to eliminate divide by infinity error

	theta1 = (math.atan2(y,x))
	theta2 = math.atan2((z-link1_length),((x**2 + y**2)**0.5))-(theta3)/2
	if theta2<0:
		theta2+=(pi/2)
		theta3-=pi
	theta3+=pi/2

	theta1 = int(round(math.degrees(theta1)))
	theta2 = int(round(math.degrees(theta2)))
	theta3 = int(round(math.degrees(theta3)))

	print theta1," ",theta2," ",theta3

	return theta1, theta2, theta3 

def talker():
	joint1 = 0
	joint2 = 0
	joint3 = 0
	joint2 = joint2 - (pi/2)
	joint3 = joint3 - (pi/2)
	pub = rospy.Publisher('chatter',custom_array, queue_size=10)
	# rospy.init_node('talker', anonymous=True)
	# rate = rospy.Rate(10) # 10hz
	msg = custom_array()
	pub1 = rospy.Publisher('joint_states', JointState, queue_size=10)
	rospy.init_node('publisher')
	rate = rospy.Rate(10) # 10hz
	joint_str = JointState()
	joint_str.header = Header()

	time.sleep(1)
	joint_str.header.stamp = rospy.Time.now()
	joint_str.name = ['joint1', 'joint2', 'joint3']
	joint_str.position = [joint1, joint2, joint3]
	joint_str.velocity = []
	joint_str.effort = []
	pub1.publish(joint_str)
	rospy.loginfo(joint_str)


	while not rospy.is_shutdown():
		
		x = input("Enter x ")
		y = input("Enter y ")
		z = input("Enter z ")

		# # hello_str = "hello world %s" % rospy.get_time()
		msg.array1.extend(compute_angles(x,y,z))

		
		pub.publish(msg)
		rospy.loginfo(msg)
		# msg.array1 = []
		# 				# rate.sleep()
		joint1 = float(msg.array1[0])
		joint2 = float(msg.array1[1])
		joint3 = float(msg.array1[2])

		joint1 = PI*(joint1)/180
		joint2 = PI*(joint2)/180
		joint3 = PI*(joint3)/180

		joint2 = joint2 - (pi/2)
		joint3 = joint3 - (pi/2)
		msg.array1 = []
		joint_str.header.stamp = rospy.Time.now()
		joint_str.name = ['joint1', 'joint2', 'joint3']
		joint_str.position = [joint1,joint2,joint3]
		joint_str.velocity = [0.01,0.01,0.01]
		joint_str.effort = []
		pub1.publish(joint_str)
		rospy.loginfo(joint_str)
		rate.sleep()
   
if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass

# ##Compute angles from provided co-ordinates




	
