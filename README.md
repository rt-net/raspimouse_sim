[English](README.md) | [日本語](README.ja.md)

# raspimouse_sim

ROS package suite for Raspberry Pi Mouse Simulator runs on Gazebo

![](https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_samplemaze_animation.gif)

## ROS Package Status

| main develop<br>(master)|Kinetic + Ubuntu Xenial<br>(kinetic-devel)|Melodic + Ubuntu Bionic<br>(melodic-devel)|
|:---:|:---:|:---:|
|[![industrial_ci](https://github.com/rt-net/raspimouse_sim/workflows/industrial_ci/badge.svg?branch=master)](https://github.com/rt-net/raspimouse_sim/actions?query=branch%3Amaster+workflow%3Aindustrial_ci)|[![industrial_ci](https://github.com/rt-net/raspimouse_sim/workflows/industrial_ci/badge.svg?branch=kinetic-devel)](https://github.com/rt-net/raspimouse_sim/actions?query=branch%3Akinetic-devel+workflow%3Aindustrial_ci)|[![industrial_ci](https://github.com/rt-net/raspimouse_sim/workflows/industrial_ci/badge.svg?branch=melodic-devel)](https://github.com/rt-net/raspimouse_sim/actions?query=branch%3Amelodic-devel+workflow%3Aindustrial_ci)|

The follwing branches are not maintained.

* rpim_book_version
* indigo-devel


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

## License

This repository is licensed under the MIT license, see [LICENSE]( ./LICENSE ).  
Unless attributed otherwise, everything in this repository is under the MIT license.

### Acknowledgements

* [CIR-KIT/fourth_robot_pkg]( https://github.com/CIR-KIT/fourth_robot_pkg )
  * ```
    <author email="groadpg@gmail.com">RyodoTanaka</author>
    <maintainer email="groadpg@gmail.com">RyodoTanaka</maintainer>
    ```
  * BSD (BSD 3-Clause License)
* [yujinrobot/kobuki]( https://github.com/yujinrobot/kobuki )
  * ```
    <author>Daniel Stonier</author>
    <author>Younghun Ju</author>
    <author>Jorge Santos Simon</author>
    <author>Marcus Liebhardt</author>
    <maintainer email="stonier@yujinrobot.com">Daniel Stonier</maintainer>
    ```
  * BSD (BSD 3-Clause License)
