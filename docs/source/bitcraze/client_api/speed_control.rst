速度控制
=======================

   控制 Crazyflie 速度的一个简单方法是使用Motion Commander，它具有前进、左转、右转和后退等功能，这些功能以速度为参数。
   motion_commander_demo.py展示了多种使用方法，你也可以查看 Motion Commander 的分步教程来开始使用。

   - https://github.com/bitcraze/crazyflie-lib-python/blob/95d912657b22e2869b84bc512af624de9940474b/cflib/positioning/motion_commander.py
   - https://github.com/bitcraze/crazyflie-lib-python/blob/95d912657b22e2869b84bc512af624de9940474b/examples/autonomy/motion_commander_demo.py
   - https://www.bitcraze.io/documentation/repository/crazyflie-lib-python/master/user-guides/sbs_motion_commander/

   这里我们将逐步讲解如何基于运动脚本让 crazyflie 动起来。本教程的第一部分只需要 crazyflie 和 Flow Deck。第二部分则需要 MultiRanger 的支持。

使用条件
-------------------------

我们假设您在开始本教程之前已经了解如下内容：

   - Python 基本经验
   - 遵循crazyflie 入门指南以及连接、日志记录和参数教程。

启动脚本
-------------------------

由于您应该已经在上一步教程中安装了 cflib，所以现在一切准备就绪。打开一个名为 的新 Python 脚本motion_flying.py。首先，您需要在脚本中添加以下导入：

.. code-block:: C

   import logging
   import sys
   import time
   from threading import Event

   import cflib.crtp
   from cflib.crazyflie import Crazyflie
   from cflib.crazyflie.log import LogConfig
   from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
   from cflib.positioning.motion_commander import MotionCommander
   from cflib.utils import uri_helper


   URI = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E7')

   DEFAULT_HEIGHT = 0.5
   BOX_LIMIT = 0.5

   if __name__ == '__main__':

      cflib.crtp.init_drivers()
      with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:
      
这一切可能看起来都很熟悉，除了一行，即：

   from cflib.positioning.motion_commander import MotionCommander

这将导入运动控制器，它基本上是对 crazyflie 位置设定点框架的封装。你可能在使用 cfclient 中的 flow deck 尝试本教程中的辅助模式时，不知不觉地体验过这一点。

第一步：飞行前安检
--------------------------

由于本教程不像上次那样是桌面教程，而是实际飞行教程，因此我们需要采取一些安全措施。您使用的 Flow 平台必须正确连接到 CrazyFlie 上。否则，它会在没有良好位置估计的情况下尝试飞行，最终肯定会坠毁。

我们想在飞行前知道甲板是否正确安装，因此需要为该参数添加一个回调函数。在in"deck.bcFlow2"之后添加以下代码：...SyncCrazyflie(...)__main__

.. code-block:: C

   with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:

   scf.cf.param.add_update_callback(group="deck", name="bcFlow2",
                           cb=param_deck_flow)
   time.sleep(1)

上面__main__，启动一个参数回调函数：

.. code-block:: C

   def param_deck_flow(_, value_str):
      value = int(value_str)
      print(value)
      if value:
         deck_attached_event.set()
         print('Deck is attached!')
      else:
         print('Deck is NOT attached!')

deck_attached_event是一个全局变量，定义在URI。请注意param_deck_flow()是字符串类型，因此您需要先将其转换为数字，然后才能对其进行任何操作。

.. code-block:: C

   ...
   URI = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E7')
   deck_attached_event = Event()

现在尝试运行脚本，看看它是否能够检测到流动甲板是否已正确连接。同时尝试将其移除，看看它是否也能检测到它缺失的情况。

   注意：您可以根据需要使用不同的定位系统和甲板，但需要查看与“deck.bcFlow2”不同的参数。请查看参数列表中的其他选项。

这是我们的完整脚本：

.. code-block:: C

   import logging
   import sys
   import time
   from threading import Event

   import cflib.crtp
   from cflib.crazyflie import Crazyflie
   from cflib.crazyflie.log import LogConfig
   from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
   from cflib.positioning.motion_commander import MotionCommander
   from cflib.utils import uri_helper

   URI = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E7')

   deck_attached_event = Event()

   logging.basicConfig(level=logging.ERROR)

   def param_deck_flow(_, value_str):
      value = int(value_str)
      print(value)
      if value:
         deck_attached_event.set()
         print('Deck is attached!')
      else:
         print('Deck is NOT attached!')


   if __name__ == '__main__':
      cflib.crtp.init_drivers()

      with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:

         scf.cf.param.add_update_callback(group='deck', name='bcFlow2',
                                          cb=param_deck_flow)
         time.sleep(1)

第 2 步：起飞功能
--------------------------

所以现在我们要启动SyncCrazyflie并在__main__函数中启动一个功能：

.. code-block:: C

   with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:

         if not deck_attached_event.wait(timeout=5):
               print('No flow deck detected!')
               sys.exit(1)

         # Arm the Crazyflie
         scf.cf.platform.send_arming_request(True)
         time.sleep(1.0)

         take_off_simple(scf)

看到我们现在使用了deck_attached_event.wait()? 吗? 如果返回 false，则不会调用该函数，crazyflie 也不会起飞。

take_off_simple(..)现在制作上面的函数__main__，它将包含运动指挥官实例。

.. code-block:: C

   def take_off_simple(scf):
      with MotionCommander(scf, default_height=DEFAULT_HEIGHT) as mc:
         time.sleep(3)
         mc.stop()

如果你运行 Python 脚本，你会看到 CrazyFlie 连接成功并立即起飞。飞行 3 秒后，它会再次降落。

crazyflie 立即起飞的原因是，运动控制器已初始化起飞函数，该函数会立即向 crazyflie 发送位置设定值。脚本退出实例后，运动控制器实例将以着陆函数关闭。

改变高度
----------------

目前，运动指挥官的默认高度为 0.3 米，但当然可以更改。

更改以下行take_off_simple(...)：

.. code-block:: C

    with MotionCommander(scf) as mc:
        mc.up(0.3)
        time.sleep(3)
        mc.stop()

再次运行脚本。crazyflie 会先起飞至 0.3 米，然后再上升 0.3 米。

同样的，也可以通过调整 motion_commander 的 default_height 来实现，这也是我们在本教程中接下来要做的事情。移除 ，mc.up(0.3)并将 motion commander 行替换为

.. code-block:: C

    with MotionCommander(scf, default_height = DEFAULT_HEIGHT) as mc:

添加下面的变量URI：

.. code-block:: C

   DEFAULT_HEIGHT = 0.5

仔细检查你的脚本是否与下面的相同，然后再次运行以检查

.. code-block:: C

   import logging
   import sys
   import time
   from threading import Event

   import cflib.crtp
   from cflib.crazyflie import Crazyflie
   from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
   from cflib.positioning.motion_commander import MotionCommander
   from cflib.utils import uri_helper

   URI = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E7')

   DEFAULT_HEIGHT = 0.5

   deck_attached_event = Event()

   logging.basicConfig(level=logging.ERROR)

   def take_off_simple(scf):
      with MotionCommander(scf, default_height=DEFAULT_HEIGHT) as mc:
         time.sleep(3)
         mc.stop()


   def param_deck_flow(name, value_str):
      ...

   if __name__ == '__main__':
      cflib.crtp.init_drivers()

      with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:

         scf.cf.param.add_update_callback(group='deck', name='bcFlow2',
                                          cb=param_deck_flow)
         time.sleep(1)

         if not deck_attached_event.wait(timeout=5):
               print('No flow deck detected!')
               sys.exit(1)

         # Arm the Crazyflie
         scf.cf.platform.send_arming_request(True)
         time.sleep(1.0)

         take_off_simple(scf)

步骤 3 前进、转弯、后退
--------------------------

现在我们知道了如何起飞，第二步就是朝一个方向移动！在上面启动一个新函数def take_off_simple(scf)：

.. code-block:: C

   def move_linear_simple(scf):
      with MotionCommander(scf, default_height=DEFAULT_HEIGHT) as mc:
         time.sleep(1)
         mc.forward(0.5)
         time.sleep(1)
         mc.back(0.5)
         time.sleep(1)

如果将 替换为take_off_simple(scf)，请尝试运行该脚本。__main__move_linear_simple(scf)

您将看到 crazyflie 起飞，向前飞行 0.5 米，向后飞行并再次着陆。

现在我们要添加一个转弯。将 motion commander 下的内容替换move_linear_simple(..)为以下内容：

.. code-block:: C

        time.sleep(1)
        mc.forward(0.5)
        time.sleep(1)
        mc.turn_left(180)
        time.sleep(1)
        mc.forward(0.5)
        time.sleep(1)

尝试再次运行脚本。现在你可以看到 CrazyFlie 起飞、前进、旋转 180 度，然后再次前进到初始位置。由于运动控制器在固定体mc.back()坐标系中发送速度设定值，因此需要将 替换为 前进。这意味着前进命令将前进到 CrazyFlie 当前航向（前方）指向的任何位置。

仔细检查您的代码是否仍然正确：

.. code-block:: C

   import logging
   import sys
   import time
   from threading import Event

   import cflib.crtp
   from cflib.crazyflie import Crazyflie
   from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
   from cflib.positioning.motion_commander import MotionCommander
   from cflib.utils import uri_helper

   URI = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E7')

   DEFAULT_HEIGHT = 0.5

   deck_attached_event = Event()
   logging.basicConfig(level=logging.ERROR)


   def move_linear_simple(scf):
      with MotionCommander(scf, default_height=DEFAULT_HEIGHT) as mc:
         time.sleep(1)
         mc.forward(0.5)
         time.sleep(1)
         mc.turn_left(180)
         time.sleep(1)
         mc.forward(0.5)
         time.sleep(1)


   def take_off_simple(scf):
      ...

   def param_deck_flow(name, value_str):
      ...


   if __name__ == '__main__':
      cflib.crtp.init_drivers()

      with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:

         scf.cf.param.add_update_callback(group='deck', name='bcFlow2',
                                          cb=param_deck_flow)
         time.sleep(1)

         if not deck_attached_event.wait(timeout=5):
               print('No flow deck detected!')
               sys.exit(1)

         # Arm the Crazyflie
         scf.cf.platform.send_arming_request(True)
         time.sleep(1.0)

         move_linear_simple(scf)

步骤 4：飞行时记录
--------------------------

当运动控制器命令执行完毕后，脚本停止，CrazyFlie 着陆……不过这样有点无聊。或许你希望它能继续飞行，同时响应某些动作！

让我们也集成一些日志记录。将以下日志配置添加__main__到SyncCrazyflie

.. code-block:: C

    logconf = LogConfig(name='Position', period_in_ms=10)
    logconf.add_variable('stateEstimate.x', 'float')
    logconf.add_variable('stateEstimate.y', 'float')
    scf.cf.log.add_config(logconf)
    logconf.data_received_cb.add_callback(log_pos_callback)

    if not deck_attached_event.wait(timeout=5):
        print('No flow deck detected!')
        sys.exit(1)

    logconf.start()

    move_linear_simple(scf)

    logconf.stop()

别忘了from cflib.crazyflie.log import LogConfig在导入中添加（我们不需要同步记录器，因为我们要使用回调）。将函数写log_pos_callback在 param_deck_flow 上方：

.. code-block:: C

   def log_pos_callback(timestamp, data, logconf):
       print(data)

现在：创建一个全局变量，该变量是一个列表，名为position_estimate，并在日志回调函数中用 x 和 y 位置填充它。这data是一个字典结构。

只需再次检查所有操作是否正确实现，然后运行脚本即可。您将看到与上一步相同的行为，但同时会打印出估算的位置。

如果您想尝试的话，您可以用绘图仪替换回调中的打印函数，就像使用 python lib matplotlib 一样:)

.. code-block:: C

   import logging
   import sys
   import time
   from threading import Event

   import cflib.crtp
   from cflib.crazyflie import Crazyflie
   from cflib.crazyflie.log import LogConfig
   from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
   from cflib.positioning.motion_commander import MotionCommander
   from cflib.utils import uri_helper


   URI = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E7')

   DEFAULT_HEIGHT = 0.5

   deck_attached_event = Event()

   logging.basicConfig(level=logging.ERROR)

   position_estimate = [0, 0]

   def move_linear_simple(scf):
      with MotionCommander(scf, default_height=DEFAULT_HEIGHT) as mc:
         time.sleep(1)
         mc.forward(0.5)
         time.sleep(1)
         mc.turn_left(180)
         time.sleep(1)
         mc.forward(0.5)
         time.sleep(1)


   def take_off_simple(scf):
      ...

   def log_pos_callback(timestamp, data, logconf):
      print(data)
      global position_estimate
      position_estimate[0] = data['stateEstimate.x']
      position_estimate[1] = data['stateEstimate.y']


   def param_deck_flow(name, value_str):
      ...

   if __name__ == '__main__':
      cflib.crtp.init_drivers()

      with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:

         scf.cf.param.add_update_callback(group='deck', name='bcFlow2',
                                          cb=param_deck_flow)
         time.sleep(1)

         logconf = LogConfig(name='Position', period_in_ms=10)
         logconf.add_variable('stateEstimate.x', 'float')
         logconf.add_variable('stateEstimate.y', 'float')
         scf.cf.log.add_config(logconf)
         logconf.data_received_cb.add_callback(log_pos_callback)

         if not deck_attached_event.wait(timeout=5):
               print('No flow deck detected!')
               sys.exit(1)

         # Arm the Crazyflie
         scf.cf.platform.send_arming_request(True)
         time.sleep(1.0)

         logconf.start()

         move_linear_simple(scf)
         logconf.stop()

步骤 5：结合日志记录和运动指挥
--------------------------------

我们放置position_estimate来从日志中捕获位置是有原因的，因为我们现在想用它做一些事情！

来回限制
^^^^^^^^^

让我们从上面的一个新功能开始move_linear_simple(scf)：

.. code-block:: C

   def move_box_limit(scf):
      with MotionCommander(scf, default_height=DEFAULT_HEIGHT) as mc:

         while (1):

               time.sleep(0.1)

如果你运行这段代码（别忘了替换move_linear_simple()成__main__），你会看到 crazyflie 起飞了，但它会停留在空中。键盘中断（ctrl+c）会停止脚本，让 crazyflie 再次降落。

现在我们将在 while 循环中添加一些行为：

.. code-block:: C

   def move_box_limit(scf):
      with MotionCommander(scf, default_height=DEFAULT_HEIGHT) as mc:
         mc.start_forward()

         while (1):
               if position_estimate[0] > BOX_LIMIT:
                  mc.start_back()
               elif position_estimate[0] < -BOX_LIMIT:
                  mc.start_forward()
               time.sleep(0.1)

BOX_LIMIT = 0.5在 的定义下方添加DEFAULT_HEIGHT = 0.5。

运行脚本，你会看到 crazyflie 会开始来回移动，直到你按下 ctrl+c。它会根据日志输入（即状态估计的 x 和 y 位置）更改其命令。一旦它指示到达“虚拟”边界，它就会改变方向。

   你可能也注意到了，我们用的是mc.start_back()and ，mc.start_forward()而不是前面步骤中的mc.forward(0.5)and mc.back(0.5)。主要区别在于mc.forward和mc.back是阻塞函数，在达到指定距离之前不会继续执行代码。
   
   mc.start …()会启动 crazyflie 并朝指定方向飞行，直到给定 才会停止mc.stop()，而该指令会在运动控制器实例退出时自动执行。正因如此，这些函数非常适合用于这类被动式场景。

.. code-block:: C

   import logging
   import sys
   import time
   from threading import Event

   import cflib.crtp
   from cflib.crazyflie import Crazyflie
   from cflib.crazyflie.log import LogConfig
   from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
   from cflib.positioning.motion_commander import MotionCommander
   from cflib.utils import uri_helper

   URI = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E7')

   DEFAULT_HEIGHT = 0.5
   BOX_LIMIT = 0.5

   deck_attached_event = Event()

   logging.basicConfig(level=logging.ERROR)

   position_estimate = [0, 0]


   def move_box_limit(scf):
      with MotionCommander(scf, default_height=DEFAULT_HEIGHT) as mc:
         while (1):
               if position_estimate[0] > BOX_LIMIT:
                  mc.start_back()
               elif position_estimate[0] < -BOX_LIMIT:
                  mc.start_forward()

   def move_linear_simple(scf):
      ...

   def take_off_simple(scf):
      ...

   def log_pos_callback(timestamp, data, logconf):
      ...

   def param_deck_flow(name, value_str):
      ...

   if __name__ == '__main__':
      cflib.crtp.init_drivers()

      with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:

         scf.cf.param.add_update_callback(group='deck', name='bcFlow2',
                                          cb=param_deck_flow)
         time.sleep(1)

         logconf = LogConfig(name='Position', period_in_ms=10)
         logconf.add_variable('stateEstimate.x', 'float')
         logconf.add_variable('stateEstimate.y', 'float')
         scf.cf.log.add_config(logconf)
         logconf.data_received_cb.add_callback(log_pos_callback)

         if not deck_attached_event.wait(timeout=5):
               print('No flow deck detected!')
               sys.exit(1)

         # Arm the Crazyflie
         scf.cf.platform.send_arming_request(True)
         time.sleep(1.0)

         logconf.start()
         move_box_limit(scf)
         logconf.stop()

在边界框中弹跳
^^^^^^^^^^^^^^^^^^

让我们更进一步！将 while 循环中的内容替换为以下内容：

.. code-block:: C

        body_x_cmd = 0.2
        body_y_cmd = 0.1
        max_vel = 0.2

        while (1):
            if position_estimate[0] > BOX_LIMIT:
                 body_x_cmd=-max_vel
            elif position_estimate[0] < -BOX_LIMIT:
                body_x_cmd=max_vel
            if position_estimate[1] > BOX_LIMIT:
                body_y_cmd=-max_vel
            elif position_estimate[1] < -BOX_LIMIT:
                body_y_cmd=max_vel

            mc.start_linear_motion(body_x_cmd, body_y_cmd, 0)

            time.sleep(0.1)

现在，Crazyflie 会开始沿特定方向进行线性运动，并使其在一个虚拟框内弹跳，该框的大小由“BOX_LIMIT”指定。因此，在飞行之前，请确保你选择的 box_limit 足够小，以便它能够适应你的飞行区域。

注意：如果您使用 Flow Deck，此框的方向可能会出现变化。这是因为 Flow Deck 无法提供绝对航向估计，其仅基于陀螺仪测量。这会随着时间的推移而漂移，如果您在应用程序中加入多次转弯，漂移速度会加快。也有报告称，当 CrazyFlie 仍在地面时，这种情况会很快发生。使用 MoCap 或 Lighthouse Deck 时，这种情况不应该发生。

检查您的代码是否仍然与完整代码匹配并运行脚本！

.. code-block:: C

   import logging
   import sys
   import time
   from threading import Event

   import cflib.crtp
   from cflib.crazyflie import Crazyflie
   from cflib.crazyflie.log import LogConfig
   from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
   from cflib.positioning.motion_commander import MotionCommander
   from cflib.utils import uri_helper

   URI = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E7')

   DEFAULT_HEIGHT = 0.5
   BOX_LIMIT = 0.5

   deck_attached_event = Event()

   logging.basicConfig(level=logging.ERROR)

   position_estimate = [0, 0]


   def move_box_limit(scf):
      with MotionCommander(scf, default_height=DEFAULT_HEIGHT) as mc:
         body_x_cmd = 0.2
         body_y_cmd = 0.1
         max_vel = 0.2

         while (1):
               #if position_estimate[0] > BOX_LIMIT:
               #    mc.start_back()
               #elif position_estimate[0] < -BOX_LIMIT:
               #    mc.start_forward()

               if position_estimate[0] > BOX_LIMIT:
                  body_x_cmd = -max_vel
               elif position_estimate[0] < -BOX_LIMIT:
                  body_x_cmd = max_vel
               if position_estimate[1] > BOX_LIMIT:
                  body_y_cmd = -max_vel
               elif position_estimate[1] < -BOX_LIMIT:
                  body_y_cmd = max_vel

               mc.start_linear_motion(body_x_cmd, body_y_cmd, 0)

               time.sleep(0.1)


   def move_linear_simple(scf):
      ...

   def take_off_simple(scf):
      ...

   def log_pos_callback(timestamp, data, logconf):
      print(data)
      global position_estimate
      position_estimate[0] = data['stateEstimate.x']
      position_estimate[1] = data['stateEstimate.y']


   def param_deck_flow(_, value_str):
      value = int(value_str)
      print(value)
      if value:
         deck_attached_event.set()
         print('Deck is attached!')
      else:
         print('Deck is NOT attached!')


   if __name__ == '__main__':
      cflib.crtp.init_drivers()

      with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:

         scf.cf.param.add_update_callback(group='deck', name='bcFlow2',
                                          cb=param_deck_flow)
         time.sleep(1)

         logconf = LogConfig(name='Position', period_in_ms=10)
         logconf.add_variable('stateEstimate.x', 'float')
         logconf.add_variable('stateEstimate.y', 'float')
         scf.cf.log.add_config(logconf)
         logconf.data_received_cb.add_callback(log_pos_callback)

         if not deck_attached_event.wait(timeout=5):
               print('No flow deck detected!')
               sys.exit(1)

         # Arm the Crazyflie
         scf.cf.platform.send_arming_request(True)
         time.sleep(1.0)

         logconf.start()
         move_box_limit(scf)
         logconf.stop()



motion_commander_demo.py
--------------------------

   您可以向 Crazyflie 发送速度命令，并根据日志和参数变量做出反应，距离使用 Crazyflie Python 库编写自己的应用程序又近了一步！如果您想了解指挥官的具体功能，请查看 cflib 示例文件夹中的motion_commander_demo.py文件。

参考：

   https://github.com/bitcraze/crazyflie-lib-python/blob/95d912657b22e2869b84bc512af624de9940474b/examples/autonomy/motion_commander_demo.py

.. code-block:: C

   # -*- coding: utf-8 -*-
   #
   #     ||          ____  _ __
   #  +------+      / __ )(_) /_______________ _____  ___
   #  | 0xBC |     / __  / / __/ ___/ ___/ __ `/_  / / _ \
   #  +------+    / /_/ / / /_/ /__/ /  / /_/ / / /_/  __/
   #   ||  ||    /_____/_/\__/\___/_/   \__,_/ /___/\___/
   #
   #  Copyright (C) 2017 Bitcraze AB
   #
   #  Crazyflie Nano Quadcopter Client
   #
   #  This program is free software; you can redistribute it and/or
   #  modify it under the terms of the GNU General Public License
   #  as published by the Free Software Foundation; either version 2
   #  of the License, or (at your option) any later version.
   #
   #  This program is distributed in the hope that it will be useful,
   #  but WITHOUT ANY WARRANTY; without even the implied warranty of
   #  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   #  GNU General Public License for more details.
   # You should have received a copy of the GNU General Public License
   # along with this program. If not, see <https://www.gnu.org/licenses/>.
   """
   This script shows the basic use of the MotionCommander class.

   Simple example that connects to the crazyflie at `URI` and runs a
   sequence. This script requires some kind of location system, it has been
   tested with (and designed for) the flow deck.

   The MotionCommander uses velocity setpoints.

   Change the URI variable to your Crazyflie configuration.
   """
   import logging
   import time

   import cflib.crtp
   from cflib.crazyflie import Crazyflie
   from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
   from cflib.positioning.motion_commander import MotionCommander
   from cflib.utils import uri_helper

   URI = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E7')

   # Only output errors from the logging framework
   logging.basicConfig(level=logging.ERROR)


   if __name__ == '__main__':
      # Initialize the low-level drivers
      cflib.crtp.init_drivers()

      with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:
         # Arm the Crazyflie
         scf.cf.platform.send_arming_request(True)
         time.sleep(1.0)

         # We take off when the commander is created
         with MotionCommander(scf) as mc:
               time.sleep(1)

               # There is a set of functions that move a specific distance
               # We can move in all directions
               mc.forward(0.8)
               mc.back(0.8)
               time.sleep(1)

               mc.up(0.5)
               mc.down(0.5)
               time.sleep(1)

               # We can also set the velocity
               mc.right(0.5, velocity=0.8)
               time.sleep(1)
               mc.left(0.5, velocity=0.4)
               time.sleep(1)

               # We can do circles or parts of circles
               mc.circle_right(0.5, velocity=0.5, angle_degrees=180)

               # Or turn
               mc.turn_left(90)
               time.sleep(1)

               # We can move along a line in 3D space
               mc.move_distance(-1, 0.0, 0.5, velocity=0.6)
               time.sleep(1)

               # There is also a set of functions that start a motion. The
               # Crazyflie will keep on going until it gets a new command.

               mc.start_left(velocity=0.5)
               # The motion is started and we can do other stuff, printing for
               # instance
               for _ in range(5):
                  print('Doing other work')
                  time.sleep(0.2)

               # And we can stop
               mc.stop()

               # We land when the MotionCommander goes out of scope
