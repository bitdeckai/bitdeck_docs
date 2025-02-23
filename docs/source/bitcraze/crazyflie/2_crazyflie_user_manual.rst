========
Crazyflie 2.X 快速入门
========


==== ========================= ========================= ================== ========================== ==============
序号 模块名                    主要元器件                功能               接口                       安装位置
==== ========================= ========================= ================== ========================== ==============
1    主控制板 - **STM32F405**  STM32F405 + nRF51822      基础飞行           提供 I2C SPI GPIO 扩展接口
2    扩展板 - **定点模块**     PMW3901 + VL53L1X         室内定点飞行       SPI + I2C                  底部，面向地面
==== ========================= ========================= ================== ========================== ==============

硬件组装
----------

请按照下述步骤组装 ESP32-S2-Drone V1.2：

.. figure:: ../../_static/images/assembling.png
   :align: center
   :alt: ESP32-S2-Drone V1.2 组装流程
   :figclass: align-center
   
   ESP32-S2-Drone V1.2 组装流程

硬件介绍和管脚资源分配可查阅：`硬件参考 <./hardware.rst>`__。

**扫描下方二维码，下载 Android APP：**

.. figure:: ../../_static/images/android_app_download.png
   :align: center
   :alt: Android APP 扫码下载
   :figclass: align-center

**下载 iOS APP：**

在 App Store 中搜索 ESP-Drone，点击下载并安装。

**iOS APP 源代码**：`ESP-Drone-iOS <https://github.com/EspressifApps/ESP-Drone-iOS>`__

**Android APP 源代码**：`ESP-Drone-Android <https://github.com/EspressifApps/ESP-Drone-Android>`__

安装 cfclient
--------------------

安装 cfclient 为可选步骤，用于实现高级调试，非必须使用。

.. figure:: ../../_static/images/cfclient.png
   :align: center
   :alt: cfclient 上位机界面
   :figclass: align-center

   cfclient 上位机界面


**1. 安装 cfclient**

1.1 下载源代码

.. code:: text

   git clone https://github.com/qljz1993/crazyflie-clients-python.git

1.2 进入下载目录

.. code:: text

   cd crazyflie-clients-python

1.3 安装 cfclient 客户端

.. code:: text

   pip3 install -e .

1.4 启动客户端

.. code:: text

   cfclient

**2. 配置遥控器**

.. figure:: ../../_static/images/gamepad_settings.png
   :align: center
   :alt: 游戏手柄配置
   :figclass: align-center

   遥控器配置

2.1 配置 4 个控制轴：``Roll 、Pitch、Yaw、Thrust``。

2.2 配置一个按键为 ``Assisted control``，用于飞行模式切换。


控制飞行
--------

-  打开 APP，点击 `Connect` 按钮，连接小飞机。连接成功，小飞机绿灯闪烁。
-  轻推油门，小飞机起飞。
-  在 APP 上滑动，控制小飞机方向。

.. figure:: ../../_static/images/espdrone_app_android.png
   :align: center
   :alt: Android APP 用户界面
   :figclass: align-center

   Android APP 用户界面

PC cfclient 使用指南
========================

cfclient 是 ``Crazeflie`` 源工程的上位机，完全实现了 ``CRTP``
协议中定义的功能，可以加快飞机的调试过程。ESP-Drone
项目对该上位机进行裁剪和调整，满足功能设计需求。

.. figure:: ../../_static/images/cfclient_architecture.png
   :align: center
   :alt: cfclient 架构
   :figclass: align-center

   cfclient 架构

.. figure:: ../../_static/images/cfclient.png
   :align: center
   :alt: cfclient 控制台界面
   :figclass: align-center

   cfclient 控制台界面

项目中有很多相关的文件，例如配置文件和缓存文件，其中 JSON
文件用来存储配置信息。关于配置信息中内容的解读，可参考：`User
Configuration
File <https://www.bitcraze.io/documentation/repository/crazyflie-clients-python/master/development/dev_info_client/>`__。

飞行设置
----------

基本飞行设置 (Basic Flight Control)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. 飞行模式 (Flight mode)：基本模式和高级模式

   -  基本模式 (Normal mode)：初学者使用。
   -  高级模式 (Advanced mode)：设置解锁最大角度，设置最大油门。

2. 自动模式 (Assisted mode)

   -  定海拔模式 (Altitude-hold mode)：保持飞行海拔，需要气压计支持。
   -  定点模式 (Position-hold mode)：保持当前位置，需要光流和 TOF 支持。
   -  定高模式 (Height-hold mode)：保持相对高度，触发时保持高于地面 40
      cm，需要 TOF 支持。
   -  悬停模式 (Hover mode)：触发时保持高于地面 40
      cm，并悬停在起飞点，需要光流和 TOF 支持。

3. 角度修正 (Trim)

   -  翻滚角修正 (Roll Trim)：用于弥补传感器水平安装误差。
   -  俯仰角修正 (Pitch Trim)：用于弥补传感器水平安装误差。

注意，在自动模式下，油门摇杆变为高度控制摇杆。

高级飞行设置 (Advanced Flight Control)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. 最大倾角 (Max angle)：设置最大允许的俯仰和翻滚角度：roll/pitch。
2. 最大自旋速度 (Max yaw rate)：设置允许的偏航速度：yaw。
3. 最大油门 (Max thrust)：设置最大油门。
4. 最小油门 (Min thrust)：设置最小油门。
5. 压摆极限 (Slew limit)：防止油门骤降，油门低于该值时，下降速度将被限定。
6. 压摆率 (Slew rate)：油门到压摆极限之后的最大下降率。

遥控器设置 (Configure Input Device)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

按照提示绑定遥控器摇杆与各个控制通道：

.. figure:: ../../_static/images/gamepad_set.png
   :align: center
   :alt: cfclient 控制器配置
   :figclass: align-center

飞行数据 (Flight Data)
~~~~~~~~~~~~~~~~~~~~~~~~~~

驾驶仪可以看到当前飞机姿态，右下方显示对应的详细数据。

1. 目标角度 (Target)
2. 测量角度 (Actual)
3. 当前油门值 (Thrust)
4. 电机实际输出 (M1/M2/M3/M4)

在线参数修改
--------------------

**在线调整 PID 参数**

.. figure:: ../../_static/images/cfclient_pid_tune.png
   :align: center
   :alt: PID 参数调整
   :figclass: align-center
   
   cfclient PID 参数调整

**注意事项**

1. 修改的参数实时生效，避免了频繁烧录固件。
2. 可在代码中通过宏定义，配置哪些参数可被上位机实时修改。
3. 注意，参数在线修改仅用于调试，掉电不保存。


飞行数据监控
--------------------

**配置要监控的参数**

.. figure:: ../../_static/images/log_set.png
   :align: center
   :alt: PID 参数调整
   :figclass: align-center

   监控参数配置

   .. figure:: ../../_static/images/log_set2.png
   :align: center
   :alt: PID 参数调整
   :figclass: align-center

   参数配置区

**实时波形绘制**

陀螺仪加速度计实时数据监测：

.. figure:: ../../_static/images/log_acc.png
   :align: center
   :alt: PID 参数调整
   :figclass: align-center

   陀螺仪加速度计数据监测

螺旋桨方向
================

-  按照下图所示位置，安装 A、B 螺旋桨。
-  飞行器上电自检时，检查螺旋桨转向是否正确。

.. figure:: ../../_static/images/espdrone_s2_v1_2_diretion2.png
   :align: center
   :alt: 螺旋桨方向示图
   :figclass: align-center

   螺旋桨方向示图

起飞前检查
================

-  将小飞机头部朝前放置，尾部天线朝向自己；
-  将小飞机置于水平面上，待机身稳定时上电；
-  观察上位机水平面是否置平；
-  观察通信建立以后，小飞机尾部绿灯是否快速闪烁；
-  观察小飞机头部红灯是否熄灭，亮起代表电量不足；
-  轻推左手小油门，检查飞机是否能快速响应；
-  轻推右手方向，检查方向控制是否正确；
-  起飞吧！
