Multi-ranger deck STEM
===========================

.. contents:: 目录
    :depth: 2
    :local:

STEM（科学技术工程数学）测距套件基于 Crazyflie 2.x 和1个Flow2 deck 和1个Multi-ranger deck 。它是一款自主无人机，可以通过简单的 Python 脚本进行控制，以在 3 维空间中探索和操作机器人。它具有检测周围障碍物的能力。

本入门指南将帮助您设置系统并进行首次自主交互式飞行。

硬件清单
--------

- 1 x Crazyflie 2.1
- 1 x Crazyradio 2.0 或 Crazyradio PA
- 1 x Flow V2 deck 
- 1 x Multi-ranger deck 

先决条件
--------

本入门指南假设您已经组装了 Crazyflie 2.x。如果不是这种情况，请按照Crazyflie 2.0 或 Crazyflie 2.1(+) 入门指南进行操作

本指南还要求您将 Crazyflie 更新到最新固件。有关如何更新固件的更多信息，请参阅Crazyflie 2.x 入门教程中Crazyflie 部分中的更新固件。

安装 Flow V2 deck
-----------------

安装Flow deck V2 下面和Multi-ranger deck 使用 Crazyflie 2.x 套件附带的长针头将其连接到 Crazyflie 2.x 上方。

.. figure:: ../../../_static/images/tutorials/getting_started_stem_ranging/getting_started_with_stem_ranging_770px.jpg
   :align: center
   :figclass: align-center

.. figure:: ../../../_static/images/tutorials/getting_started_stem_ranging/getting_started_with_stem_ranging_770px-2.jpg
   :align: center
   :figclass: align-center

有关如何安装扩展卡的更多信息，请参阅扩展卡入门教程。

安装 Python 和 cflib
--------------------

Windows安装
^^^^^^^^^^^^^^^

用于控制 Crazyflie 2.x 的后端库称为 cflib，用 python 3 编写。要使用它，您必须在计算机上安装 Pyhton 3，可以在此处下载。

使用标准设置安装 python，为了方便起见，勾选添加到 PATH 复选框。

.. figure:: ../../../_static/images/tutorials/getting_started_stem/python3_toPATH.png
   :align: center
   :figclass: align-center

安装 python 3 后，打开命令提示符并使用 pip 安装 cflib。

pip3 install cflib在命令提示符中输入

.. figure:: ../../../_static/images/tutorials/getting_started_stem/pip_cflib.png
   :align: center
   :figclass: align-center

Linux安装
^^^^^^^^^^^^^^^

以下说明已在 Ubuntu 16.04 上测试过。

要安装 Python、pip 和 Crazyflie 库，请运行以下命令：

.. code-block:: bash

    sudo apt-get install python3 python3-pip python3-usb idle3
    pip3 install cflib

您的用户需要访问 USB 设备才能使用 Crazyradio，请运行以下几行以授予访问权限。运行该命令后，需要再次插入 Crazyradio 以使规则生效。

.. code-block:: bash

    sudo groupadd plugdev
    sudo usermod -a -G plugdev $USER
    echo 'SUBSYSTEM=="usb", ATTRS{idVendor}=="1915", ATTRS{idProduct}=="7777", MODE="0664", GROUP="plugdev"' | sudo tee /etc/udev/rules.d/99-crazyradio.rules


运行你的第一个飞行脚本
--------------------------

现在，当所有设置和安装完成之后，启动 Python 编辑器 IDLE3。选择文件->新建并将下面的脚本复制/粘贴到新脚本中。使用合适的名称保存脚本。

.. code-block:: python

    """
    Example script that allows a user to "push" the Crazyflie 2.x around
    using your hands while it's hovering.

    This examples uses the Flow and Multi-ranger decks to measure distances
    in all directions and tries to keep away from anything that comes closer
    than 0.2m by setting a velocity in the opposite direction.

    The demo is ended by either pressing Ctrl-C or by holding your hand above the
    Crazyflie.
    """
    import logging
    import sys
    import time

    import cflib.crtp
    from cflib.crazyflie import Crazyflie
    from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
    from cflib.positioning.motion_commander import MotionCommander
    from cflib.utils.multiranger import Multiranger

    URI = 'radio://0/80/2M'

    if len(sys.argv) > 1:
        URI = sys.argv[1]

    # Only output errors from the logging framework
    logging.basicConfig(level=logging.ERROR)


    def is_close(range):
        MIN_DISTANCE = 0.2  # m

        if range is None:
            return False
        else:
            return range < MIN_DISTANCE


    if __name__ == '__main__':
        # Initialize the low-level drivers (don't list the debug drivers)
        cflib.crtp.init_drivers(enable_debug_driver=False)

        cf = Crazyflie(rw_cache='./cache')
        with SyncCrazyflie(URI, cf=cf) as scf:
            # Arm the Crazyflie
            scf.cf.platform.send_arming_request(True)
            time.sleep(1.0)

            with MotionCommander(scf) as motion_commander:
                with Multiranger(scf) as multi_ranger:
                    keep_flying = True

                    while keep_flying:
                        VELOCITY = 0.5
                        velocity_x = 0.0
                        velocity_y = 0.0

                        if is_close(multi_ranger.front):
                            velocity_x -= VELOCITY
                        if is_close(multi_ranger.back):
                            velocity_x += VELOCITY

                        if is_close(multi_ranger.left):
                            velocity_y -= VELOCITY
                        if is_close(multi_ranger.right):
                            velocity_y += VELOCITY

                        if is_close(multi_ranger.up):
                            keep_flying = False

                        motion_commander.start_linear_motion(
                            velocity_x, velocity_y, 0)

                        time.sleep(0.1)

                print('Demo terminated!')

按 F5 运行脚本。

注意：如果您打开了 Python 客户端，请确保 Crazyflie 已与其断开连接。Crazyradio 不支持同时连接多个程序，如果 Crazyflie 仍连接到 Python 客户端，脚本将不起作用。

输出应与此类似。

.. code-block:: bash

    Connecting to radio://0/110/2M
    Connected to radio://0/110/2M
    Demo terminated!

视频展示
--------

.. raw:: html

   <div style="text-align: center">
      <video width="100%" height="auto" controls autoplay muted loop>
         <source src="../../../_static/videos/stem_ranging_bundle.mp4" type="video/mp4">
         Your browser does not support the video tag.
      </video>
   </div>