[English](README.en.md) | [日本語](README.md)

# raspimouse_gazebo

This package provides models and scripts to set up a simulation environment in Gazebo.

![](https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_color_objects_world.png)

## Table of Contents

- [raspimouse\_gazebo](#raspimouse_gazebo)
  - [Table of Contents](#table-of-contents)
  - [How To Use Examples](#how-to-use-examples)
    - [Joystick Control](#joystick-control)
    - [Object Tracking](#object-tracking)
    - [Camera Line Follower](#camera_line_follower)
    - [SLAM & Navigation](#slam--navigation)
  - [Model data list](#etc-lifecycle-description等)

## How to Use Examples

### Joystick Control

Operates using a joystick controller.

<img src=https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_joystick.gif width=500 />

Run the following command in Terminal 1 to launch the Gazebo simulator.

```sh
ros2 launch raspimouse_gazebo raspimouse_with_emptyworld.launch.py
```

Run the following command in Terminal 2 to control the Raspberry Pi Mouse using a joystick controller.

```sh
ros2 launch raspimouse_ros2_examples teleop_joy.launch.py joydev:="/dev/input/js0" joyconfig:=f710 mouse:=false
```

[back to example list](#how-to-use-examples)

---

### Object Tracking

Follows an orange (red) object.

<img src=https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_object_tracking.gif width=500 />


Run the following command in Terminal 1 to launch a world with colored cubes.

```sh
ros2 launch raspimouse_gazebo raspimouse_with_color_objects.launch.py use_rgb_camera:=true
```

Run the following command in Terminal 2 to make the Raspberry Pi Mouse follow an orange (red) object.

```sh
ros2 launch raspimouse_ros2_examples object_tracking.launch.py mouse:=false use_camera_node:=false
```

[back to example list](#how-to-use-examples)

---

### camera_line_follower

Follows a black line.

For parameters used in camera-based line tracing, please refer to this [section](https://github.com/rt-net/raspimouse_ros2_examples?tab=readme-ov-file#parameters).


<img src=https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_camerafollower_short.gif width=500 />


Run the following command in Terminal 1 to launch a world with a sample course for line tracing.

```sh
ros2 launch raspimouse_gazebo raspimouse_with_line_follower_field.launch.py use_rgb_camera:=true camera_downward:=true
```

Run the following command in Terminal 2 to start the camera-based line tracing node.

```sh
ros2 launch raspimouse_ros2_examples camera_line_follower.launch.py mouse:=false use_camera_node:=false
```

Run the following command in Terminal 3 to start the Raspberry Pi Mouse's movement.

```sh
ros2 topic pub --once /switches raspimouse_msgs/msg/Switches "{switch0: false, switch1: false, switch2: true}"
```

Run the following command to stop the Raspberry Pi Mouse.

```sh
ros2 topic pub --once /switches raspimouse_msgs/msg/Switches "{switch0: true, switch1: false, switch2: false}"
```

[back to example list](#how-to-use-examples)

---

### SLAM & Navigation

Runs SLAM and navigation using LiDAR.

> [!NOTE]
> This sample requires [raspimouse_slam_navigation_ros2](https://github.com/rt-net/raspimouse_slam_navigation_ros2) to run.

#### SLAM

Runs SLAM for localization and mapping.

<img src=https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_slam.png width=500 />
<img src=https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_slam_short.gif width=500 />


Run the following command in Terminal 1 to launch a world with the `Lake House` model placed in it.

> [!NOTE]
> The `lidar` option supports `urg`, `lds`, and `rplidar`.

```sh
ros2 launch raspimouse_gazebo raspimouse_with_lakehouse.launch.py lidar:=urg
```

Run the following command in Terminal 2 to control the Raspberry Pi Mouse with a joystick controller.

```sh
ros2 launch raspimouse_ros2_examples teleop_joy.launch.py joydev:="/dev/input/js0" joyconfig:=f710 mouse:=false
```

Run the following command in Terminal 3 to run SLAM.

```sh
ros2 launch raspimouse_slam pc_slam.launch.py
```

Run the following command in Terminal 4 to save the created map.

> [!NOTE]
> You can specify any name for `MAP_NAME`.

```sh
ros2 run nav2_map_server map_saver_cli -f ~/MAP_NAME
```

#### Navigation

Navigate using the created map.

<img src=https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_navigation_short.gif width=500 />
 
Run the following command in Terminal 1 to launch a world with the `Lake House` model placed in it.

> [!NOTE]
> The `lidar` option supports `urg`, `lds`, and `rplidar`.

```sh
ros2 launch raspimouse_gazebo raspimouse_with_lakehouse.launch.py lidar:=urg
```

Run the following command in Terminal 2 to run Navigation.

> [!NOTE]
> Specify the path to the map file created by SLAM for the map argument.

```sh
ros2 launch raspimouse_navigation pc_navigation.launch.py use_sim_time:=true map:=$HOME/MAP_NAME.yaml
```

[back to example list](#how-to-use-examples)

---

## Model Data List

This is a list of model data used in the various samples.

> [!NOTE]
> The dae file is edited in Blender 4.0.

- `course_curve_50x50cm`
  - Curve course panel for line following.
  - Panel size is 50 cm x 50 cm and line width is 4 cm.

    <img src=../raspimouse_gazebo/models/course_curve_50x50cm/meshes/course_curve.jpg width=300 />

- `course_straight_50x50cm`
  - Straight course panel for line following.
  - Panel size is 50 cm x 50 cm and line width is 4 cm.
  
    <img src=../raspimouse_gazebo/models/course_straight_50x50cm/meshes/course_straight.jpg width=300 />

- `cube_*cm_color-name`
  - The cube colors are red, yellow, blue, green and black.
  - Each cube is 5 cm, 7.5 cm, 10 cm, and 15 cm, 30 cm on a side.

    <img src=https://rt-net.github.io/images/raspberry-pi-mouse/color_objects.png width=300 />

