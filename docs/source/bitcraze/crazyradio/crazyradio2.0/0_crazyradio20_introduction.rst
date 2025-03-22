Crazyradio 2.0
===============

.. contents:: 目录
    :depth: 2
    :local:

Crazyradio 2.0 是一款基于 Nordic Semiconductor 的 nRF52840 的长距离开放式 USB 无线电适配器，具有 20dBm 功率放大器和 LNA。

Crazyradio 2.0 不仅可与 Crazyflie 系列设备一起使用，因为它是一个开放项目，具有开放固件和 Python API，因此对于需要比 WiFi 更可预测的延迟且对带宽要求不同的系统来说，它是一个很好的构建块。该硬件附带一个引导加载程序，可通过 USB 升级固件，而无需任何额外的硬件。

Crazyradio 2.0 与 Crazyflie 生态系统兼容。

根据安装的固件，Crazyradio 2.0 可以以两种不同的模式运行：

- Crazyradio PA 仿真 - 其行为类似于Crazyradio PA。这是最初可用的固件。
- Crazyradio 2.0 - 一套新的协议和功能，将改善生态系统中的通信。这项工作正在进行中，并将随着时间的推移而发展。

.. figure:: ../../../_static/images/crazyradio2-0/CR2.0-dongle-585px.jpg
   :align: center
   :alt: crazyradio2-0

特征
----
- 无线电功率放大器提供 20dBm 输出功率
- 通过 USB 升级固件
- 开源固件
- 低延迟

机械规格
--------
- 重量：7克
- 尺寸（宽x高x深）：63x18x8mm（包括连接器）

电气规格
--------
- 基于 Nordic Semiconductor 的 nRF52840 芯片
    - 64MHz Cortex-M4F 处理器，配备 1MB 闪存和 256Kb RAM
    - 2.4GHz ISM 频段无线电
    - USB 设备外围设备
    - 100 个广播频道
    - 1 Mbps、2Mbps 和长距离（125kbps 和 500kbps 模式）蓝牙® 低功耗模式
    - 250kbps IEEE 802.15.4模式
    - 1Mbps 和 2Mbps Nordic专有模式

- 可通过焊盘提供额外信号，实现定制扩展
    - 3 个输入/输出
    - GND
    - 3.15V输出
    - 5V输入
- 标准 USB-A 连接器
- 编程连接器

无线电规格
----------
- 20dBm输出功率（100mW）
- 低噪声放大器 (LNA)
- RP-SMA 连接器

资料下载
--------

- `数据手册 <../../../_static/products/crazyradio-2-0/datasheet/crazyradio_2_0-datasheet.pdf>`_