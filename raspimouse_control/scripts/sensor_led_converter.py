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
    hoge[0] = range_to_led(data.ranges)
    # write_to_file(hoge)

def sensor2_callback(data):
    hoge[1] = range_to_led(data.ranges)
    # write_to_file(hoge)

def sensor3_callback(data):
    hoge[2] = range_to_led(data.ranges)
    # write_to_file(hoge)

def sensor4_callback(data):
    hoge[3] = range_to_led(data.ranges)
    write_to_file(hoge)

def listener():
    rospy.Subscriber("/raw_raspimouse/rf/scan", LaserScan, sensor1_callback)
    rospy.Subscriber("/raw_raspimouse/rs/scan", LaserScan, sensor2_callback)
    rospy.Subscriber("/raw_raspimouse/ls/scan", LaserScan, sensor3_callback)
    rospy.Subscriber("/raw_raspimouse/lf/scan", LaserScan, sensor4_callback)

if __name__ == "__main__":
    hoge = [15, 15, 15, 15]
    rospy.init_node("sensor_data_converter", anonymous=True)
    listener()
    rospy.spin()
