[English](README.en.md) | [日本語](README.md)

# raspimouse_sim

[![industrial_ci](https://github.com/rt-net/raspimouse_sim/actions/workflows/industrial_ci.yml/badge.svg?branch=ros2)](https://github.com/rt-net/raspimouse_sim/actions/workflows/industrial_ci.yml)

Gazebo上でRaspberry Pi Mouseの動作をシミュレーションするためのROS 2パッケージです。

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

次のコマンドを実行するとGazeboシミュレータが起動し、Raspberry Pi Mouseのモデルが表示されます。

```sh
ros2 launch raspimouse_gazebo raspimouse_with_emptyworld.launch.py
```

## Packages

- raspimouse_sim
  - 本リポジトリに含まれる複数のパッケージに関するメタ情報を管理します。
- raspimouse_fake
  - Raspberry Pi Mouseのモータ制御インターフェースを模擬するパッケージです。
- raspimouse_gazebo
  - [Gazebo](https://gazebosim.org)上でシミュレーション環境を構築するためのモデルやスクリプトを提供するパッケージです。

## How to Use Examples

サンプルプログラムの詳細な動作方法は、`raspimouse_gazebo`パッケージの[README](./raspimouse_gazebo/README.md)で説明しています。

- raspimouse_gazebo
  - [Joystick Control](./raspimouse_gazebo/README.md#joystick-control)
  - [Object Tracking](./raspimouse_gazebo/README.md#object-tracking)
  - [Camera Line Follower](./raspimouse_gazebo/README.md#camera_line_follower)
  - [SLAM & Navigation](./raspimouse_gazebo/README.md#slam--navigation)

## License

(C) 2016 RT Corporation \<support@rt-net.jp\>

各ファイルはライセンスがファイル中に明記されている場合、そのライセンスに従います。特に明記されていない場合は、MIT Licenseに基づき公開されています。
ライセンスの全文は[LICENSE](./LICENSE)または[https://www.apache.org/licenses/LICENSE-2.0](https://www.apache.org/licenses/LICENSE-2.0)から確認できます。

## Contributing

- 本ソフトウェアはオープンソースですが、開発はオープンではありません。
- 本ソフトウェアは基本的にオープンソースソフトウェアとして「AS IS」（現状有姿のまま）で提供しています。
- 本ソフトウェアに関する無償サポートは行っていません。
- バグの修正や誤字脱字の修正に関するリクエストは常に受け付けていますが、
それ以外の機能追加等のリクエストについては社内のガイドラインを優先します。
詳しくは[コントリビューションガイドライン](https://github.com/rt-net/.github/blob/master/CONTRIBUTING.md)に従ってください。

### Acknowledgements

本リポジトリは、以下のリポジトリのファイルをベースに開発されています。

- [CIR-KIT/fourth_robot_pkg](https://github.com/CIR-KIT/fourth_robot_pkg)
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
