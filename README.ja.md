# raspimouse_sim 

Gaezbo上でシミュレートできるRaspberry Pi MouseのROSパッケージ一式です。

詳細なセットアップ方法は[Wiki](https://github.com/rt-net/raspimouse_sim/wiki)にまとめています。

![](https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_samplemaze_animation.gif)

## ROS Package Status

|Kinetic + Ubuntu Xenial|Melodic + Ubuntu Bionic|master|
|:---:|:---:|:---:|
|[![Build Status](https://travis-ci.org/rt-net/raspimouse_sim.svg?branch=kinetic-devel)](https://travis-ci.org/rt-net/raspimouse_sim)|[![Build Status](https://travis-ci.org/rt-net/raspimouse_sim.svg?branch=melodic-devel)](https://travis-ci.org/rt-net/raspimouse_sim)|[![Build Status](https://travis-ci.org/rt-net/raspimouse_sim.svg?branch=master)](https://travis-ci.org/rt-net/raspimouse_sim)|


## 動作環境

以下の環境を前提として動作確認しています。


* Ubuntu
  * Ubuntu Xenial Xerus 16.04.*
* ROS
  * ROS Kinetic Kame
* Gazebo
  * Gazebo 7.x
* ROS Package
  * ros-kinetic-desktop-full

または

* Ubuntu
  * Ubuntu Bionic Beaver 18.04.*
* ROS
  * ROS Melodic Morenia
* Gazebo
  * Gazebo 9.x
* ROS Package
  * ros-melodic-desktop-full

## インストール方法

このROSパッケージをダウンロードします。

```
cd ~/catkin_ws/src
git clone https://github.com/rt-net/raspimouse_sim.git
```

依存しているROSパッケージをインストールします。

```
cd ~/catkin_ws/src
git clone https://github.com/rt-net/raspimouse_description.git
rosdep install -r -y -i --from-paths raspimouse*
```

`catkin_make`を使用してパッケージをビルドします。

```
cd ~/catkin_ws && catkin_make
source ~/catkin_ws/devel/setup.bash
```

Gazeboで使用するモデルデータをダウンロードします。

```
rosrun raspimouse_gazebo download_gazebo_models.sh
```

## QuickStart

シミュレータのインストール後、次のコマンドを入力して起動してください。

```
rosrun raspimouse_control gen_dev_file.sh
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

## ライセンス

このリポジトリはMITライセンスに基づいて公開されています。  
MITライセンスについては[LICENSE]( ./LICENSE )を確認してください。

### 引用または参考にしたリポジトリ

* [CIR-KIT/fourth_robot_pkg]( https://github.com/CIR-KIT/fourth_robot_pkg ) - BSD (BSD 3-Clause License)
  * urdf model xacro files
  * ros_control definition files
* [yujinrobot/kobuki]( https://github.com/yujinrobot/kobuki ) - BSD (BSD 3-Clause License)
  * launch files
