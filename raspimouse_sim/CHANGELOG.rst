^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package raspimouse_sim
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forthcoming
-----------
* ROS 2 Humble環境のraspimouse_with_emptyworld.launch.pyを実装 (`#66 <https://github.com/rt-net/raspimouse_sim/issues/66>`_)
* Contributors: YusukeKato

0.1.1 (2023-08-22)
------------------
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
* Migrate package.xml to Format 2 (`#41 <https://github.com/rt-net/raspimouse_sim/issues/41>`_)
  * Migrate package.xml to Format 2
  * Fix package.xml format error
  * Fix package.xml format
  metapackage can contain only buildtool_depend and exec_depend
  * Add deps used in launch files
  * Revert update for deprecated package
  * Add deps used in scripts
* Refactor package.xml
* Merge branch 'indigo-devel' into kinetic-devel
* Fix typo
* Merge branch 'indigo-devel' into kinetic-devel
* Update to be independent of raspimouse_ros `#7 <https://github.com/rt-net/raspimouse_sim/issues/7>`_
* Merge pull request `#15 <https://github.com/rt-net/raspimouse_sim/issues/15>`_ from Tiryoh/spike
  Refactor package
* Update dependencies in package.xml
  https://github.com/ryuichiueda/raspimouse_sim_installer/commit/efc6795c72e2a632fbad5fa26e31f2250904f35a#diff-95ed54bd44e1f2d0531683c0b1a94849R26
* Add ROS metapackage settings
* Contributors: Daisuke Sato, Tiryoh
