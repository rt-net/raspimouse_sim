^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package raspimouse_gazebo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2.0.0 (2023-11-07)
------------------
* Gazebo上で画像トピックを配信できるようにbridgeを設定 (`#71 <https://github.com/rt-net/raspimouse_sim/issues/71>`_)
* カメラサンプル用のcolor_objects_worldを作成 (`#70 <https://github.com/rt-net/raspimouse_sim/issues/70>`_)
* シミュレータ環境に擬似的なラズパイマウスノードを追加 (`#69 <https://github.com/rt-net/raspimouse_sim/issues/69>`_)
  Co-authored-by: Shota Aoki <s.aoki@rt-net.jp>
* controller managerノードにプラグインを追加するように変更 (`#68 <https://github.com/rt-net/raspimouse_sim/issues/68>`_)
* robot_description_lodarを使用するように変更 (`#67 <https://github.com/rt-net/raspimouse_sim/issues/67>`_)
* ROS 2 Humble環境のraspimouse_with_emptyworld.launch.pyを実装 (`#66 <https://github.com/rt-net/raspimouse_sim/issues/66>`_)
* Contributors: YusukeKato

0.1.1 (2023-08-22)
------------------
* Fix CMakeLists.txt to support both python2 and 3 (`#62 <https://github.com/rt-net/raspimouse_sim/issues/62>`_)
* Add urg on/off option and lidar frame rename option (`#57 <https://github.com/rt-net/raspimouse_sim/issues/57>`_)
  * Add xacro option arg to every launch to support lidar option
  * Fix default value
  * Support lidar_frame rename option
  * Remove unused arg
  * Add arg for backward compatibility
* Add LaserScan topic to RViz configuration file (`#59 <https://github.com/rt-net/raspimouse_sim/issues/59>`_)
* Add keyboard teleop lauch (`#56 <https://github.com/rt-net/raspimouse_sim/issues/56>`_)
* Update namespace to fix odom tf error (`#55 <https://github.com/rt-net/raspimouse_sim/issues/55>`_)
  * Update namespace to fix odom tf error
  * Remove duplicates
  * Define robot_namespace for xacro manually
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
* Disable shadows by default (`#51 <https://github.com/rt-net/raspimouse_sim/issues/51>`_)
* Refactor XML format files (`#43 <https://github.com/rt-net/raspimouse_sim/issues/43>`_)
* Add an office-like Gazebo world sample (`#46 <https://github.com/rt-net/raspimouse_sim/issues/46>`_)
  * Add raspimouse with willowgarage launch
  * Use local .world file to enable using modified settings
  This .world file is optional.
  Gazebo can load .wolrd file from /usr/share/gazebo-*/world/.
  * Fix model path
  * Add use_devfile option, added by PR `#34 <https://github.com/rt-net/raspimouse_sim/issues/34>`_
  * Update initial camera position
  Co-authored-by: yukixx6 <s1526707DA@s.chibakoudai.jp>
* Replace deprecated xacro parser (`#45 <https://github.com/rt-net/raspimouse_sim/issues/45>`_)
  related issue: https://github.com/rt-net/raspimouse_sim/issues/18
* Add Gazebo model download script (`#47 <https://github.com/rt-net/raspimouse_sim/issues/47>`_)
  * Add Gazebo model download script
  * Add download_gazebo_models.sh to installation step
  * Refactor
* Migrate package.xml to Format 2 (`#41 <https://github.com/rt-net/raspimouse_sim/issues/41>`_)
  * Migrate package.xml to Format 2
  * Fix package.xml format error
  * Fix package.xml format
  metapackage can contain only buildtool_depend and exec_depend
  * Add deps used in launch files
  * Revert update for deprecated package
  * Add deps used in scripts
* Add use_devfile argumet to launch files to make virtual device file optional (`#34 <https://github.com/rt-net/raspimouse_sim/issues/34>`_)
  * Add use_devfile argument to launch simulator without virtual files
  * Add use_devfile argument to gasstand.launch
  * Add use_devfile argument and fix some description to launch nodes
* fix raspimouse_with_empetyworld.launch to load robot descrption (`#35 <https://github.com/rt-net/raspimouse_sim/issues/35>`_)
* Add an index to each wall model name for fixing `#26 <https://github.com/rt-net/raspimouse_sim/issues/26>`_ (`#32 <https://github.com/rt-net/raspimouse_sim/issues/32>`_)
* Refactor package.xml
* Merge branch 'indigo-devel' into kinetic-devel
* Fix typo
* Merge pull request `#15 <https://github.com/rt-net/raspimouse_sim/issues/15>`_ from Tiryoh/spike
  Refactor package
* Update dependencies in package.xml
  https://github.com/ryuichiueda/raspimouse_sim_installer/commit/efc6795c72e2a632fbad5fa26e31f2250904f35a#diff-95ed54bd44e1f2d0531683c0b1a94849R26
* Merge pull request `#8 <https://github.com/rt-net/raspimouse_sim/issues/8>`_ from Tiryoh/spike
  support device file of lightsensors `#3 <https://github.com/rt-net/raspimouse_sim/issues/3>`_, `#6 <https://github.com/rt-net/raspimouse_sim/issues/6>`_
* Update robot namespace
  All nodes depends on gazebo are now in /raspimouse_on_gazebo
* Refactoring to reduce warning
* Update launch files
* Update file path of urdf model
* Initial commit
* Contributors: Daisuke Sato, Shota Aoki, Shuhei Kozasa, Tiryoh
