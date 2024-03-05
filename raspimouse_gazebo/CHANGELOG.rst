^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package raspimouse_gazebo
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Forthcoming
-----------
* シミュレータ環境でSLAMとNavigationを実行 (`#77 <https://github.com/rt-net/raspimouse_sim/issues/77>`_)
  Co-authored-by: Shota Aoki <s.aoki@rt-net.jp>
* コントローラのパラメータを調整してオドメトリのズレを修正 (`#76 <https://github.com/rt-net/raspimouse_sim/issues/76>`_)
* camera_downwardがtrueのときRGBカメラが斜め下を向くように変更 (`#75 <https://github.com/rt-net/raspimouse_sim/issues/75>`_)
  Co-authored-by: Shota Aoki <s.aoki@rt-net.jp>
* ライントレース用のコースを作成 (`#74 <https://github.com/rt-net/raspimouse_sim/issues/74>`_)
  Co-authored-by: Shota Aoki <s.aoki@rt-net.jp>
* Contributors: YusukeKato

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
* Add LaserScan topic to RViz configuration file (`#59 <https://github.com/rt-net/raspimouse_sim/issues/59>`_)
* Add keyboard teleop lauch (`#56 <https://github.com/rt-net/raspimouse_sim/issues/56>`_)
* Update namespace to fix odom tf error (`#55 <https://github.com/rt-net/raspimouse_sim/issues/55>`_)
* Use DiffDriveController defined in xacro to simplify raspimouse_gazebo (`#53 <https://github.com/rt-net/raspimouse_sim/issues/53>`_)
* Disable shadows by default (`#51 <https://github.com/rt-net/raspimouse_sim/issues/51>`_)
* Refactor XML format files (`#43 <https://github.com/rt-net/raspimouse_sim/issues/43>`_)
* Add an office-like Gazebo world sample (`#46 <https://github.com/rt-net/raspimouse_sim/issues/46>`_)
  Co-authored-by: yukixx6 <s1526707DA@s.chibakoudai.jp>
* Replace deprecated xacro parser (`#45 <https://github.com/rt-net/raspimouse_sim/issues/45>`_)
* Add Gazebo model download script (`#47 <https://github.com/rt-net/raspimouse_sim/issues/47>`_)
* Migrate package.xml to Format 2 (`#41 <https://github.com/rt-net/raspimouse_sim/issues/41>`_)
* Add use_devfile argumet to launch files to make virtual device file optional (`#34 <https://github.com/rt-net/raspimouse_sim/issues/34>`_)
* fix raspimouse_with_empetyworld.launch to load robot descrption (`#35 <https://github.com/rt-net/raspimouse_sim/issues/35>`_)
* Add an index to each wall model name for fixing `#26 <https://github.com/rt-net/raspimouse_sim/issues/26>`_ (`#32 <https://github.com/rt-net/raspimouse_sim/issues/32>`_)
* Merge pull request `#15 <https://github.com/rt-net/raspimouse_sim/issues/15>`_ from Tiryoh/spike
* Merge pull request `#8 <https://github.com/rt-net/raspimouse_sim/issues/8>`_ from Tiryoh/spike
* Refactoring to reduce warning
* Update launch files
* Update file path of urdf model
* Initial commit
* Contributors: Daisuke Sato, Shota Aoki, Shuhei Kozasa, Tiryoh
