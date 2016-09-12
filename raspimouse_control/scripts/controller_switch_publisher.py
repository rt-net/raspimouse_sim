#!/usr/bin/env python

import rospy
from raspimouse_ros.msg import Switches

rospy.init_node('swich_publisher')
pub = rospy.Publisher('/raspimouse/switches', Switches, queue_size=1)
while not rospy.is_shutdown():
    sw = Switches()
    sw_input = raw_input('z: front, x: center, c: rear > ')
    if 'z' in sw_input:
        sw.front = 1
    if 'x' in sw_input:
        sw.center = 1
    if 'c' in sw_input:
        sw.rear = 1
    if 'q' in sw_input:
        break
    print sw_input
    pub.publish(sw)

