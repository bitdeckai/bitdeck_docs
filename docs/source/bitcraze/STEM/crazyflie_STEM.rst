Crazyflie STEM
==============================

.. contents:: 目录
    :depth: 2
    :local:

STEM（科学、技术、工程、数学）理念强调通过可视化、可编程和可实验的方式来学习无人机基础知识。Crazyflie STEM 套件以 Crazyflie 2.x 平台为核心，结合 Flow deck、扩展板和 Python 控制流程，适合教学、原型验证、算法开发和飞行演示等场景。

本页面主要介绍 Crazyflie STEM 平台的基本概念、坐标系、软件准备和固件升级方法，帮助用户快速完成环境配置和首次上手。

概述
----

Crazyflie 是一款轻型、开源、可扩展的四旋翼飞行平台，适合用于教育和研究场景。结合 Flow deck V2、Multi-ranger deck、Crazyradio 和 Python 客户端之后，可以实现稳定悬停、运动控制、路径规划以及环境感知与避障实验。

STEM 套件的核心价值在于：

- 通过低门槛硬件快速搭建飞行平台
- 使用 Python / cflib 进行控制脚本开发
- 结合可视化逻辑进行教学演示和算法验证
- 支持从入门学习到高级实验的逐步扩展
- 通过 Multi-ranger deck 扩展周围环境感知能力

硬件组成
--------

- 1 x Crazyflie 2.1
- 1 x Flow deck V2
- 1 x Multi-ranger deck
- 1 x Crazyradio 2.0 或 Crazyradio PA
- 1 x USB 连接线
- 计算机与 Python 3 环境
- cflib 控制库及飞行脚本

Multi-ranger deck 作为扩展模块，可用于测量前后左右及上方的障碍距离，为无人机避障、定位和环境感知实验提供基础能力。
参考资料
--------

- `Crazyflie 官方文档 <https://www.bitcraze.io/>`_
- `Bitcraze GitHub <https://github.com/bitcraze>`_
- `cfloader 文档 <https://wiki.bitcraze.io/doc:crazyflie:client:cfloader:index>`_
- `Flow deck v2 介绍 <../deck/flow2_deck/0_flow2_deck_introduction.html>`_
- `Flow deck v2 STEM 套件 <../deck/flow2_deck/3_flow2_deck_STEM_bundle.html>`_
- `Multi-ranger deck 介绍 <../deck/Multi-ranger_deck/0_multi-ranger_deck_introduction.html>`_
- `Multi-ranger deck STEM 套件 <../deck/Multi-ranger_deck/3_multi-ranger_deck_STEM_bundle.html>`_

Crazyflie2.1/Bolt/Brushless 目录
---------------------------------

.. toctree::
   :maxdepth: 6
   :caption: Crazyflie

   aily_blockly_STEM/1_aily_blockly_flow2_deck_STEM_bundle


