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
from raspimouse_description.robot_description_loader import RobotDescriptionLoader
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import SetParameter
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode


def generate_launch_description():
    declare_arg_lidar = DeclareLaunchArgument(
        'lidar',
        default_value='none',
        description='Set "none", "urg", "lds", or "rplidar".')
    declare_arg_lidar_frame = DeclareLaunchArgument(
        'lidar_frame',
        default_value='laser',
        description='Set lidar link name.')
    declare_arg_use_rgb_camera = DeclareLaunchArgument(
        'use_rgb_camera',
        default_value='false',
        description='Set "true" to mount rgb camera.')
    declare_arg_world_name = DeclareLaunchArgument(
        'world_name',
        default_value=get_package_share_directory('raspimouse_gazebo')+'/worlds/empty_world.sdf',
        description='Set world name.')

    env = {'IGN_GAZEBO_SYSTEM_PLUGIN_PATH': os.environ['LD_LIBRARY_PATH'],
           'IGN_GAZEBO_RESOURCE_PATH': os.path.dirname(
               get_package_share_directory('raspimouse_description')) + ':' +
           os.path.join(get_package_share_directory('raspimouse_gazebo'), 'models'),
           }
    gui_config = os.path.join(
        get_package_share_directory('raspimouse_gazebo'), 'gui', 'gui.config')
    ign_gazebo = ExecuteProcess(
            cmd=['ign gazebo -r', LaunchConfiguration('world_name'), '--gui-config', gui_config],
            output='screen',
            additional_env=env,
            shell=True
        )

    ignition_spawn_entity = Node(
        package='ros_gz_sim',
        executable='create',
        output='screen',
        arguments=['-topic', '/robot_description',
                   '-name', 'raspimouse',
                   '-allow_renaming', 'true'],
    )

    description_loader = RobotDescriptionLoader()
    description_loader.lidar = LaunchConfiguration('lidar')
    description_loader.lidar_frame = LaunchConfiguration('lidar_frame')
    description_loader.use_gazebo = 'true'
    description_loader.use_rgb_camera = LaunchConfiguration('use_rgb_camera')
    description_loader.gz_control_config_package = 'raspimouse_gazebo'
    description_loader.gz_control_config_file_path = 'config/raspimouse_controllers.yaml'

    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': description_loader.load()}]
    )

    spawn_joint_state_broadcaster = ExecuteProcess(
                cmd=['ros2 run controller_manager spawner joint_state_broadcaster'],
                shell=True,
                output='screen',
            )

    spawn_diff_drive_controller = ExecuteProcess(
                cmd=['ros2 run controller_manager spawner diff_drive_controller'],
                shell=True,
                output='screen',
            )

    rviz_config_file = get_package_share_directory(
        'raspimouse_gazebo') + '/config/config.rviz'
    rviz = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen",
        arguments=["-d", rviz_config_file],
    )

    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=['/clock@rosgraph_msgs/msg/Clock[ignition.msgs.Clock',
                   '/camera/color/image_raw@sensor_msgs/msg/Image@gz.msgs.Image',
                   '/camera_info@sensor_msgs/msg/CameraInfo@gz.msgs.CameraInfo'],
        output='screen'
    )

    container = ComposableNodeContainer(
            name='fake_raspimouse_container',
            namespace='',
            package='rclcpp_components',
            executable='component_container_mt',
            composable_node_descriptions=[
                ComposableNode(
                    package='raspimouse_fake',
                    plugin='fake_raspimouse::Raspimouse',
                    name='raspimouse'),
            ],
            output='screen',
    )

    return LaunchDescription([
        SetParameter(name='use_sim_time', value=True),
        declare_arg_lidar,
        declare_arg_lidar_frame,
        declare_arg_use_rgb_camera,
        declare_arg_world_name,
        ign_gazebo,
        ignition_spawn_entity,
        robot_state_publisher,
        spawn_joint_state_broadcaster,
        spawn_diff_drive_controller,
        rviz,
        bridge,
        container
    ])
