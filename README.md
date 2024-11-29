[English](README.en.md) | [日本語](README.md)

# raspimouse_sim

[![industrial_ci](https://github.com/rt-net/raspimouse_sim/actions/workflows/industrial_ci.yml/badge.svg?branch=ros2)](https://github.com/rt-net/raspimouse_sim/actions/workflows/industrial_ci.yml)

Gazebo上でシミュレートできるRaspberry Pi MouseのROS 2パッケージです。

![](https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_color_objects_world.png)

**本ブランチはROS 2 Jazzy向けです。他のディストリビューションについては、以下にリストされた対応するブランチを参照してください。**

- ROS 2 Humble ([humble](https://github.com/rt-net/raspimouse_sim/tree/humble))

## 動作環境

以下の環境を前提として動作確認しています。

* Ubuntu
  * Ubuntu 24.04 Noble Numbat
* ROS 2
  * ROS 2 Jazzy Jalisco
* Gazebo
  * Gazebo Sim 8.x
* ROS 2 Package
  * ros-jazzy-desktop-full

## インストール方法

このROS 2パッケージをダウンロードします。

```sh
cd ~/ros2_ws/src
git clone -b $ROS_DISTRO https://github.com/rt-net/raspimouse_sim.git
```

依存しているROS 2パッケージをインストールします。

```sh
cd ~/ros2_ws/src
git clone -b $ROS_DISTRO https://github.com/rt-net/raspimouse_ros2_examples.git
git clone -b $ROS_DISTRO https://github.com/rt-net/raspimouse_slam_navigation_ros2.git
git clone -b $ROS_DISTRO https://github.com/rt-net/raspimouse_description.git
rosdep install -r -y -i --from-paths raspimouse*
```

`colcon`を使用してパッケージをビルドします。

```sh
cd ~/ros2_ws
colcon build --symlink-install
source ~/ros2_ws/install/setup.bash
```

## QuickStart

パッケージビルド後、次のコマンドを実行するとGazeboシミュレータが起動します。

```sh
ros2 launch raspimouse_gazebo raspimouse_with_emptyworld.launch.py
```

## サンプル動作例

各サンプルの動作には、[raspimouse_ros2_examples](https://github.com/rt-net/raspimouse_ros2_examples)が必要です。

### ジョイスティックコントローラによる操縦サンプル

端末1で次のコマンドを実行すると、Gazeboシミュレータが起動します。

```sh
ros2 launch raspimouse_gazebo raspimouse_with_emptyworld.launch.py
```

端末2で次のコマンドを実行すると、Raspberry Pi Mouseをジョイスティックコントローラで操作できます。

```sh
ros2 launch raspimouse_ros2_examples teleop_joy.launch.py joydev:="/dev/input/js0" joyconfig:=f710 mouse:=false
```

![](https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_joystick.gif)

### RGBカメラを用いた色検出による物体追従サンプル

端末1で次のコマンドを実行すると、色付きの立方体が配置されたワールドが表示されます。

```sh
ros2 launch raspimouse_gazebo raspimouse_with_color_objects.launch.py use_rgb_camera:=true
```

端末2で次のコマンドを実行すると、Raspberry Pi Mouseがオレンジ色（赤色）の物体を追従します。

```sh
ros2 launch raspimouse_ros2_examples object_tracking.launch.py mouse:=false use_camera_node:=false
```

![](https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_object_tracking.gif)

### RGBカメラを用いたライントレースサンプル

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

カメラライントレースにおけるパラメータは[こちら](https://github.com/rt-net/raspimouse_ros2_examples?tab=readme-ov-file#parameters)を参照してください。

![](https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_camerafollower_short.gif)

### LiDARを用いたSLAMとNavigationのサンプル

本サンプルの動作には、[raspimouse_slam_navigation_ros2](https://github.com/rt-net/raspimouse_slam_navigation_ros2) が必要です。

#### SLAM

端末1で次のコマンドを実行すると、`Lake House`のモデルが配置されたワールドが表示されます。
```sh
ros2 launch raspimouse_gazebo raspimouse_with_lakehouse.launch.py lidar:=urg
```
`lidar`は`urg`、`lds`、`rplidar`のいずれかを指定してください。

端末2で次のコマンドを実行すると、Raspberry Pi Mouseをジョイスティックコントローラで操作できます。
```sh
ros2 launch raspimouse_ros2_examples teleop_joy.launch.py joydev:="/dev/input/js0" joyconfig:=f710 mouse:=false
```

端末3で次のコマンドを実行すると、SLAMが実行されます。
```sh
ros2 launch raspimouse_slam pc_slam.launch.py
```

![](https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_slam.png)

端末4で次のコマンドを実行すると、作成した地図を保存できます。
```sh
ros2 run nav2_map_server map_saver_cli -f ~/MAP_NAME
```
`MAP_NAME`は任意の名前を指定できます。

![](https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_slam_short.gif)

#### Navigation

端末1で次のコマンドを実行すると、`Lake House`のモデルが配置されたワールドが表示されます。
```sh
ros2 launch raspimouse_gazebo raspimouse_with_lakehouse.launch.py lidar:=urg
```
`lidar`は`urg`、`lds`、`rplidar`のいずれかを指定してください。

端末2で次のコマンドを実行すると、Navigationが実行されます。
```sh
ros2 launch raspimouse_navigation pc_navigation.launch.py use_sim_time:=true map:=$HOME/MAP_NAME.yaml
```
引数`map`にはSLAMで作成した地図ファイルのパスを指定してください。

![](https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_navigation_short.gif)

## モデルデータ一覧

### course_curve_50x50cm

ライントレース用の曲線コースパネルです。
パネルサイズは50cm x 50cm、線の幅は4cmです。

![](./raspimouse_gazebo/models/course_curve_50x50cm/meshes/course_curve.jpg)

### course_straight_50x50cm

ライントレース用の直線コースパネルです。
パネルサイズは50cm x 50cm、線の幅は4cmです。

![](./raspimouse_gazebo/models/course_straight_50x50cm/meshes/course_straight.jpg)

### cube_*cm_color-name
それぞれ一辺5cm、7.5cm、10cm、15cm、30cmの立方体です。
色は赤、黄、青、緑、黒です。

![](https://rt-net.github.io/images/raspberry-pi-mouse/color_objects.png)

### daeファイルについて
daeファイルはBlender 4.0で編集しています。

## ライセンス

このリポジトリはMITライセンスに基づいて公開されています。
MITライセンスについては[LICENSE]( ./LICENSE )を確認してください。

※このソフトウェアは基本的にオープンソースソフトウェアとして「AS IS」（現状有姿のまま）で提供しています。本ソフトウェアに関する無償サポートはありません。
バグの修正や誤字脱字の修正に関するリクエストは常に受け付けていますが、それ以外の機能追加等のリクエストについては社内のガイドラインを優先します。

### 謝辞

以下のリポジトリのファイルをベースに開発されています。

* [CIR-KIT/fourth_robot_pkg]( https://github.com/CIR-KIT/fourth_robot_pkg )
  * author
    * RyodoTanaka
  * maintainer
    * RyodoTanaka
  * BSD ([BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause))
  * 詳細は [package.xml](https://github.com/CIR-KIT/fourth_robot_pkg/blob/indigo-devel/fourth_robot_control/package.xml) を参照してください。
* [yujinrobot/kobuki]( https://github.com/yujinrobot/kobuki )
  * authors
    * Daniel Stonier
    * Younghun Ju
    * Jorge Santos Simon
    * Marcus Liebhardt
  * maintainer
    * Daniel Stonier
  * BSD ([BSD 3-Clause License](https://opensource.org/licenses/BSD-3-Clause))
  * 詳細は [package.xml](https://github.com/yujinrobot/kobuki/blob/melodic/kobuki/package.xml) を参照してください。
