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
        #添加gazebo文件
        ('share/' + package_name + "/gazebo", ['gazebo/pkg.world']),
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
        ],
    },
)
