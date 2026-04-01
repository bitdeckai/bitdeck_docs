Lighthouse位置与姿态获取
==============================

在 ``crazyflie-lib-python`` 的 Lighthouse 示例中，常见的两个入门脚本分别是：

- ``lighthouse_simple_position.py``: 只读取 Crazyflie 的三维位置。
- ``lighthouse_simple_position_attitude.py``: 同时读取三维位置和姿态角。

这两个示例都适合用来验证 Lighthouse 定位链路是否正常，以及确认飞行器当前的状态估计是否稳定。

示例定位
-------------------------

两个脚本的核心区别很直接：

``lighthouse_simple_position.py``
   只关注位置数据，输出 ``X``、``Y``、``Z`` 三个方向的位置估计。

``lighthouse_simple_position_attitude.py``
   在位置数据基础上，额外输出 ``Roll``、``Pitch``、``Yaw``，适合在调试姿态估计或联动上位机显示时使用。

如果当前目标只是确认无人机有没有被 Lighthouse 正常追踪，优先使用 ``lighthouse_simple_position.py`` 即可。
如果还要进一步确认机体朝向、姿态变化是否合理，再使用 ``lighthouse_simple_position_attitude.py``。

主要流程
-------------------------

这两个示例的整体工作流基本一致：

1. 初始化 ``cflib.crtp`` 驱动。
2. 通过 ``SyncCrazyflie`` 建立与 Crazyflie 的同步连接。
3. 调用 ``reset_estimator()`` 重置状态估计器。
4. 使用 ``LogConfig`` 配置日志变量和采样周期。
5. 注册日志回调函数，持续打印当前状态。
6. 在限定时间内接收数据，结束后自动停止日志并断开连接。

从文档角度理解，这两个示例本质上都是“日志订阅”示例，而不是“轨迹控制”示例。它们的重点是从飞控内部变量中读取状态估计结果。

示例下载
-------------------------

可以直接下载对应示例文件：

- :download:`lighthouse_simple_position.py <../../_static/develop/crazyflie-lib-python/lighthouse_simple_position.py>`
- :download:`lighthouse_simple_position_attitude.py <../../_static/develop/crazyflie-lib-python/lighthouse_simple_position_attitude.py>`
- :download:`crazyflie-lib-python-master.rar <../../_static/develop/crazyflie-lib-python/crazyflie-lib-python-master.rar>`

如果只想快速验证 Lighthouse 定位，下载 ``lighthouse_simple_position.py`` 即可。
如果需要同时观察位置和姿态，下载 ``lighthouse_simple_position_attitude.py``。
如果希望保留完整示例环境，可以直接下载压缩包。

如何执行代码
-------------------------

这两个脚本都是标准 Python 脚本，执行方式非常直接。

源代码仓库：

- https://github.com/bitcraze/crazyflie-lib-python

在开始之前，建议先完成以下准备：

- Crazyradio PA/Crazyradio 2.0已连接到电脑。
- Crazyflie 已上电。
- Lighthouse 基站已经正常工作。
- Crazyflie 已进入 Lighthouse 可追踪范围。
- 本地 Python 环境已经安装 ``cflib``。

如果还没有安装 ``cflib``，可以先执行：

.. code-block:: bash

   pip install cflib

如果你是单独下载 ``python`` 文件（而不是直接使用完整仓库），请把文件放到下面目录：

.. code-block:: text

   crazyflie-lib-python-master\examples\lighthouse

然后在仓库根目录终端执行：

.. code-block:: powershell

   python .\examples\lighthouse\lighthouse_simple_position.py
   python .\examples\lighthouse\lighthouse_simple_position_attitude.py

也可以分别执行：

.. code-block:: powershell

   python .\examples\lighthouse\lighthouse_simple_position.py

执行同时读取位置和姿态的脚本：

.. code-block:: powershell

   python .\examples\lighthouse\lighthouse_simple_position_attitude.py

这两个脚本默认连接下面这个 URI：

.. code-block:: text

   radio://0/80/2M/E7E7E7E7E7

如果你的 Crazyflie 使用的是其他无线地址，可以先设置环境变量，再执行脚本。

Windows PowerShell 示例：

.. code-block:: powershell

   $env:CFLIB_URI="radio://0/80/2M/E7E7E7E7E8"
   python lighthouse_simple_position.py

或者：

.. code-block:: powershell

   $env:CFLIB_URI="radio://0/80/2M/E7E7E7E7E8"
   python lighthouse_simple_position_attitude.py

执行后会发生什么
-------------------------

程序启动后，主要会按下面顺序工作：

1. 初始化底层无线驱动。
2. 连接到指定 URI 的 Crazyflie。
3. 调用 ``reset_estimator(scf)`` 重置状态估计器。
4. 启动日志订阅。
5. 以 100 ms 周期持续打印数据。
6. 持续约 30 秒后停止，并打印结束信息。

如果连接正常，终端里首先会看到连接提示。

只读取位置的脚本，开始时通常会打印：

.. code-block:: text

   Connecting to Crazyflie at radio://0/80/2M/E7E7E7E7E7...
   Logging position data for 30 seconds...

位置与姿态脚本，开始时通常会打印：

.. code-block:: text

   Connecting to Crazyflie at radio://0/80/2M/E7E7E7E7E7...
   Logging position and attitude data for 30 seconds...

打印信息说明
-------------------------

读取的数据内容
-------------------------

``lighthouse_simple_position.py`` 通常读取以下变量：

- ``kalman.stateX``
- ``kalman.stateY``
- ``kalman.stateZ``

这三个变量表示卡尔曼状态估计器输出的位置，单位通常为米。

``lighthouse_simple_position_attitude.py`` 在此基础上，额外增加：

- ``stabilizer.roll``
- ``stabilizer.pitch``
- ``stabilizer.yaw``

这三个变量表示飞行器当前姿态角，通常用于判断机体是否水平、是否发生明显偏航，以及定位与姿态解算是否一致。

预期打印输出
-------------------------

``lighthouse_simple_position.py`` 的单行输出格式如下：

.. code-block:: text

   Position: X=0.123, Y=-0.045, Z=0.812

其中：

- ``X`` 表示前后或坐标系 X 方向位置。
- ``Y`` 表示左右或坐标系 Y 方向位置。
- ``Z`` 表示高度方向位置。

如果 Lighthouse 工作正常，你应该看到这些数值持续刷新，并随着无人机移动而变化。

``lighthouse_simple_position_attitude.py`` 的单行输出格式如下：

.. code-block:: text

   Position: X=0.123, Y=-0.045, Z=0.812 | Attitude: Roll=1.25, Pitch=-0.84, Yaw=92.43

其中：

- ``Position`` 部分表示当前位置。
- ``Roll`` 表示横滚角。
- ``Pitch`` 表示俯仰角。
- ``Yaw`` 表示偏航角。

程序结束时，两个脚本最后都会打印：

.. code-block:: text

   Done!

异常情况说明
-------------------------

如果执行后没有看到持续刷新的位置数据，通常优先检查以下问题：

- URI 是否正确。
- Crazyradio 是否被正常识别。
- Crazyflie 是否已经连接成功。
- Lighthouse 基站是否覆盖到当前飞行器位置。
- Lighthouse 标定结果是否可用。
- 飞控固件是否正确输出 ``kalman.stateX/Y/Z`` 和 ``stabilizer`` 相关变量。

如果终端只打印了连接信息，但位置数值明显不变化或大幅跳变，一般说明当前状态估计还没有稳定，或者 Lighthouse 追踪质量不足。

两者差异
-------------------------

.. list-table::
   :header-rows: 1
   :widths: 25 35 40

   * - 对比项
     - ``lighthouse_simple_position.py``
     - ``lighthouse_simple_position_attitude.py``
   * - 输出内容
     - 位置 ``X/Y/Z``
     - 位置 ``X/Y/Z`` + 姿态 ``Roll/Pitch/Yaw``
   * - 日志变量数量
     - 3 个
     - 6 个
   * - 适用场景
     - 验证定位是否正常
     - 同时验证定位和姿态估计
   * - 调试复杂度
     - 更低，输出更简洁
     - 更高，信息更完整

使用条件
-------------------------

在运行这两个示例之前，建议确认以下条件已经满足：

- Crazyflie 已经可以正常连接。
- 已安装并启用了 Lighthouse 相关硬件。
- Lighthouse 基站已经完成基本部署与标定。
- 飞行器处于基站可见范围内。
- 固件中的 Lighthouse 定位功能工作正常。
- 本地 Python 环境已经安装 ``cflib``。

如果缺少基站视野、标定不完整，或者定位数据尚未收敛，脚本虽然可能成功连接，但输出的位置和姿态会明显跳变，不能直接用于飞行控制判断。

关键点说明
-------------------------

``reset_estimator()``
   这是两个示例里非常关键的一步。重置后，EKF 会重新收敛，能够减少旧状态残留带来的影响。

``LogConfig``
   用于指定要读取哪些内部变量，以及数据更新周期。示例中通常使用较短周期，便于实时观察状态。

``position_callback``
   通过回调函数处理日志数据。位置脚本只打印坐标，位置与姿态脚本则会一起打印坐标和欧拉角。

``SyncCrazyflie``
   用于简化连接过程，适合示例、验证和脚本式开发。

建议使用方式
-------------------------

建议按下面顺序使用：

1. 先运行 ``lighthouse_simple_position.py``，确认位置数据连续、稳定、方向正常。
2. 再运行 ``lighthouse_simple_position_attitude.py``，观察姿态角是否与真实摆放姿态一致。
3. 如果位置正常但姿态异常，优先检查机体放置方向、固件姿态估计和传感器状态。
4. 如果位置与姿态都不稳定，优先回到 Lighthouse 基站部署、可见性和标定结果进行排查。

适用场景
-------------------------

这两个示例特别适合以下场景：

- 新搭建 Lighthouse 环境后的首次联调。
- 检查 Crazyflie 是否已经成功进入 Lighthouse 定位模式。
- 为后续轨迹控制、定点悬停、姿态联动显示做基础验证。
- 在上位机界面之外，通过 Python 脚本快速查看实时状态。

总结
-------------------------

``lighthouse_simple_position.py`` 更适合做最小化验证，快速判断 Lighthouse 定位是否可用。

``lighthouse_simple_position_attitude.py`` 则适合在定位验证完成后，继续检查姿态估计结果，帮助完成更完整的状态观测。

如果只是做链路检查，优先使用前者；如果要为自主飞行、闭环控制或可视化系统做准备，建议直接使用后者。

