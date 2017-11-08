#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import rospy
import math
from raspimouse_ros.msg import LightSensorValues
from sensor_msgs.msg import LaserScan


def range_to_led(range_value):
    try:
        distance = int(range_value[0]*1000) # distance[mm]
        if distance < 4:
            distance = 8 - distance

        led_value = int( 761000 / math.pow(distance,1.66) )

        if led_value > 4000:
            led_value = 4000
        if led_value < 15:
            led_value = 15
    except:
        led_value = 15 
    # rospy.loginfo(led_value)
    return led_value
    # return distance

def write_to_file(data):
    try:
        with open("/dev/rtlightsensor0", "w") as f:
            print >> f, "%d %d %d %d" % tuple(data)
    except:
        rospy.logerr("failed to open rtlightsensor0")

def sensor1_callback(data):
    led_val[0] = range_to_led(data.ranges)
    # write_to_file(led_val)

def sensor2_callback(data):
    led_val[1] = range_to_led(data.ranges)
    # write_to_file(led_val)

def sensor3_callback(data):
    led_val[2] = range_to_led(data.ranges)
    # write_to_file(led_val)

def sensor4_callback(data):
    led_val[3] = range_to_led(data.ranges)
    write_to_file(led_val)

def listener():
    rospy.Subscriber("/raspimouse_on_gazebo/rf_scan", LaserScan, sensor1_callback)
    rospy.Subscriber("/raspimouse_on_gazebo/rs_scan", LaserScan, sensor2_callback)
    rospy.Subscriber("/raspimouse_on_gazebo/ls_scan", LaserScan, sensor3_callback)
    rospy.Subscriber("/raspimouse_on_gazebo/lf_scan", LaserScan, sensor4_callback)

if __name__ == "__main__":
    led_val = [15, 15, 15, 15]
    rospy.init_node("sensor_data_converter", anonymous=True)
    listener()
    rospy.spin()
