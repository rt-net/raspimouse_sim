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

## Usage

After `git clone`, run git submodule update command shown below.

```
sudo apt install ros-kinetic-ros-control ros-kinetic-ros-controllers
git submodule update --init
```

In another way, add `--recursive` option when you clone repository.

## License

This repository is licensed under the MIT license, see [LICENSE]( ./LICENSE ).

Unless attributed otherwise, everything is under the MIT license.

### Include

* [ryuichiueda/raspimouse_ros]( https://github.com/ryuichiueda/raspimouse_ros ) - [MIT LICENSE]( https://github.com/ryuichiueda/raspimouse_ros/blob/v1.0/LICENSE )
  * msg files 
* [CIR-KIT/fourth_robot_pkg]( https://github.com/CIR-KIT/fourth_robot_pkg ) - BSD (BSD 3-Clause License)
  * urdf model xacro files
  * ros_control definition files
* [yujinrobot/kobuki]( https://github.com/yujinrobot/kobuki ) - BSD (BSD 3-Clause License)
  * launch files
