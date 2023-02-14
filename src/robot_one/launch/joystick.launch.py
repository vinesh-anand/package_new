from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument

import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    use_sim_time = LaunchConfiguration('use_sim_time')

    keyboard_params = os.path.join(get_package_share_directory('robot_one'),'config','joystick.yaml')

    keyboard_node = Node(
            package='keyboard',
            executable='keyboard_node',
            parameters=[keyboard_params, {'use_sim_time': use_sim_time}],
         )

    teleop_node = Node(
            package='teleop_twist_keyboard',
            executable='teleop_node',
            name='teleop_node',
            parameters=[keyboard_params, {'use_sim_time': use_sim_time}],
            remappings=[('/cmd_vel','/diff_cont/cmd_vel_keyboard')]
         )

    #twist_stamper = Node(
    #        package='twist_stamper',
    #        executable='twist_stamper',
    #        parameters=[{'use_sim_time': use_sim_time}],
    #        remappings=[('/cmd_vel_in','/diff_cont/cmd_vel_unstamped'),
    #                    ('/cmd_vel_out','/diff_cont/cmd_vel')]
    #     )


    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use sim time if true'),
        keyboard_node,
        teleop_node,
        # twist_stamper       
    ])
