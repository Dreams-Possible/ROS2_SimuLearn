## 环境相关
1. 请使用env或类似的虚拟环境  
ros2暂不支持和预编译好的conda环境一同运行
2. 本项目基于ROS2 Humbel+Classic Gazebo
请确定你要使用的环境，自行安装ROS2

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
sudo apt install ros-$ROS_DISTRO-robot-state-publisher
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
1. 安装classic gazebo
```
sudo apt install ros-${ROS_DISTRO}-gazebo-ros
```
2. 启动
```
gazebo
```
3. 安装gazebo插件包
```
sudo apt install ros-${ROS_DISTRO}-gazebo-ros-pkgs
```

## 键盘控制相关
1. 安装键盘控制包
```
sudo apt install ros-${ROS_DISTRO}-teleop-twist-keyboard
```
2. 启动键盘控制节点
```
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

## 建图相关
1. 安装slam—toolbox插件包
```
sudo apt install ros-$ROS_DISTRO-slam-toolbox
```
2. 启动建图
```
ros2 launch slam_toolbox online_async_launch.py use_sim_time:=True
```
3. 安装nav2-map-server插件包
```
sudo apt install ros-$ROS_DISTRO-nav2-map-server
```
4. 保存地图
```
#打开要保存的文件夹
cd ./pkg_simu/map
ros2 run nav2_map_server map_saver_cli -f map
```

## 导航相关
1. 安装navigation2插件包
```
sudo apt install ros-$ROS_DISTRO-navigation2
```
2. 安装nav2示例功能包
```
sudo apt install ros-$ROS_DISTRO-nav2-bringup
```
3. 配置文件默认路径
```
# 默认参数
/opt/ros/$ROS_DISTRO/share/nav2_bringup/params/params/nav2_params.yaml
# 默认rviz
/opt/ros/$ROS_DISTRO/share/nav2_bringup/params/rviz/nav2_default_view.rviz

```

## 例程使用说明
1. 打开构建目录
```
cd /path/to/build
```
2. 激活环境
```
#激活ROS2环境
source /opt/ros/humble/setup.bash
#激活虚拟环境
source /path/to/venv/activate
```
3. 构建包并激活
```
colcon build
source path/to/pkg/./install/setup.bash
```
4. 运行gazebo仿真
```
ros2 launch pkg_simu pkg.launch.py
```
5. 打开rqt查看tfTree
```
见上rqt部分
```
7. 启动键盘控制节点（如果想自己操作）
```
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```
8. rviz2中使用自动导航
```
使用nav2goal即可设置目标点
```

### 其他
1. 顺带一提，因为classic gazebo停止维护的原因，gazebo_ros_pkg也停止了更新  
但由于种种原因，classic gazebo和ros那边的描述文档并没有对齐颗粒度  
请参阅这一节中的**Plugin in the original model**来获取最新的插件语法
```
https://gazebosim.org/docs/harmonic/migrating_gazebo_classic_ros2_packages/#modify-the-model
```
2. 对于ros2导航来说，地图路径中不能出现中文  
虽然linux一般默认utf8,但可能是由于nav2的mapio中出现了某些神秘代码，导致其无法识别中文路径  
为什么专门说呢，因为ubuntu如果你安装的时候选的中文，桌面文件夹的名字就叫“桌面”  
自行把工程和环境修改到不含中文路径的文件夹内，推荐新建～/Desktop，和“桌面”同级，可以在“桌面”创建一个符号链接方便的指向Desktop  
为什么不用Desktop彻底替换“桌面”呢？因为ubuntu的资源管理器硬编码了这些用户文件夹的路径...所以不建议修改原来的
3. 关于局部代价地图  
对于humble来说，ros2bringup默认使用DWB局部控制器
部分极端场景，比如路径上包含锐角等，可以尝试把局部代价地图范围设置小一些，或使用分段导航  
