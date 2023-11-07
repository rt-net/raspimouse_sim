^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package raspimouse_fake
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forthcoming
-----------
* シミュレータ環境に擬似的なラズパイマウスノードを追加 (`#69 <https://github.com/rt-net/raspimouse_sim/issues/69>`_)
  Co-authored-by: Shota Aoki <s.aoki@rt-net.jp>
* ROS 2 Humble環境のraspimouse_with_emptyworld.launch.pyを実装 (`#66 <https://github.com/rt-net/raspimouse_sim/issues/66>`_)
* Contributors: YusukeKato

0.1.1 (2023-08-22)
------------------
* Fix CMakeLists.txt to support both python2 and 3 (`#62 <https://github.com/rt-net/raspimouse_sim/issues/62>`_)
* Use DiffDriveController defined in xacro to simplify raspimouse_gazebo (`#53 <https://github.com/rt-net/raspimouse_sim/issues/53>`_)
  * Fix diff_drive_controller settings
  details: `#21 <https://github.com/rt-net/raspimouse_sim/issues/21>`_
  * Remove image files from repository
  * Use DiffDriveController defined in xacro
  * Use xacro instead of xacro.py
  * Remove external package from meta package config
  * Fix namespace error
  * Set no lidar on samplemaze
  * Refactor device file simulation
  * Fix source package not found
  * Add teleop launch
  * Fix merge error
  ac1585f1878a98fd546b26e3f58f10a5739ea9ab
  * Fix typo
  * Remove not-used script
  * Update README
  * Support sum_all, sum_forward
  * Fix package.xml
  * Fix package.xml
* Contributors: Daisuke Sato, Shota Aoki
