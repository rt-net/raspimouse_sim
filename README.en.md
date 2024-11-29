[English](README.en.md) | [日本語](README.md)

# raspimouse_sim

[![industrial_ci](https://github.com/rt-net/raspimouse_sim/actions/workflows/industrial_ci.yml/badge.svg?branch=ros2)](https://github.com/rt-net/raspimouse_sim/actions/workflows/industrial_ci.yml)

ROS 2 package suite for Raspberry Pi Mouse Simulator runs on Gazebo

![](https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_color_objects_world.png)

**This branch is intended for ROS 2 Jazzy. For other distributions, please refer to the corresponding branches listed below.**

- ROS 2 Humble ([humble](https://github.com/rt-net/raspimouse_sim/tree/humble))


## Requirements

requires the following to run:

* Ubuntu
  * Ubuntu 24.04 Noble Numbat
* ROS 2
  * ROS 2 Jazzy Jalisco
* Gazebo
  * Gazebo Sim 8.x
* ROS 2 Package
  * ros-jazzy-desktop-full

## Installation

Download this ROS 2 package.

```sh
cd ~/ros2_ws/src
git clone -b $ROS_DISTRO https://github.com/rt-net/raspimouse_sim.git
```

Download the dependent ROS 2 packages.

```sh
cd ~/ros2_ws/src
git clone -b $ROS_DISTRO https://github.com/rt-net/raspimouse_ros2_examples.git
git clone -b $ROS_DISTRO https://github.com/rt-net/raspimouse_slam_navigation_ros2.git
git clone -b $ROS_DISTRO https://github.com/rt-net/raspimouse_description.git
rosdep install -r -y -i --from-paths raspimouse*
```

Build this package using `colcon`.

```sh
cd ~/ros2_ws
colcon build --symlink-install
source ~/ros2_ws/install/setup.bash
```

## QuickStart

After building this package, run the following commands.

```sh
ros2 launch raspimouse_gazebo raspimouse_with_emptyworld.launch.py
```

## Examples

These exsamples require [raspimouse_ros2_examples](https://github.com/rt-net/raspimouse_ros2_examples) to operate.

### Joystick Controll

Terminal 1:

```sh
ros2 launch raspimouse_gazebo raspimouse_with_emptyworld.launch.py
```

Terminal 2:

```sh
ros2 launch raspimouse_ros2_examples teleop_joy.launch.py joydev:="/dev/input/js0" joyconfig:=f710 mouse:=false
```

![](https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_joystick.gif)

### Object Tracking

Terminal 1:

```sh
ros2 launch raspimouse_gazebo raspimouse_with_color_objects.launch.py use_rgb_camera:=true
```

Terminal 2:

```sh
ros2 launch raspimouse_ros2_examples object_tracking.launch.py mouse:=false use_camera_node:=false
```

![](https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_object_tracking.gif)

### camera_line_follower

Terminal 1:

```sh
ros2 launch raspimouse_gazebo raspimouse_with_line_follower_field.launch.py use_rgb_camera:=true camera_downward:=true
```

Terminal 2:

```sh
ros2 launch raspimouse_ros2_examples camera_line_follower.launch.py mouse:=false use_camera_node:=false
```

Terminal 3: Start

```sh
ros2 topic pub --once /switches raspimouse_msgs/msg/Switches "{switch0: false, switch1: false, switch2: true}"
```

Terminal 3: Stop
```sh
ros2 topic pub --once /switches raspimouse_msgs/msg/Switches "{switch0: true, switch1: false, switch2: false}"
```

For information on parameters in camera line follower, click [here](https://github.com/rt-net/raspimouse_ros2_examples/blob/master/README.en.md#parameters).

![](https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_camerafollower_short.gif)

### SLAM & Navigation

This exsample requires [raspimouse_slam_navigation_ros2](https://github.com/rt-net/raspimouse_slam_navigation_ros2) to operate.

#### SLAM

Terminal 1:
```sh
ros2 launch raspimouse_gazebo raspimouse_with_lakehouse.launch.py lidar:=urg
```
The lidar option supports `urg`, `lds`, and `rplidar`.

Terminal 2:
```sh
ros2 launch raspimouse_ros2_examples teleop_joy.launch.py joydev:="/dev/input/js0" joyconfig:=f710 mouse:=false
```

Terminal 3:
```sh
ros2 launch raspimouse_slam pc_slam.launch.py
```

![](https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_slam.png)

Terminal 4:
```sh
ros2 run nav2_map_server map_saver_cli -f ~/MAP_NAME
```

![](https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_slam_short.gif)

#### Navigation

Terminal 1:
```sh
ros2 launch raspimouse_gazebo raspimouse_with_lakehouse.launch.py lidar:=urg
```
The lidar option supports `urg`, `lds`, and `rplidar`.

Terminal 2:
```sh
ros2 launch raspimouse_navigation pc_navigation.launch.py use_sim_time:=true map:=$HOME/MAP_NAME.yaml
```

![](https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_navigation_short.gif)

## Model data list

### course_curve_50x50cm
Curve course panel for line following.
Panel size is 50 cm x 50 cm and line width is 4 cm.

![](./raspimouse_gazebo/models/course_curve_50x50cm/meshes/course_curve.jpg)

### course_straight_50x50cm
Straight course panel for line following.
Panel size is 50 cm x 50 cm and line width is 4 cm.

![](./raspimouse_gazebo/models/course_straight_50x50cm/meshes/course_straight.jpg)

### cube_*cm_color-name
Each cube is 5 cm, 7.5 cm, 10 cm, and 15 cm, 30 cm on a side.
The cube colors are red, yellow, blue, green and black.

![](https://rt-net.github.io/images/raspberry-pi-mouse/color_objects.png)

### about dae files
The dae file is edited in Blender 4.0.

## License

This repository is licensed under the MIT license, see [LICENSE]( ./LICENSE ).
Unless attributed otherwise, everything in this repository is under the MIT license.

### Acknowledgements

* [CIR-KIT/fourth_robot_pkg]( https://github.com/CIR-KIT/fourth_robot_pkg )
  * author
    * RyodoTanaka
  * maintainer
    * RyodoTanaka
  * BSD ([BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause))
  * See [package.xml](https://github.com/CIR-KIT/fourth_robot_pkg/blob/indigo-devel/fourth_robot_control/package.xml) for details.
* [yujinrobot/kobuki]( https://github.com/yujinrobot/kobuki )
  * authors
    * Daniel Stonier
    * Younghun Ju
    * Jorge Santos Simon
    * Marcus Liebhardt
  * maintainer
    * Daniel Stonier
  * BSD ([BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause))
  * See [package.xml](https://github.com/yujinrobot/kobuki/blob/melodic/kobuki/package.xml) for details。
