# ROS2_SimuLearn
## 自学ROS2Humble+ClassicGazebo仿真留档，内容是一个扫地机器人。
### v1 
* 例程中在一个空的venv虚拟环境中搭建，虚拟环境请自行准备，缺失的几个依赖包很容易根据报错补全。
* 请使用venv或类似的虚拟环境，不要使用conda，因为它的python二进制构建似乎不受ros2支持。
* 如使用conda环境，任何显式的import rclpy均会报错，如果使用pkg包，则不会有任何报错，也不会产生任何实际的效果。
<img width="2114" height="805" alt="image" src="https://github.com/user-attachments/assets/1ea0cd6b-24ce-49cf-b5f8-160177641cb5" />
### v2
* 对包结构进行了一些调整，看起来更合理
* 增加了nav2自主导航系统
* 完善了launch文件使测试过程更加自动化
* 完善了readme.md
