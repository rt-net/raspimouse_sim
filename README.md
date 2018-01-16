# raspimouse_sim 

[![Build Status](https://travis-ci.org/rt-net/raspimouse_sim.svg?branch=indigo-devel)](https://travis-ci.org/rt-net/raspimouse_sim)

ROS package suite for Raspberry Pi Mouse Simulator runs on Gazebo

日本語版READMEは[こちら](./README.ja.md)です。

Quick Startは[こちら](https://github.com/rt-net/raspimouse_sim/wiki/quickstart)です。

チュートリアルと詳細なセットアップ方法は[Wiki](https://github.com/rt-net/raspimouse_sim/wiki)にまとめています。


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
  * ros-indigo-desktop-full
  * ros-indigo-gazebo-ros-control
  * ros-indigo-ros-controllers

## Installation

```
bash -exv -c "$(curl -sSfL https://git.io/raspimouse-sim-installer)"
```

## Screenshots

### moving in sample maze

![](./docs/images/raspimouse_samplemaze.png)

### moving with URG

![](./docs/images/raspimouse_urg.png)

## License

This repository is licensed under the MIT license, see [LICENSE]( ./LICENSE ).

Unless attributed otherwise, everything is under the MIT license.

### Includings & References

* [CIR-KIT/fourth_robot_pkg]( https://github.com/CIR-KIT/fourth_robot_pkg ) - BSD (BSD 3-Clause License)
  * urdf model xacro files
  * ros_control definition files
* [yujinrobot/kobuki]( https://github.com/yujinrobot/kobuki ) - BSD (BSD 3-Clause License)
  * launch files
