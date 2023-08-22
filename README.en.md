[English](README.en.md) | [日本語](README.md)

# raspimouse_sim

ROS package suite for Raspberry Pi Mouse Simulator runs on Gazebo

![](https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_samplemaze_animation.gif)

## ROS Package Status

| main develop<br>(master)|Noetic + Ubuntu Focal<br>(noetic-devel)|
|:---:|:---:|
|[![industrial_ci](https://github.com/rt-net/raspimouse_sim/workflows/industrial_ci/badge.svg?branch=master)](https://github.com/rt-net/raspimouse_sim/actions?query=branch%3Amaster+workflow%3Aindustrial_ci)|[![industrial_ci](https://github.com/rt-net/raspimouse_sim/workflows/industrial_ci/badge.svg?branch=noetic-devel)](https://github.com/rt-net/raspimouse_sim/actions?query=branch%3Anoetic-devel+workflow%3Aindustrial_ci)|

The follwing branches are not maintained.

* rpim_book_version
* indigo-devel
* kinetic-devel
* melodic-devel

## Requirements

requires the following to run:

* Ubuntu
  * Ubuntu Focal Fossa 20.04.*
* ROS
  * ROS Noetic Ninjemys
* Gazebo
  * Gazebo 11.x
* ROS Package
  * ros-noetic-desktop-full

## Installation

Download this ROS package.

```
cd ~/catkin_ws/src
git clone https://github.com/rt-net/raspimouse_sim.git
```

Download the dependent ROS packages.

```
cd ~/catkin_ws/src
git clone https://github.com/ryuichiueda/raspimouse_ros_2.git
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

### SLAM

```
# 1st terminal
roslaunch raspimouse_gazebo raspimouse_with_willowgarage.launch
# 2nd terminal
roslaunch raspimouse_ros_examples slam_gmapping.launch
# 3rd terminal
roslaunch raspimouse_ros_examples teleop.launch key:=true mouse:=false
```

![](https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_urg_slam_gmapping.png)

[rt-net/raspimouse_ros_examples](https://github.com/rt-net/raspimouse_ros_examples) is required to launch nodes in raspimouse_ros_examples.  
Run the following commands to install it.

```
cd ~/catkin_ws/src
git clone https://github.com/rt-net/raspimouse_ros_examples.git
rosdep install -r -y -i --from-paths raspimouse*
cd ~/catkin_ws && catkin_make
source ~/catkin_ws/devel/setup.bash
```


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
