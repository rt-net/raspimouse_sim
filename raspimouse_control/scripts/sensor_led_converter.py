#!/usr/bin/env python

import sys, time, math, rospy
from raspimouse_ros.msg import LightSensorValues
from sensor_msgs.msg import LaserScan

def sensor1_callback(data):
    sensor1.ranges = data.ranges

def sensor2_callback(data):
    sensor2.ranges = data.ranges

def sensor3_callback(data):
    sensor3.ranges = data.ranges

def sensor4_callback(data):
    sensor4.ranges = data.ranges

def range2led(range_value):
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

def listener():
    sub1 = rospy.Subscriber('/raw_raspimouse/rf/scan', LaserScan, sensor1_callback)
    sub2 = rospy.Subscriber('/raw_raspimouse/rs/scan', LaserScan, sensor2_callback)
    sub3 = rospy.Subscriber('/raw_raspimouse/ls/scan', LaserScan, sensor3_callback)
    sub4 = rospy.Subscriber('/raw_raspimouse/lf/scan', LaserScan, sensor4_callback)

def talker():
    rospy.init_node('lightsensors')
    pub = rospy.Publisher('lightsensors', LightSensorValues, queue_size=1)
    r = rospy.Rate(10)
    if not rospy.is_shutdown():
        try:
            # rospy.loginfo(sensor1.ranges[0] * 1000)
            d = LightSensorValues()
            d.right_forward = range2led(sensor1.ranges)
            d.right_side = range2led(sensor2.ranges)
            d.left_side = range2led(sensor3.ranges)
            d.left_forward = range2led(sensor4.ranges)
            pub.publish(d)
        except:
            rospy.logerr("Converting Sensor Data Failed")

        r.sleep()

if __name__ == "__main__":
    # sensor[4] = [0.0,0.0,0.0,0.0]
    sensor1 = LaserScan()
    sensor2 = LaserScan()
    sensor3 = LaserScan()
    sensor4 = LaserScan()
    try:
        while not rospy.is_shutdown():
            listener()
            talker()
    except rospy.ROSInterruptException:
        pass

