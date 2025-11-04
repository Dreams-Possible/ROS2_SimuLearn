import rclpy
from geometry_msgs.msg import PoseStamped
from nav2_simple_commander.robot_navigator import BasicNavigator

#导航加载初始位置
def nav2_load_pos():
    rclpy.init()
    nav=BasicNavigator()
    init_pos=PoseStamped()
    init_pos.header.frame_id="map"
    init_pos.pose.position.x=0.0
    init_pos.pose.position.y=0.0
    init_pos.pose.orientation.w=1.0
    nav.setInitialPose(init_pos)
    nav.waitUntilNav2Active()
    rclpy.spin(nav)
    rclpy.shutdown()

#初始化
def init():
    #初始化
    nav2_load_pos()
