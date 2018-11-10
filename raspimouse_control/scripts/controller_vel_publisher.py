#!/usr/bin/env python
# -*- coding: utf-8 -*-

# MIT License 2016-2017 (C) Tiryoh<tiryoh@gmail.com>

import rospy
from geometry_msgs.msg import Twist

if __name__ == '__main__':
    rospy.init_node('vel_publisher')
    pub = rospy.Publisher('/raspimouse_on_gazebo/diff_drive_controller/cmd_vel', Twist, queue_size=10)
    try:
        while not rospy.is_shutdown():
            vel = Twist()
            direction = raw_input('w: forward, s: backward, a: left, d: right, q: quit > ')
            if 'w' in direction:
                vel.linear.x = 0.18
            if 's' in direction:
                vel.linear.x = -0.18
            if 'a' in direction:
                vel.angular.z = 90*3.14/180.0
            if 'd' in direction:
                vel.angular.z = -90*3.14/180.0
            if 'q' in direction:
                break
            print vel
            pub.publish(vel)
    except rospy.ROSInterruptException:
            pass

