Flow2 deck
===============

.. contents:: 目录
    :depth: 2
    :local:

简介
--------

Flow deck v2 使 Crazyflie 2.x 能够感知其在任何方向上的移动。VL53L1x ToF 传感器可高精度测量与地面的距离，而 PMW3901 光流传感器则可测量相对于地面的运动。这创造了一个可飞行的 3D 机器人，它可以通过预先编程实现在任何方向上的飞行距离，或者作为初学者的辅助工具，创建一个非常稳定的飞行平台。

特征
----

- 快速、准确的测距
- 测量绝对范围高达 4 米
- 人眼安全
- 测量水平运动
- 创建可预编程的 3D 机器人
- 辅助飞行

机械规格
--------

- 重量：1.6 克
- 尺寸（宽x高x深）：21x28x4 mm
- 设计用于安装在 Crazyflie 2.X 下方

电气规格
--------

- VL53L1x ToF 传感器可测量最远 4 米的距离，精度为几毫米（取决于表面和光线条件）
- 用于自动扩展卡检测的单线存储器
- PMW3901 光流传感器（在无光泽表面上效果最佳）

使用限制
--------

.. raw:: html

   <div style="text-align: center">
      <video width="100%" height="auto" controls autoplay muted loop>
         <source src="../../../_static/videos/flow_deck_v2/Crazyflie Flow deck flying limitations..mp4" type="video/mp4">
         Your browser does not support the video tag.
      </video>
   </div>

PMW3901 是一款基于光流（Optical Flow）原理的运动检测传感器，广泛用于无人机、机器人等领域来进行二维位置追踪和速度估计。以下是它适用和不适用的典型场景：

适合的使用场景
^^^^^^^^^^^^^^

- **有纹理的非反光表面**
  
  如木地板、地毯、水泥地等有细节纹理的表面，光流算法能准确跟踪像素变化。

- **良好的光照条件**
  
  室内明亮环境或室外光线均匀的场景，有助于稳定获取图像数据。

- **小型飞行器或机器人近地飞行/移动**
  
  常用于如 Crazyflie、Tello 等微型无人机，用于水平速度估计和位置保持。

- **无需高精度绝对定位的场合**
  
  适用于需要相对位置追踪和速度检测的任务，如悬停、匀速前进等。

不适合的使用场景
^^^^^^^^^^^^^^^^

- **无纹理或单色表面**
  
  如纯白墙面、玻璃或光滑桌面，缺乏图像特征，容易导致跟踪失败。

- **强反光或透明表面**
  
  比如玻璃、水面、抛光金属，反射会干扰图像采集，导致输出不稳定。

- **光照极差或频繁变化的环境**
  
  过暗或光线频闪的环境将严重影响图像帧间差异分析，可能导致错误数据。

- **大幅垂直运动**
  
  由于其只追踪二维光流，剧烈的高度变化会引起误判或信号丢失。

资料下载
--------

- `数据手册 <../../../_static/products/flow-deck-2/datasheet/flow_deck_2-datasheet.pdf>`_

- `原理图 <../../../_static/products/flow-deck-2/electronics/flow-deck-v2-reva.pdf>`_

使用手册
----------------

.. toctree::
   :maxdepth: 2
   :caption: Loco User Manual

   1_flow2_deck_assembly
   2_flow2_deck_getting_started
   3_flow2_deck_STEM_bundle