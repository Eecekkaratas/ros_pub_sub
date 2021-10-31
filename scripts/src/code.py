#!/usr/bin/env python

import rospy

from std_msgs.msg import String


def publisher():

	pub = rospy.Publisher('robotics_ozu_rover_first_topic' ,String, queue_size = 10)
	rospy.init_node('publisher_node' , anonymous=False)
	rate = rospy.Rate(10) #10 hz

	while not rospy.is_shutdown():

		msg = "first publisher code! :"
		rospy.loginfo(msg)
		pub.publish(msg)
		rate.sleep()


if __name__ == "__main__":

	publisher()
