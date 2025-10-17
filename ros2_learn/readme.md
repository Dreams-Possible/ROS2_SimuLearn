## 创建ros2功能包
1. 指定为python包
```
ros2 pkg create --build-type ament_python 包名
```
2. 启动功能包（通过launch文件）
```
ros2 launch 功能包 launch启动文件
```
## rqt相关
1. 安装tf查看工具
```
sudo apt install ros-$ROS_DISTRO-rqt-tf-tree
```
2. 删除旧的配置文件以便于自动更新配置文件
```
rm -r ~/.config/ros.org/rqt_gui.ini
```
3. 图形化查看
* 打开rqt
* Plgins
* Visualization
* TF Tree

## tf相关
1. 安装tf工具
```
sudo apt install ros-$ROS_DISTRO-robots-tate-publisher
sudo apt install ros-$ROS_DISTRO-joint-state-publisher
```
## xacro相关
1. 安装xacro工具
```
sudo apt install ros-$ROS_DISTRO-xacro
```
2. 检查xarco文件
```
ros2 run xacro xacro 文件路径
```
3. 输出xacro文件
```
ros2 run xacro xacro 输入xacro文件路径 > 输出urdf文件路径
```
## gazebo相关
1. 安装
```
sudo apt install ros-${ROS_DISTRO}-gazebo-ros #传统gazebo，支持较多，建议使用
sudo apt-get install ros-${ROS_DISTRO}-ros-gz #新gazebo，自持较少，不建议使用
sudo apt install gazebo #gazebo独立本体，若有问题再单独安装
```
2. 启动
```
. /opt/ros/${ROS_DISTRO}/setup.bash #刷新ros2
gazebo
```
3. 安装gazebo插件包
```
sudo apt install ros-${ROS_DISTRO}-gazebo-ros-pkgs
```
4. 安装键盘控制包
```
sudo apt install ros-${ROS_DISTRO}-teleop-twist-keyboard
```
5. 启动键盘控制节点
```
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```
## 例程使用说明
1. 打开构建目录
```
cd ~/桌面/ros2_learn/py_ros2_src/ros2_pkg/simu_v1
```
2. 激活环境
```
source ~/桌面/ros2_learn/py_ros2_env/bin/activate
```
3. 运行gazebo仿真
```
ros2 launch pkg_simu pkg.launch.py
```
4. 打开rqt查看tfTree
```
见上rqt部分
```
5. 打开rviz2查看模型
```
打开rviz2
使用pkg_simu目录下的simu/src/rviz2配置文件
如果不动点一下左下角reset
```
6. 启动键盘控制节点
```
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```
### 其他
1. 顺带一提，因为老gazebo停止维护的原因，gazebo_ros_pkg也停止了更新
2. 但是很坑的是，其附带的plugin api后来出现了一些变化
3. 具体来说
```
本来使用文档应该在：gazebo官网（现在是classic gazebo）：
https://classic.gazebosim.org/tutorials?tut=ros_gzplugins&cat=connect_ros
```
```
结果因为部分api发生了更新，于是ros在其plugin部分的文档单独进行了更新（由于某些原因classic gazebo官网文档并没有同步更新）
但ros官网上只贴出了部分更新的api（并非全部api都进行了更新），完整api仍然需要去classic gazebo查看，之后替换调更新的部分
ros的plugin文档官网：
https://docs.ros.org/en/rolling/p/gazebo_plugins/generated
```
