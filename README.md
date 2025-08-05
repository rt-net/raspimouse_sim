[English](README.en.md) | [日本語](README.md)

# raspimouse_sim

[![industrial_ci](https://github.com/rt-net/raspimouse_sim/actions/workflows/industrial_ci.yml/badge.svg?branch=ros2)](https://github.com/rt-net/raspimouse_sim/actions/workflows/industrial_ci.yml)

Gazebo上でシミュレートできるRaspberry Pi MouseのROS 2パッケージです。

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
  - [How To Use Examples](#how-to-use-examples)
    - [Joystick Controll](#joystick-controll)
    - [Object Tracking](#object-tracking)
    - [Camera Line Follower](#camera_line_follower)
    - [SLAM & Navigation](#slam--navigation)
  - [Mode data list](#etc-lifecycle-description等)
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

次のコマンドを実行するとGazeboシミュレータが起動します。

```sh
ros2 launch raspimouse_gazebo raspimouse_with_emptyworld.launch.py
```

## How to Use Examples

### Joystick Controll

Raspberry Pi Mouseをジョイスティックコントローラで操作します。


<img src=https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_joystick.gif width=500 />


端末1で次のコマンドを実行すると、Gazeboシミュレータが起動します。

```sh
ros2 launch raspimouse_gazebo raspimouse_with_emptyworld.launch.py
```

端末2で次のコマンドを実行すると、Raspberry Pi Mouseをジョイスティックコントローラで操作できます。
v
```sh
ros2 launch raspimouse_ros2_examples teleop_joy.launch.py joydev:="/dev/input/js0" joyconfig:=f710 mouse:=false
```

### Object Tracking

Raspberry Pi Mouseがオレンジ色（赤色）の物体を追従します。

<img src=https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_object_tracking.gif width=500 />


端末1で次のコマンドを実行すると、色付きの立方体が配置されたワールドが表示されます。

```sh
ros2 launch raspimouse_gazebo raspimouse_with_color_objects.launch.py use_rgb_camera:=true
```

端末2で次のコマンドを実行すると、Raspberry Pi Mouseがオレンジ色（赤色）の物体を追従します。

```sh
ros2 launch raspimouse_ros2_examples object_tracking.launch.py mouse:=false use_camera_node:=false
```

### camera_line_follower

Raspberry Pi Mouseが、床に描かれた黒いラインを追従します。

カメラライントレースにおけるパラメータは[こちら](https://github.com/rt-net/raspimouse_ros2_examples?tab=readme-ov-file#parameters)を参照してください。

<img src=https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_camerafollower_short.gif width=500 />


端末1で次のコマンドを実行すると、ライントレースのサンプルコースが配置されたワールドが表示されます。
```sh
ros2 launch raspimouse_gazebo raspimouse_with_line_follower_field.launch.py use_rgb_camera:=true camera_downward:=true
```

端末2で次のコマンドを実行すると、カメラライントレースのノードが起動します。
```sh
ros2 launch raspimouse_ros2_examples camera_line_follower.launch.py mouse:=false use_camera_node:=false
```

端末3で次のコマンドを実行すると、Raspberry Pi Mouseが走行を開始します。
```sh
ros2 topic pub --once /switches raspimouse_msgs/msg/Switches "{switch0: false, switch1: false, switch2: true}"
```

次のコマンドを実行すると、Raspberry Pi Mouseが停止します。
```sh
ros2 topic pub --once /switches raspimouse_msgs/msg/Switches "{switch0: true, switch1: false, switch2: false}"
```

### SLAM & Navigation

RapimouseがLiDARを使用したSLAMとNavigationを行います。

> [!NOTE]
> 本サンプルの動作には、[raspimouse_slam_navigation_ros2](https://github.com/rt-net/raspimouse_slam_navigation_ros2) が必要です。

#### SLAM

SLAMによる自己位置推定と地図作成を行います。

<img src=https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_slam.png width=500 />
<img src=https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_slam_short.gif width=500 />


端末1で次のコマンドを実行すると、`Lake House`のモデルが配置されたワールドが表示されます。

> [!NOTE]
> `lidar`は`urg`、`lds`、`rplidar`のいずれかを指定してください。

```sh
ros2 launch raspimouse_gazebo raspimouse_with_lakehouse.launch.py lidar:=urg
```

端末2で次のコマンドを実行すると、Raspberry Pi Mouseをジョイスティックコントローラで操作できます。

```sh
ros2 launch raspimouse_ros2_examples teleop_joy.launch.py joydev:="/dev/input/js0" joyconfig:=f710 mouse:=false
```

端末3で次のコマンドを実行すると、SLAMが実行されます。
```sh
ros2 launch raspimouse_slam pc_slam.launch.py
```

端末4で次のコマンドを実行すると、作成した地図を保存できます。

> [!NOTE]
> `MAP_NAME`は任意の名前を指定できます。

```sh
ros2 run nav2_map_server map_saver_cli -f ~/MAP_NAME
```

#### Navigation

作成した地図をもとにNavigationします。

<img src=https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_navigation_short.gif width=500 />

端末1で次のコマンドを実行すると、`Lake House`のモデルが配置されたワールドが表示されます。

> [!NOTE]
> `lidar`は`urg`、`lds`、`rplidar`のいずれかを指定してください。

```sh
ros2 launch raspimouse_gazebo raspimouse_with_lakehouse.launch.py lidar:=urg
```

端末2で次のコマンドを実行すると、Navigationが実行されます。

> [!NOTE]
> 引数`map`にはSLAMで作成した地図ファイルのパスを指定してください。

```sh
ros2 launch raspimouse_navigation pc_navigation.launch.py use_sim_time:=true map:=$HOME/MAP_NAME.yaml
```

## Packages

- raspimouse_sim
  - 本リポジトリ内の各種パッケージのメタ情報を管理します。
- raspimouse_fake
  - Raspberry Pi Mouseのモータ制御インターフェースを模擬するROS 2ライフサイクルコンポーネントノードを提供します。
- raspimouse_gazebo
  - Gazebo上で動作するシミュレーション環境を構築するためのモデルや設定ファイルを提供します。

## Model data list

各種サンプルで使用しているモデルデータ一覧です。

> [!NOTE]
> daeファイルはBlender 4.0で編集されています。

- `course_curve_50x50cm`
  -   ライントレース用の曲線コースパネルです。
  - パネルサイズは50cm x 50cm、線の幅は4cmです。

    <img src=./raspimouse_gazebo/models/course_curve_50x50cm/meshes/course_curve.jpg width=300 />

- `course_straight_50x50cm`
  - ライントレース用の直線コースパネルです。
  - パネルサイズは50cm x 50cm、線の幅は4cmです。
  
    <img src=./raspimouse_gazebo/models/course_straight_50x50cm/meshes/course_straight.jpg width=300 />

- `cube_*cm_color-name`
  - それぞれ一辺5cm、7.5cm、10cm、15cm、30cmの立方体です。
  - 色は赤、黄、青、緑、黒です。

    <img src=https://rt-net.github.io/images/raspberry-pi-mouse/color_objects.png width=300 />

## License

(C) 2016 RT Corporation \<support@rt-net.jp\>

各ファイルはライセンスがファイル中に明記されている場合、そのライセンスに従います。特に明記されていない場合は、MIT Licenseに基づき公開されています。
ライセンスの全文は[LICENSE](./LICENSE)または[https://www.apache.org/licenses/LICENSE-2.0](https://www.apache.org/licenses/LICENSE-2.0)から確認できます。

## Contributing

- 本ソフトウェアはオープンソースですが、開発はオープンではありません。
- 本ソフトウェアは基本的にオープンソースソフトウェアとして「AS IS」（現状有姿のまま）で提供しています。
- 本ソフトウェアに関する無償サポートはありません。
- バグの修正や誤字脱字の修正に関するリクエストは常に受け付けていますが、
それ以外の機能追加等のリクエストについては社内のガイドラインを優先します。
詳しくは[コントリビューションガイドライン](https://github.com/rt-net/.github/blob/master/CONTRIBUTING.md)に従ってください。

### Acknowledgements

本リポジトリは、以下のリポジトリのファイルをベースに開発されています。

- [CIR-KIT/fourth_robot_pkg]( https://github.com/CIR-KIT/fourth_robot_pkg )
  - author
    - RyodoTanaka
  - maintainer
    - RyodoTanaka
  - BSD ([BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause))
  - 詳細は [package.xml](https://github.com/CIR-KIT/fourth_robot_pkg/blob/indigo-devel/fourth_robot_control/package.xml) を参照してください。
- [yujinrobot/kobuki]( https://github.com/yujinrobot/kobuki )
  - authors
    - Daniel Stonier
    - Younghun Ju
    - Jorge Santos Simon
    - Marcus Liebhardt
  - maintainer
    - Daniel Stonier
  - BSD ([BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause))
  - 詳細は [package.xml](https://github.com/yujinrobot/kobuki/blob/melodic/kobuki/package.xml) を参照してください。
