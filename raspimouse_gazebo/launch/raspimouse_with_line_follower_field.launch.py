# The MIT License (MIT)
#
# Copyright 2023 RT Corporation <support@rt-net.jp>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the "Software"), to deal in
# the Software without restriction, including without limitation the rights to
# use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
# the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
# FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
# IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import SetParameter
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    world_file = os.path.join(
        get_package_share_directory('raspimouse_gazebo'),
        'worlds',
        'line_follower_world.sdf')
    world_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            get_package_share_directory('raspimouse_gazebo'),
            '/launch/raspimouse_with_emptyworld.launch.py']),
        launch_arguments={
            'world_name': world_file,
            'spawn_x': '0.0',
            'spawn_y': '0.0',
            'spawn_z': '0.02'
            }.items()
    )

    return LaunchDescription([
        SetParameter(name='use_sim_time', value=True),
        world_launch
    ])
