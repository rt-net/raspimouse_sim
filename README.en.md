[English](README.en.md) | [日本語](README.md)

# raspimouse_sim

[![industrial_ci](https://github.com/rt-net/raspimouse_sim/actions/workflows/industrial_ci.yml/badge.svg?branch=ros2)](https://github.com/rt-net/raspimouse_sim/actions/workflows/industrial_ci.yml)

ROS 2 package suite for simulating the Raspberry Pi Mouse in Gazebo

![](https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_color_objects_world.png)

## Table of Contents

- [raspimouse\_sim](#raspimouse_sim)
  - [Table of Contents](#table-of-contents)
  - [Supported ROS distributions](#supported-ros-distributions)
  - [Requirements](#requirements)
  - [Installation](#installation)
    - [Binary Installation](#binary-installation)
    - [Source Build](#source-build)
  - [QuickStart](#quickstart)
  - [Packages](#packages)
    - raspimouse_sim
    - raspimouse_fake
    - raspimouse_gazebo
  - [How to Use Examples](#how-to-use-examples)
    - Joystick Control
    - Object Tracking
    - Camera Line Follower
    - SLAM & Navigation
  - [License](#license)
  - [Contributing](#contributing)
  - [Acknowledgements](#acknowledgements)

## Supported ROS distributions

### ROS 2

- [Humble Hawksbill](https://github.com/rt-net/raspimouse_sim/tree/humble)
- [Jazzy Jalisco](https://github.com/rt-net/raspimouse_sim/tree/jazzy)

## Requirements

- OS
  - Ubuntu Desktop 24.04
- ROS 2
  - ROS 2 Jazzy Jalisco
- Gazebo
  - Gazebo Sim 8.x

## Installation

### Binary Installation

```bash
sudo apt install ros-jazzy-raspimouse-sim
```

### Source Build

```bash
# Create workspace directory
mkdir -p ~/ros2_ws/src && cd ~/ros2_ws/src

# Clone package
git clone -b $ROS_DISTRO https://github.com/rt-net/raspimouse_sim.git

# Install dependencies
rosdep install -r -y -i --from-paths .

# Build & Install
cd ~/ros2_ws
colcon build --symlink-install
source ~/ros2_ws/install/setup.bash
```

## QuickStart

The following command launches the Gazebo simulator and displays the Raspberry Pi Mouse model.

```sh
ros2 launch raspimouse_gazebo raspimouse_with_emptyworld.launch.py
```

## Packages

- raspimouse_sim
  - Manages meta-information for the packages in this repository.
- raspimouse_fake
  - This package simulates the motor control interface of the Raspberry Pi Mouse.
- raspimouse_gazebo
  - This package provides models and scripts to set up a simulation environment on [Gazebo](https://gazebosim.org).

## How to Use Examples

Detailed usage of the sample program is explained in the README of the `raspimouse_gazebo` package.

- raspimouse_gazebo
  - [Joystick Control](./raspimouse_gazebo/README.md#joystick-control)
  - [Object Tracking](./raspimouse_gazebo/README.md#object-tracking)
  - [Camera Line Follower](./raspimouse_gazebo/README.md#camera_line_follower)
  - [SLAM & Navigation](./raspimouse_gazebo/README.md#slam--navigation)

## License

(C) 2016 RT Corporation \<support@rt-net.jp\>

Each file is licensed as stated in their headers.  
If no license is specified, the file is licensed under the MIT License.  
The full license text is available in the [LICENSE](./LICENSE) file or at [https://opensource.org/license/MIT](https://opensource.org/license/MIT).

## Contributing

- This software is open source, but its development is not open.
- This software is essentially provided as open source software on an “AS IS” (in its current state) basis.
- No free support is available for this software.
- Requests for bug fixes and corrections of typographical errors are always accepted; however, requests for additional features will be subject to our internal guidelines. For further details, please refer to the [Contribution Guidelines](https://github.com/rt-net/.github/blob/master/CONTRIBUTING.md).

### Acknowledgements

This repository is developed based on files from the following repository.

- [CIR-KIT/fourth_robot_pkg]( https://github.com/CIR-KIT/fourth_robot_pkg )
  - author
    - RyodoTanaka
  - maintainer
    - RyodoTanaka
  - BSD ([BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause))
  - For details, see [package.xml](https://github.com/CIR-KIT/fourth_robot_pkg/blob/indigo-devel/fourth_robot_control/package.xml).
- [yujinrobot/kobuki]( https://github.com/yujinrobot/kobuki )
  - authors
    - Daniel Stonier
    - Younghun Ju
    - Jorge Santos Simon
    - Marcus Liebhardt
  - maintainer
    - Daniel Stonier
  - BSD ([BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause))
  - For details, see [package.xml](https://github.com/yujinrobot/kobuki/blob/melodic/kobuki/package.xml).