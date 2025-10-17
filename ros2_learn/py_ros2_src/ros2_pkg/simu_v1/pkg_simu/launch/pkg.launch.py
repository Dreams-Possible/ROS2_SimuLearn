import launch
import launch_ros
import os
from ament_index_python.packages import get_package_share_directory



#tf_st节点
def robot_state_publisher_node():
    #urdf文件路径
    urdf_path=os.path.join(
        get_package_share_directory('pkg_simu'),
        'urdf',
        'pkg.urdf'
    )
    #urdf文件内容
    urdf_file=""
    with open(urdf_path,"r",encoding="utf-8") as f:
        urdf_file=f.read()
    #拉起服务
    node=launch_ros.actions.Node(
        #包名
        package="robot_state_publisher",
        #任务名
        executable="robot_state_publisher",
        #参数
        parameters=[{'robot_description':urdf_file}]
    )
    return node

#tf_dy节点
def joint_state_publisher_node():
    #拉起服务
    node=launch_ros.actions.Node(
        #包名
        package="joint_state_publisher",
        #任务名
        executable="joint_state_publisher"
    )
    return node

#gazebo启动节点
def gazebo_ros_node():
    #world文件路径
    world_path=os.path.join(
        get_package_share_directory('pkg_simu'),
        'gazebo',
        'pkg.world'
    )
    #拉起服务
    node=launch.actions.IncludeLaunchDescription(
        launch.launch_description_sources.PythonLaunchDescriptionSource(
            [get_package_share_directory('gazebo_ros'),'/launch','/gazebo.launch.py']
        ),
        launch_arguments=[('world',world_path),('verbose','true')]
    )
    return node

#gazebo加载节点
def gazebo_load_node():
    #拉起服务
    node=launch_ros.actions.Node(
        #包名
        package="gazebo_ros",
        #任务名
        executable="spawn_entity.py",
        #参数
        arguments=['-topic','/robot_description','-entity','robot_name']
    )
    return node

#自启动
def generate_launch_description():
    #拉起所有服务
    return launch.LaunchDescription([
        #服务
        robot_state_publisher_node(),
        # joint_state_publisher_node(),
        gazebo_ros_node(),
        gazebo_load_node()
    ])
