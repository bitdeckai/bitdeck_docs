Crazyswarm 简介
===============

Crazyswarm 是一个功能强大的多无人机编队控制系统，最初由南加州大学 (USC) 和加州理工学院 (Caltech) 开发，专为控制大量 Crazyflie 微型无人机而设计，广泛应用于研究、教学和演示领域。

主要功能
--------

- **多无人机控制**：支持同时控制几十架 Crazyflie 无人机。
- **精确定位**：配合 Vicon、OptiTrack 等定位系统，实现厘米级精度。
- **轨迹规划与控制**：支持离线轨迹导入与实时控制，适用于复杂编队飞行。
- **基于 ROS 架构**：便于集成其他机器人系统与算法模块。
- **多语言接口**：支持 Python 与 C++ 接口进行开发和实验。

系统组成
--------

1. **Crazyflie 无人机**：由 Bitcraze 开发的微型飞行平台。
2. **定位系统**：如 Vicon、OptiTrack 或 Crazyflie 的 LPS 系统。
3. **Crazyswarm 软件栈**：
   
   - `crazyswarm` ROS 节点：统一管理飞行任务（起飞、降落、轨迹跟踪）。
   - 定制版 `crazyflie-firmware`：支持高频率控制输入。
   - `crazyflie_ros`：与 Crazyflie 通信的 ROS 驱动层。
4. **地面工作站**：运行 ROS 的计算机，用于任务发布和数据处理。

常见应用
--------

- 多机飞行编队演示
- 分布式协同控制算法研究
- 教学平台（控制、定位、飞行原理）
- 室内 SLAM、轨迹跟踪与路径规划实验

开源地址
--------

GitHub 仓库：  
`https://github.com/USC-ACTLab/crazyswarm`

.. toctree::
   :maxdepth: 2
   :caption: Crazyswarm

