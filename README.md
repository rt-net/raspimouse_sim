[English](README.en.md) | [日本語](README.md)

# raspimouse_sim 

Gazebo上でシミュレートできるRaspberry Pi MouseのROSパッケージ一式です。

詳細なセットアップ方法は[Wiki](https://github.com/rt-net/raspimouse_sim/wiki)にまとめています。

![](https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_samplemaze_animation.gif)

## ROS Package Status

| main develop<br>(master)|Noetic + Ubuntu Focal<br>(noetic-devel)|
|:---:|:---:|
|[![industrial_ci](https://github.com/rt-net/raspimouse_sim/workflows/industrial_ci/badge.svg?branch=master)](https://github.com/rt-net/raspimouse_sim/actions?query=branch%3Amaster+workflow%3Aindustrial_ci)|[![industrial_ci](https://github.com/rt-net/raspimouse_sim/workflows/industrial_ci/badge.svg?branch=noetic-devel)](https://github.com/rt-net/raspimouse_sim/actions?query=branch%3Anoetic-devel+workflow%3Aindustrial_ci)|

以下のブランチのメンテナンスは終了しています。

* rpim_book_version
* indigo-devel
* kinetic-devel
* melodic-devel

## 動作環境

以下の環境を前提として動作確認しています。

* Ubuntu
  * Ubuntu Focal Fossa 20.04.*
* ROS
  * ROS Noetic Ninjemys
* Gazebo
  * Gazebo 11.x
* ROS Package
  * ros-noetic-desktop-full

## インストール方法

このROSパッケージをダウンロードします。

```
cd ~/catkin_ws/src
git clone https://github.com/rt-net/raspimouse_sim.git
```

依存しているROSパッケージをインストールします。

```
cd ~/catkin_ws/src
git clone https://github.com/ryuichiueda/raspimouse_ros_2.git
git clone https://github.com/rt-net/raspimouse_description.git
rosdep install -r -y -i --from-paths raspimouse*
```

`catkin_make`を使用してパッケージをビルドします。

```
cd ~/catkin_ws && catkin_make
source ~/catkin_ws/devel/setup.bash
```

Gazeboで使用するハードウェアモデルデータをダウンロードします。

```
rosrun raspimouse_gazebo download_gazebo_models.sh
```

## QuickStart

シミュレータのインストール後、次のコマンドを入力して起動してください。

```
roslaunch raspimouse_gazebo raspimouse_with_samplemaze.launch
```

詳細は[このページ](https://github.com/rt-net/raspimouse_sim/wiki/quickstart)をお読みください。

## スクリーンショット

### サンプル迷路での動作例

```
roslaunch raspimouse_gazebo raspimouse_with_samplemaze.launch
```

![](https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_samplemaze.png)

### URG付きモデルでの動作例

```
roslaunch raspimouse_gazebo raspimouse_with_gasstand.launch
```

![](https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_urg.png)

### URG付きモデルでSLAM動作例

```
# 1つ目の端末で
roslaunch raspimouse_gazebo raspimouse_with_willowgarage.launch
# 2つ目の端末で
roslaunch raspimouse_ros_examples slam_gmapping.launch
# 3つ目の端末で
roslaunch raspimouse_ros_examples teleop.launch key:=true mouse:=false
```

![](https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_urg_slam_gmapping.png)

※raspimouse_ros_examplesを使う際には[rt-net/raspimouse_ros_examples](https://github.com/rt-net/raspimouse_ros_examples)のインストールが必要です。

以下のコマンドでインストールができます。

```
cd ~/catkin_ws/src
git clone https://github.com/rt-net/raspimouse_ros_examples.git
rosdep install -r -y -i --from-paths raspimouse*
cd ~/catkin_ws && catkin_make
source ~/catkin_ws/devel/setup.bash
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
