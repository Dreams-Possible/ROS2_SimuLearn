from setuptools import find_packages, setup

package_name = 'pkg_simu'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        #添加自启动
        ('share/' + package_name + "/launch", ['launch/pkg.launch.py']),
        #添加urdf文件
        ('share/' + package_name + "/urdf", ['urdf/pkg.urdf']),
        #添加rviz2文件
        ('share/' + package_name + "/rviz2", ['rviz2/pkg.rviz']),
        #添加gazebo文件
        ('share/' + package_name + "/gazebo", ['gazebo/pkg.world']),
        ('share/' + package_name + "/gazebo", ['gazebo/bridge.yaml']),
        #添加map文件
        ('share/' + package_name + "/map", ['map/pkg.yaml']),
        ('share/' + package_name + "/map", ['map/pkg.pgm']),
        #添加nav2文件
        ('share/' + package_name + "/nav2", ['nav2/nav2_params.yaml']),
        ('share/' + package_name + "/nav2", ['nav2/nav2_default_view.rviz']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='linux',
    maintainer_email='linux@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "pkg_init=init.init:init"
        ],
    },
)
