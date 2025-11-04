from launch import LaunchContext
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.substitutions import PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

#结构发布节点
def robot_pub_node():
    #urdf文件路径
    urdf_path=PathJoinSubstitution([
        FindPackageShare('pkg_simu'),
        'urdf',
        'pkg.urdf',
    ])
    #urdf文件内容
    urdf_file=""
    with open(urdf_path.perform(LaunchContext()),"r",encoding="utf-8") as f:
        urdf_file=f.read()
    #拉起服务
    node=Node(
        #包名
        package="robot_state_publisher",
        #任务名
        executable="robot_state_publisher",
        #参数
        parameters=[{'robot_description':urdf_file}],
    )
    return node

# #关节发布节点
# def joint_pub_node():
#     #拉起服务
#     node=Node(
#         #包名
#         package="joint_state_publisher",
#         #任务名
#         executable="joint_state_publisher",
#     )
#     return node

#gazebo初始化节点
def gazebo_init_node():
    #world文件路径
    world_path=PathJoinSubstitution([
        FindPackageShare('pkg_simu'),
        'gazebo',
        'pkg.world',
    ])
    #拉起服务
    node=IncludeLaunchDescription(
        PathJoinSubstitution([
            FindPackageShare('ros_gz_sim'),
            'launch',
            'gz_sim.launch.py',
        ]),
        launch_arguments={
            'gz_args': ['-r ',world_path.perform(LaunchContext())],
            # 'gz_args': ['-r --render-engine ogre ',world_path.perform(LaunchContext())],
            'on_exit_shutdown': 'true',
        }.items()
    )
    return node

#gazebo加载模型节点
def gazebo_load_model_node():
    #urdf文件路径
    urdf_path=PathJoinSubstitution([
        FindPackageShare('pkg_simu'),
        'urdf',
        'pkg.urdf',
    ])
    #拉起服务
    node=Node(
        #包名
        package="ros_gz_sim",
        #任务名
        executable="create",
        #参数
        arguments=[
            '-name','robot_name',
            '-file',urdf_path.perform(LaunchContext()),
            '-x','0.0',
            '-y','0.0',
            '-z','0.01',
        ],
        output='screen',
    )
    return node

#gazebo桥接节点
def gazebo_bridge_node():
    #bridge文件路径
    bridgr_path=PathJoinSubstitution([
        FindPackageShare('pkg_simu'),
        'gazebo',
        'bridge.yaml',
    ])
    #拉起服务
    node=Node(
        #包名
        package="ros_gz_bridge",
        #任务名
        executable="parameter_bridge",
        #参数
        arguments=[
            '--ros-args',
            '-p',
            f'config_file:={bridgr_path.perform(LaunchContext())}',
        ],
        output='screen',
    )
    return node

#gazebo桥接图像节点
def gazebo_bridge_image_node():
    #拉起服务
    node=Node(
        #包名
        package="ros_gz_image",
        #任务名
        executable="image_bridge",
        #参数
        arguments=[
            '/camera/image_raw',
        ],
        output='screen',
    )
    return node

#导航初始化节点
def nav2_init_node():
    #map文件路径
    map_path=PathJoinSubstitution([
        FindPackageShare('pkg_simu'),
        'map',
        'pkg.yaml',
    ])
    #nav2文件路径
    nav2_path=PathJoinSubstitution([
        FindPackageShare('pkg_simu'),
        'nav2',
        'nav2_params.yaml',
    ])
    #拉起服务
    node=IncludeLaunchDescription(
        PathJoinSubstitution([
            FindPackageShare('nav2_bringup'),
            'launch',
            'bringup_launch.py',
        ]),
        launch_arguments={
            'map':map_path.perform(LaunchContext()),
            'params_file':nav2_path.perform(LaunchContext()),
            'use_sim_time':"True",
        }.items(),
    )
    return node

#导航加载节点
def nav2_load_node():
    #拉起服务
    node=Node(
        #包名
        package="pkg_simu",
        #任务名
        executable="pkg_init",
    )
    return node

#rviz2加载节点
def rviz2_load_node():
    #rviz2文件路径
    rviz2_path=PathJoinSubstitution([
        FindPackageShare('pkg_simu'),
        'nav2',
        'nav2_default_view.rviz',
    ])
    # rviz2_path=PathJoinSubstitution([
    #     FindPackageShare('pkg_simu'),
    #     'rviz2',
    #     'pkg.rviz',
    # ])
    #拉起服务
    node=Node(
        #包名
        package="rviz2",
        #任务名
        executable="rviz2",
        #参数
        arguments=['-d',rviz2_path.perform(LaunchContext())],
    )
    return node

#自启动
def generate_launch_description():
    #拉起所有服务
    return LaunchDescription([
        #服务
        robot_pub_node(),
        # joint_pub_node(),
        gazebo_init_node(),
        gazebo_load_model_node(),
        gazebo_bridge_node(),
        gazebo_bridge_image_node(),
        nav2_init_node(),
        nav2_load_node(),
        rviz2_load_node(),
    ])
