#!/usr/bin/env python
import rospy, math
from geometry_msgs.msg import Twist
import subprocess

def get_motor_freq():
    swfile ='/dev/rtmotoren0'
    lfile = '/dev/rtmotor_raw_l0'
    rfile = '/dev/rtmotor_raw_r0'
    vel = Twist()
    sound_count = 0
    while not rospy.is_shutdown():
        try:
            with open(swfile,'r') as f:
                motor_power_status = f.readline().rstrip()
            if motor_power_status=='0':
                sound_count = 0
            if motor_power_status=='1' and sound_count == 0:
                subprocess.call("aplay ~/catkin_ws/src/raspimouse_sim/raspimouse_control/scripts/ms_sound.wav", shell=True)
                sound_count = 1
            if motor_power_status=='1':
                with open(lfile,'r') as lf,\
                open(rfile,'r') as rf:
                    lhz_str = lf.readline().rstrip()
                    rhz_str = rf.readline().rstrip()
                if len(lhz_str)==0:
                    print("Reset /dev/rtmotor_raw_l0")
                    with open(lfile,'w') as lf:
                        lf.write('0')
                if len(rhz_str)==0:
                    print("Reset /dev/rtmotor_raw_r0")
                    with open(rfile,'w') as rf:
                        rf.write('0')
                else:
                    try:
                        lhz = int(lhz_str)
                    except:
                        lhz = 0
                    try:
                        rhz = int(rhz_str)
                    except:
                        rhz = 0
                    vel.linear.x = (lhz+rhz)*9*math.pi/160000.0
                    vel.angular.z = (rhz-lhz)*math.pi/800.0
                    #print(vel)
                    pub.publish(vel)

        except rospy.ROSInterruptException:
            pass

if __name__ == "__main__":
    rospy.init_node('virtual_motors')
    pub = rospy.Publisher('/raspimouse_on_gazebo/diff_drive_controller/cmd_vel', Twist, queue_size=10)
    get_motor_freq()
    rospy.spin()
