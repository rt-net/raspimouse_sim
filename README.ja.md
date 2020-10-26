# raspimouse_sim 

Gaezbo上でシミュレートできるRaspberry Pi MouseのROSパッケージ一式です。

詳細なセットアップ方法は[Wiki](https://github.com/rt-net/raspimouse_sim/wiki)にまとめています。

![](https://rt-net.github.io/images/raspberry-pi-mouse/raspimouse_sim_samplemaze_animation.gif)

## ROS Package Status

| main develop<br>(master)|Kinetic + Ubuntu Xenial<br>(kinetic-devel)|Melodic + Ubuntu Bionic<br>(melodic-devel)|
|:---:|:---:|:---:|
|[![industrial_ci](https://github.com/rt-net/raspimouse_sim/workflows/industrial_ci/badge.svg?branch=master)](https://github.com/rt-net/raspimouse_sim/actions?query=branch%3Amaster+workflow%3Aindustrial_ci)|[![industrial_ci](https://github.com/rt-net/raspimouse_sim/workflows/industrial_ci/badge.svg?branch=kinetic-devel)](https://github.com/rt-net/raspimouse_sim/actions?query=branch%3Akinetic-devel+workflow%3Aindustrial_ci)|[![industrial_ci](https://github.com/rt-net/raspimouse_sim/workflows/industrial_ci/badge.svg?branch=melodic-devel)](https://github.com/rt-net/raspimouse_sim/actions?query=branch%3Amelodic-devel+workflow%3Aindustrial_ci)|

以下のブランチのメンテナンスは終了しています。

* rpim_book_version
* indigo-devel


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
git clone https://github.com/ryuichiueda/raspimouse_ros_2.git
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

### 謝辞

以下のリポジトリのファイルをベースに開発されています。

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
* []