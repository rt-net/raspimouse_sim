[English](README.en.md) | [日本語](README.md)

# raspimouse_sim 

Gazebo上でシミュレートできるRaspberry Pi MouseのROS 2パッケージです。

## ROS 2 Package Status

| main develop<br>(ros2)|Humble + Ubuntu Jammy<br>(humble-devel)|
|:---:|:---:|
|[![industrial_ci](https://github.com/rt-net/raspimouse_sim/workflows/industrial_ci/badge.svg?branch=ros2)](https://github.com/rt-net/raspimouse_sim/actions?query=branch%3Aros2+workflow%3Aindustrial_ci)|[![industrial_ci](https://github.com/rt-net/raspimouse_sim/workflows/industrial_ci/badge.svg?branch=humble-devel)](https://github.com/rt-net/raspimouse_sim/actions?query=branch%3Ahumble-devel+workflow%3Aindustrial_ci)|

## 動作環境

以下の環境を前提として動作確認しています。

* Ubuntu
  * Ubuntu Jammy Jellyfish 22.04.*
* ROS 2
  * ROS Humble Hawksbill
* Gazebo
  * Ignition Gazebo 6.x
* ROS 2 Package
  * ros-humble-desktop-full

## インストール方法

このROS 2パッケージをダウンロードします。

```sh
cd ~/ros2_ws/src
git clone -b ros2 https://github.com/rt-net/raspimouse_sim.git
```

依存しているROS 2パッケージをインストールします。

```sh
cd ~/ros2_ws/src
git clone https://github.com/rt-net/raspimouse_ros2_examples.git
git clone -b ros2 https://github.com/rt-net/raspimouse_description.git
rosdep install -r -y -i --from-paths raspimouse*
```

`colcon`を使用してパッケージをビルドします。

```sh
cd ~/ros2_ws
colcon build --symlink-install
source ~/ros2_ws/install/setup.bash
```

## QuickStart

シミュレータのインストール後、次のコマンドを入力して起動してください。

```sh
ros2 launch raspimouse_gazebo raspimouse_with_emptyworld.launch.py
```

## サンプル動作例

### ジョイスティックコントローラによる操縦サンプル

端末1で次のコマンドを実行すると、Gazeboシミュレータが起動します。

```sh
ros2 launch raspimouse_gazebo raspimouse_with_emptyworld.launch.py
```

端末2で次のコマンドを実行すると、Raspberry Pi Mouseをジョイスティックコントローラで操作できます。

```sh
ros2 launch raspimouse_ros2_examples teleop_joy.launch.py joydev:="/dev/input/js0" joyconfig:=f710 mouse:=false
```

### RGBカメラを用いた色検出による物体追従サンプル

端末1で次のコマンドを実行すると、色付きの立方体が配置されたワールドが表示されます。

```sh
ros2 launch raspimouse_gazebo raspimouse_with_color_objects.launch.py use_rgb_camera:=true
```

端末2で次のコマンドを実行すると、Raspberry Pi Mouseがオレンジ色（赤色）の物体を追従します。

```sh
ros2 launch raspimouse_ros2_examples object_tracking.launch.py mouse:=false use_camera_node:=false
```

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
