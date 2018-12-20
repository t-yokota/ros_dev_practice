#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import LaserScan

class subLaserScan:
	def __init__(self):
		rospy.init_node('subLaserScan', anonymous=True)
		rospy.Subscriber('/scan', LaserScan, self.scanCallback)
	
	def scanCallback(self, scan):
		rospy.loginfo("len:%f", len(scan.ranges))
		for i in range(len(scan.ranges)):
			rospy.loginfo("val[%d]:%f", i, scan.ranges[i])

if __name__ ==  '__main__':
	try:
		sls = subLaserScan()
		rospy.spin()
	except rospy.ROSInterruptException: pass
