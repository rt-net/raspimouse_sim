[English](README.md) | [日本語](README.ja.md)

# raspimouse_sim

ROS package suite for Raspberry Pi Mouse Simulator runs on Gazebo

![](https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_samplemaze_animation.gif)

## ROS Package Status

|Kinetic + Ubuntu Xenial|Melodic + Ubuntu Bionic|master|
|:---:|:---:|:---:|
|[![Build Status](https://travis-ci.org/rt-net/raspimouse_sim.svg?branch=kinetic-devel)](https://travis-ci.org/rt-net/raspimouse_sim)|[![Build Status](https://travis-ci.org/rt-net/raspimouse_sim.svg?branch=melodic-devel)](https://travis-ci.org/rt-net/raspimouse_sim)|[![Build Status](https://travis-ci.org/rt-net/raspimouse_sim.svg?branch=master)](https://travis-ci.org/rt-net/raspimouse_sim)|


## Requirements

requires the following to run:

* Ubuntu
  * Ubuntu Xenial Xerus 16.04.*
* ROS
  * ROS Kinetic Kame
* Gazebo
  * Gazebo 7.x
* ROS Package
  * ros-kinetic-desktop-full

or

* Ubuntu
  * Ubuntu Bionic Beaver 18.04.*
* ROS
  * ROS Melodic Morenia
* Gazebo
  * Gazebo 9.x
* ROS Package
  * ros-melodic-desktop-full

## Installation

Download this ROS package.

```
cd ~/catkin_ws/src
git clone https://github.com/rt-net/raspimouse_sim.git
```

Download the dependent ROS package.

```
cd ~/catkin_ws/src
git clone https://github.com/rt-net/raspimouse_description.git
rosdep install -r -y -i --from-paths raspimouse*
```

Build this package using `catkin_make`.

```
cd ~/catkin_ws && catkin_make
source ~/catkin_ws/devel/setup.bash
```

Download the hardware model data that will be used in Gazebo.

```
rosrun raspimouse_gazebo download_gazebo_models.sh
```

## QuickStart

After the installation, run the following commands.

```
rosrun raspimouse_control gen_dev_file.sh
roslaunch raspimouse_gazebo raspimouse_with_samplemaze.launch
```

Checkout [this page](https://github.com/rt-net/raspimouse_sim/wiki/quickstart) for details.

## Screenshots

### moving in sample maze

```
roslaunch raspimouse_gazebo raspimouse_with_samplemaze.launch
```

![](https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_samplemaze.png)

### moving with URG

```
roslaunch raspimouse_gazebo raspimouse_with_gasstand.launch
```

![](https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_urg.png)

## License

This repository is licensed under the MIT license, see [LICENSE]( ./LICENSE ).  
Unless attributed otherwise, everything in this repository is under the MIT license.

### Includings & References

* [CIR-KIT/fourth_robot_pkg]( https://github.com/CIR-KIT/fourth_robot_pkg ) - BSD (BSD 3-Clause License)
  * urdf model xacro files
  * ros_control definition files
* [yujinrobot/kobuki]( https://github.com/yujinrobot/kobuki ) - BSD (BSD 3-Clause License)
  * launch files
