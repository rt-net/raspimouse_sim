# raspimouse_sim 

[![Build Status](https://travis-ci.org/rt-net/raspimouse_sim.svg?branch=indigo-devel)](https://travis-ci.org/rt-net/raspimouse_sim)

Gaezbo上でシミュレートできるRaspberry Pi MouseのROSパッケージ一式です。

詳細なセットアップ方法は[Wiki](https://github.com/rt-net/raspimouse_sim/wiki)にまとめています。

## 動作環境

以下の環境を前提として動作確認しています。

* Ubuntu
  * Ubuntu Bionic Beaver 18.04
* ROS
  * ROS Melodic Morenia
* Gazebo
  * Gazebo 9.x
* ROS Package
  * ros-melodic-desktop-full

## インストール方法

ターミナルを開き、以下のコマンドを実行してください。

```
bash -exv -c "$(curl -sSfL https://git.io/raspimouse-sim-installer)"
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

![](./docs/images/raspimouse_samplemaze.png)

### URG付きモデルでの動作例

![](./docs/images/raspimouse_urg.png)

## ライセンス

このリポジトリはMITライセンスに基づいて公開されています。
MITライセンスについては[LICENSE]( ./LICENSE )を確認してください。

### 引用または参考にしたリポジトリ

* [CIR-KIT/fourth_robot_pkg]( https://github.com/CIR-KIT/fourth_robot_pkg ) - BSD (BSD 3-Clause License)
  * urdf model xacro files
  * ros_control definition files
* [yujinrobot/kobuki]( https://github.com/yujinrobot/kobuki ) - BSD (BSD 3-Clause License)
  * launch files
