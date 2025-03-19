Multi-ranger deck
====================

.. contents:: 目录
    :depth: 2
    :local:

概述
----
Multi-ranger Deck 是专为 **Crazyflie 2.X 系列微型无人机** 设计的扩展模块，用于环境感知和避障。通过多方向激光测距传感器，支持无人机实现自主导航与避障功能。

核心功能
--------
- **多方向距离检测**
  - 配备 5 个激光 ToF（Time-of-Flight）传感器，覆盖前、后、左、右和上五个方向
  - 结合无人机旋转可实现 360° 障碍物检测

- **轻量化设计**
  - 重量极轻（< 10g），适配 Crazyflie 微型机身

技术参数
--------
:传感器类型:      VL53L1x 激光 ToF
:检测范围:        4cm – 4m（实际受环境光影响）
:更新速率:        最高 50 Hz
:通信接口:        I²C 总线
:供电方式:        Crazyflie 扩展接口取电
:功耗:            < 200mW


软件支持
--------
固件集成
~~~~~~~~
原生支持 Crazyflie 固件（FreeRTOS），通过以下接口调用数据：

.. code-block:: c

    // 示例：读取前方传感器数据
    uint16_t front_distance = multiRangerGetFrontRange();

Python API
~~~~~~~~~~
通过 ``cflib`` 库实现控制：

.. code-block:: python

    from cflib.crazyflie import Crazyflie
    cf = Crazyflie()
    cf.connected.add_callback(connected_callback)
    
    def connected_callback(uri):
        cf.multiranger.distance_updated.add_callback(print_data)

ROS 兼容
~~~~~~~~
通过 ``crazyflie_ros`` 包接入 ROS 系统：

.. code-block:: bash

    roslaunch crazyflie_demo multi_ranger_teleop.launch

示例代码
~~~~~~~~
GitHub 官方示例：`multi-ranger <https://github.com/bitcraze/crazyflie-lib-python/tree/master/examples/multiranger>`_

使用限制
--------
- **环境光敏感**: 强光/反光表面可能导致失效


资料下载
--------

- `数据手册 <../../../_static/products/multi-ranger-deck/datasheet/multi_ranger_deck-datasheet.pdf>`_

- `原理图(主板) <../../../_static/products/multi-ranger-deck/electronics/multi-ranger-reve.pdf>`_

- `原理图(子板) <../../../_static/products/multi-ranger-deck/electronics/multi-ranger-daughter-board-reve.pdf>`_

典型应用
--------
- 避障飞行（人工势场法/VFH+ 算法）
- 室内 SLAM（2D/3D 地图构建）
- 无人机群体协作防撞
- 控制算法教学与科研

使用手册
----------------

.. toctree::
   :maxdepth: 2
   :caption: Loco User Manual

   1_multi-ranger_deck_assembly
   2_multi-ranger_deck_getting_started
   3_multi-ranger_deck_STEM_bundle