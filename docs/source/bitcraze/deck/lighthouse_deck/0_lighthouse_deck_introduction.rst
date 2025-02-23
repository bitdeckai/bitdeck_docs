Lighthouse Deck
===============

The lighthouse positioning system is an optically-based positioning system that allows an object to locate itself with high precision indoors. The system allows to get a precision of tracking approaching what can be achieved with a Motion Capture system, but for a much lower cost and with the advantage that the position is acquired onboard the tracked device rather than in the infrastructure. For a flying robot like the Crazyflie, this means that the position information is directly available for autonomous flight without requiring low latency reliable transport of the position over radio.

灯塔定位系统是一种基于光学的定位系统，可以让物体在室内实现高精度自主定位。该系统能够实现接近动作捕捉系统的跟踪精度，但成本要低得多，而且具有一个重要优势：位置信息是在被跟踪设备上直接获取的，而不是在基础设施中获取。对于像 Crazyflie 这样的飞行机器人来说，这意味着位置信息可以直接用于自主飞行，无需通过无线电传输来获取低延迟的可靠位置数据。

.. figure:: ../../../images/deck/lighthouse_deck.png
   :align: center
   :alt: lighthouse 定位系统
   :figclass: align-center


Lighthouse 基站
----------------

该系统使用 SteamVR 基站作为光学信标，使 Crazyflie 能够计算其位置，精度优于分米级，可达到毫米级精度。

基站由旋转的光鼓组成，在房间内发射激光。Crazyflie 或任何需要定位的物体都有一个光接收器（光电二极管），用于接收旋转的激光，然后能够测量基站和接收器之间的角度。通过使用多个接收器，可以计算出物体相对于基站的位置和方向。如果我们知道基站的位置和方向，就最终可以确定 Crazyflie 的位置和方向。

V1 和 V2

灯塔定位系统使用灯塔基站作为信标。基站有两代产品，都受支持：V1 和 V2。

灯塔 V1 使用两个旋转光鼓，而灯塔 V2 只使用一个，但在同一个光鼓上有两个倾斜的光平面。灯塔 V1 系统最多可以使用 2 个基站，而灯塔 V2 系统设计上最多可支持 16 个基站。Crazyflie 固件目前标准支持最多 4 个基站，通过手动配置固件可以启用更多基站。

+------------------+------------------+------------------+--------------------------------------------------------+
| 特性             | 灯塔 V1          | 灯塔 V2          | 备注                                                   |
+==================+==================+==================+========================================================+
| 范围             | ~6米             | 6米              | V1范围取决于环境。V2设计范围为6米                      |
+------------------+------------------+------------------+--------------------------------------------------------+
| 定位频率         | 30Hz (2个基站)    | ~50Hz            | V2频率与基站数量无关                                   |
+------------------+------------------+------------------+--------------------------------------------------------+
| 基站数量         | 1 - 2            | 1 - 4            | V2硬件最多支持16个，可在Crazyflie固件中配置            |
+------------------+------------------+------------------+--------------------------------------------------------+
| 水平视角         | 120°             | 150°             |                                                        |
+------------------+------------------+------------------+--------------------------------------------------------+
| 垂直视角         | 120°             | 110°             |                                                        |
+------------------+------------------+------------------+--------------------------------------------------------+


系统几何结构
----------------