#!/usr/bin/env python
import rospy
import pickle as pk
from std_msgs.msg import String
from beginner_tutorials.msg import custom_array ##custom message

def compute_angles(t1,t2,t3):
	
	theta_1 = t1
	theta_2 = t2
	theta_3 = t3
	return theta_1, theta_2, theta_3 

def talker():
		pub = rospy.Publisher('chatter',custom_array, queue_size=10)
		rospy.init_node('talker', anonymous=True)
		rate = rospy.Rate(10) # 10hz
		msg = custom_array()
		while not rospy.is_shutdown():
			t1 = int(input("Enter theta1 "))
			t2 = int(input("Enter theta2 "))
			t3 = int(input("Enter theta3 "))
			# hello_str = "hello world %s" % rospy.get_time()
			msg.array1.extend(compute_angles(t1,t2,t3))
			rospy.loginfo(msg)
			pub.publish(msg)
			msg.array1 = []
			rate.sleep()
   
if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass





	