[English](README.en.md) | [日本語](README.md)

# raspimouse_gazebo

Gazebo上でシミュレーション環境を構築するためのモデルやスクリプトを提供するパッケージです。

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

Raspberry Pi Mouseをジョイスティックコントローラで操作します。

<img src=https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_joystick.gif width=500 />


端末1で次のコマンドを実行し、Gazeboシミュレータを起動します。

```sh
ros2 launch raspimouse_gazebo raspimouse_with_emptyworld.launch.py
```

端末2で次のコマンドを実行し、Raspberry Pi Mouseをジョイスティックコントローラで操作できます。

```sh
ros2 launch raspimouse_ros2_examples teleop_joy.launch.py joydev:="/dev/input/js0" joyconfig:=f710 mouse:=false
```

### Object Tracking

Raspberry Pi Mouseがオレンジ色（赤色）の物体を追従します。

<img src=https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_object_tracking.gif width=500 />


端末1で次のコマンドを実行し、色付きの立方体が配置されたワールドを表示します。

```sh
ros2 launch raspimouse_gazebo raspimouse_with_color_objects.launch.py use_rgb_camera:=true
```

端末2で次のコマンドを実行し、Raspberry Pi Mouseがオレンジ色（赤色）の物体を追従します。

```sh
ros2 launch raspimouse_ros2_examples object_tracking.launch.py mouse:=false use_camera_node:=false
```

### camera_line_follower

Raspberry Pi Mouseが、黒いラインを追従します。

カメラライントレースにおけるパラメータは[こちら](https://github.com/rt-net/raspimouse_ros2_examples?tab=readme-ov-file#parameters)を参照してください。

<img src=https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_camerafollower_short.gif width=500 />


端末1で次のコマンドを実行し、ライントレースのサンプルコースが配置されたワールドを表示します。
```sh
ros2 launch raspimouse_gazebo raspimouse_with_line_follower_field.launch.py use_rgb_camera:=true camera_downward:=true
```

端末2で次のコマンドを実行し、カメラライントレースのノードを起動します。
```sh
ros2 launch raspimouse_ros2_examples camera_line_follower.launch.py mouse:=false use_camera_node:=false
```

端末3で次のコマンドを実行し、Raspberry Pi Mouseを走行させます。
```sh
ros2 topic pub --once /switches raspimouse_msgs/msg/Switches "{switch0: false, switch1: false, switch2: true}"
```

次のコマンドを実行すると、Raspberry Pi Mouseが停止します。
```sh
ros2 topic pub --once /switches raspimouse_msgs/msg/Switches "{switch0: true, switch1: false, switch2: false}"
```

### SLAM & Navigation

Raspberry Pi MouseがLiDARを使用したSLAMとNavigationを行います。

> [!NOTE]
> 本サンプルの動作には、[raspimouse_slam_navigation_ros2](https://github.com/rt-net/raspimouse_slam_navigation_ros2) が必要です。

#### SLAM

SLAMによる自己位置推定と地図作成を行います。

<img src=https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_slam.png width=500 />
<img src=https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_slam_short.gif width=500 />


端末1で次のコマンドを実行し、`Lake House`のモデルが配置されたワールドを表示します。

> [!NOTE]
> `lidar`は`urg`、`lds`、`rplidar`のいずれかを指定してください。

```sh
ros2 launch raspimouse_gazebo raspimouse_with_lakehouse.launch.py lidar:=urg
```

端末2で次のコマンドを実行し、ジョイスティックコントローラでRaspberry Pi Mouseを手動操作します。

```sh
ros2 launch raspimouse_ros2_examples teleop_joy.launch.py joydev:="/dev/input/js0" joyconfig:=f710 mouse:=false
```

端末3で次のコマンドを実行し、SLAMを開始します。

```sh
ros2 launch raspimouse_slam pc_slam.launch.py
```

端末4で次のコマンドを実行し、作成した地図を保存します。

> [!NOTE]
> `MAP_NAME`は任意の名前を指定できます。

```sh
ros2 run nav2_map_server map_saver_cli -f ~/MAP_NAME
```

#### Navigation

作成した地図をもとにNavigationを行います。

<img src=https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_navigation_short.gif width=500 />

端末1で次のコマンドを実行し、`Lake House`のモデルが配置されたワールドを表示します。

> [!NOTE]
> `lidar`は`urg`、`lds`、`rplidar`のいずれかを指定してください。

```sh
ros2 launch raspimouse_gazebo raspimouse_with_lakehouse.launch.py lidar:=urg
```

端末2で次のコマンドを実行し、Navigationを開始します。

> [!NOTE]
> 引数`map`にはSLAMで作成した地図ファイルのパスを指定してください。

```sh
ros2 launch raspimouse_navigation pc_navigation.launch.py use_sim_time:=true map:=$HOME/MAP_NAME.yaml
```

## Model Data List

各種サンプルで使用しているモデルデータ一覧です。

> [!NOTE]
> daeファイルはBlender 4.0で編集されています。

- `course_curve_50x50cm`
  - ライントレース用の曲線コースパネルです。
  - パネルサイズは50cm x 50cm、線の幅は4cmです。

    <img src=../raspimouse_gazebo/models/course_curve_50x50cm/meshes/course_curve.jpg width=300 />

- `course_straight_50x50cm`
  - ライントレース用の直線コースパネルです。
  - パネルサイズは50cm x 50cm、線の幅は4cmです。
  
    <img src=../raspimouse_gazebo/models/course_straight_50x50cm/meshes/course_straight.jpg width=300 />

- `cube_*cm_color-name`
  - 色は赤、黄、青、緑、黒です。
  - それぞれ一辺5cm、7.5cm、10cm、15cm、30cmの立方体です。

    <img src=https://rt-net.github.io/images/raspberry-pi-mouse/color_objects.png width=300 />

