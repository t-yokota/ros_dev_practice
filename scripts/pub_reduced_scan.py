#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from sensor_msgs.msg import LaserScan

class reduceLaserScan:
	def __init__(self):
		rospy.init_node('reduceLaserScan', anonymous=True)
		rospy.Subscriber('/scan', LaserScan, self.scanCallback)
		self.pub_reduced_scan = rospy.Publisher('/scan/reduced', LaserScan)
	
	def scanCallback(self, scan):
		rmin = [0 , 315]
		rmax = [45, 360]
		reduced_scan = LaserScan()
		
		reduced_scan.header = scan.header
		reduced_scan.angle_min = scan.angle_min
		reduced_scan.angle_max = scan.angle_max	
		reduced_scan.angle_increment = scan.angle_increment
		reduced_scan.time_increment = scan.time_increment
		reduced_scan.scan_time = scan.scan_time
		reduced_scan.range_min = scan.range_min
		reduced_scan.range_max = scan.range_max
		reduced_scan.intensities = scan.intensities

		for i in range(len(scan.ranges)):
			if   i >= rmin[0] and i <= rmax[0]-1:
				reduced_scan.ranges.append(scan.ranges[i])
			elif i >= rmin[1] and i <= rmax[1]-1:
				reduced_scan.ranges.append(scan.ranges[i])
			else:
				reduced_scan.ranges.append(0)
			rospy.loginfo("val[%d]:%f", i, reduced_scan.ranges[i])

 		self.pub_reduced_scan.publish(reduced_scan)
		
if __name__ ==  '__main__':
	try:
		rls = reduceLaserScan()
		rospy.spin()
	except rospy.ROSInterruptException: pass
