ROS2与Lighthouse定位系统-测试单台无人机起飞和降落
===============================================
说明
--------------------------------

介绍如何通过crazyswarm2测试单台无人机的8字飞行
本测试基于无人机集群主机配置，如果是自己配置，请参考官方文档
Crazyflie无人机集群套件 `采购地址 <https://item.taobao.com/item.htm?ft=t&id=858112103307&spm=a21dvs.23580594.0.0.52de2c1bg17fUu>`_
仿真飞行
在真机测试之前，我们先做以下仿真
进入目录
cd scripts_ros
scripts_ros是一个软连接，对应到crazyswarm2/crazyflie_examples/crazyflie_examples目录
仿真运行，启动launch文件，并指定为仿真

.. code-block:: bash

ubuntu@Crazeflie-NUC:~/scripts_ros2$ ros2 launch crazyflie launch.py backend:=sim
[INFO] [launch]: All log files can be found below /home/ubuntu/.ros/log/2024-04-03-11-35-24-423922-Crazeflie-NUC-21702
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [crazyflie_server-3]: process started with pid [21708]
[INFO] [teleop-1]: process started with pid [21704]
[INFO] [joy_node-2]: process started with pid [21706]
[INFO] [gui.py-4]: process started with pid [21710]
[teleop-1] [INFO] [1712115325.375741980] [teleop]: Mode changed to cmd_vel_world
之后后，会弹出一个nicegui页面，效果如图：
请输入图片描述

执行figure8命令
ros2 run crazyflie_examples figure8 --ros-args -p use_sim_time:=True
过几秒，在nicegui页面无人机开始缓慢上升，停留几秒，开始8字绕飞，最后回到中心点，再缓慢降落
真机测试
1号无人机放置在基站测试区域中心
同时配置好crazyflies.yaml为1号无人机
效果图：
请输入图片描述

终端下启动launch文件
ros2 launch crazyflie launch.py
新终端，执行hello_world命令
ros2 run crazyflie_examples figure8 
过几秒，无人机开始缓慢上升，停留几秒，开始8字绕飞，最后回到中心点，再缓慢降落，效果和仿真一致