Crazyradio PA
===============

.. contents:: 目录
    :depth: 2
    :local:

Crazyradio PA 是一款基于 Nordic Semiconductor 的 nRF24LU1+ 的长距离开放式 USB 无线电适配器。它具有 20dBm 功率放大器、LNA，并预编程了与 Crazyflie 兼容的固件。功率放大器可扩大范围，与 Crazyflie 2.x 一起使用时，范围可达 1 公里（理想条件下），Crazyradio PA 到 Crazyradio PA 之间的范围可达 2 公里（理想条件下）。

由于它是一个开放项目，固件是从头编写的，并有一个 Python API 来控制它，因此对于需要比 WiFi 更长距离且对带宽没有相同要求的系统来说，它是一个很好的构建块。该硬件附带最新的固件以及一个引导加载程序，可通过 USB 升级固件，而无需任何额外的硬件。Crazyflie PA 与第一代 Crazyflie 兼容，但不会像 Crazyflie 2.x 那样增加范围。

.. figure:: ../../../_static/images/crazyradio-pa/Radio-PA-585px.JPG
   :align: center
   :alt: crazyradio-pa

特征
----
- 无线电功率放大器提供 20dBm 输出功率
- > Crazyflie 2.X 的视线范围为 1 公里
- 2x5 2.54mm 原型接头（未安装）
- PPM 的硬件支持
- 与第一代 Crazyradio 具有相同的机械尺寸
- 开源固件
- 通过 USB 升级固件
- 低延迟

机械规格
--------
- 重量：6克
-  尺寸（宽x高x深）：58x16x6.5mm（包括连接器）

电气规格
--------
- 基于 Nordic Semiconductor 的 nRF24LU1+ 芯片
    - 8051 MCU，最高频率为 16MHz，配备 16Kb 或 32Kb 闪存和 2Kb SRAM
    - 2.4GHz ISM 频段无线电
    - USB 设备外围设备
    - 125 个广播频道
    - 2Mbps、1Mbps 和 250Kps 通信数据速率
    - 发送和接收最多 32 字节有效载荷的数据包
    - 自动处理地址和数据包确认
    - 硬件 SPI 和 UART
    - 与 Nordic Semiconductor 的增强型 ShockBurst 协议兼容

- 可通过扩展接头供电高达 13V
- 2x5 2.54mm 扩展接头，带有以下信号（未安装）：
    - PPM 输入
    - 高达 13V 的输入电源
    - GND
    - SPI/UART
- 标准 USB-A 连接器

无线电规格
----------
- 20dBm输出功率（100mW）
- 低噪声放大器 (LNA)
- RP-SMA 连接器

Crazyradio PA 拓展用途(无线鼠标漏洞)
-------------------------------------

想象一下，无人机从窗外飞过，几秒钟内你的电脑就被黑客攻破！本视频展示了如何利用无人机和无线鼠标的漏洞（MouseJack）进行攻击，黑客可以在几秒内入侵你的电脑系统，远程控制文件、破坏数据。你是否也可能成为攻击的目标？揭秘现代无线设备背后的隐患，确保你的设备安全！

.. raw:: html

   <div style="text-align: center">
      <video width="100%" height="auto" controls autoplay muted loop>
         <source src="../../../_static/videos/crazyradio/crazyradioPA_hack.mp4" type="video/mp4">
         Your browser does not support the video tag.
      </video>
   </div>

视频出自 https://www.bilibili.com/video/BV1DdwTevEfC/?spm_id_from=333.337.top_right_bar_window_custom_collection.content.click&vd_source=043cb97b7bfecc6a495d2cdd5a873975

资料下载
--------

- `数据手册 <../../../_static/products/crazyradio-pa/datasheet/crazyradio_pa-datasheet.pdf>`_