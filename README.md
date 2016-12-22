# raspimouse_sim 

ROS package suite for Raspberry Pi Mouse Simulator runs on Gazebo

## Requirements

requires the following to run:

* Ubuntu
  * Ubuntu Trusty 14.04
* ROS
  * ROS Indigo
* Gazebo
  * Gazebo 2.x
* ROS Package
  * [raspimouse_ros](https://github.com/ryuichiueda/raspimouse_ros)

## Installation

Install the latest stable version of ros_control.

```
sudo apt-get install ros-indigo-desktop-full ros-indigo-gazebo-ros-control ros-indigo-ros-controllers
```

Download the dependent ROS package into `~/catkin_ws/src` and build it.

```
cd ~/catkin_ws/src
git clone https://github.com/ryuichiueda/raspimouse_ros.git
cd ~/catkin_ws && catkin_make && source ~/catkin_ws/devel/setup.bash
```

Download this repository and build it.

```
cd ~/catkin_ws/src
git clone https://github.com/rt-net/raspimouse_sim.git
cd ~/catkin_ws && catkin_make && source ~/catkin_ws/devel/setup.bash
```

## License

This repository is licensed under the MIT license, see [LICENSE]( ./LICENSE ).

Unless attributed otherwise, everything is under the MIT license.

### Includings

* [CIR-KIT/fourth_robot_pkg]( https://github.com/CIR-KIT/fourth_robot_pkg ) - BSD (BSD 3-Clause License)
  * urdf model xacro files
  * ros_control definition files
* [yujinrobot/kobuki]( https://github.com/yujinrobot/kobuki ) - BSD (BSD 3-Clause License)
  * launch files
