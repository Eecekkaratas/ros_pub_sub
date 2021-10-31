#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):

	msg = "First message is: " 
	rospy.loginfo(msg + data.data)
	

def subs():

	rospy.init_node('listener', anonymous=True)
	rospy.Subscriber('robotics_ozu_rover_first_topic', String, callback)
	rospy.spin()
	
if __name__ == '__main__':

	subs()
