Matrix Ranger deck 固件接入（代码修改指南）
=============================================

.. contents:: 目录
   :depth: 3
   :local:

简介
----

基础代码crazyflie-firmware的tag 2024.10.2上增加对Matrix Ranger deck的支持

https://github.com/bitcraze/crazyflie-firmware/tree/2024.10.2

本文档基于 ``crazyflie-firmware-2024.10.2_matrix_ranger_deck.zip`` 中的变更报告
``docs/git-diff-change-report-2026-07-10.md``，说明如何在标准 Crazyflie 固件上手动接入
Matrix Ranger deck 代码。

接入目标
--------

- 将默认构建目标切换到 ``examples/app_matrix_ranger``。
- 在 ``multiranger.c`` 中启用 Matrix Ranger 传感器路径。
- 保留可回退能力（通过宏开关切换）。

需要新增的目录与文件
--------------------

请先把以下目录/文件复制到固件仓库对应位置：

- ``examples/app_matrix_ranger``
- ``examples/app_matrix_ranger/src/test_tof.c``
- ``examples/app_matrix_ranger/src/tof_driver/ToF_process.c``
- ``examples/app_matrix_ranger/src/tof_driver/ToFplatform.c``
- ``examples/app_matrix_ranger/src/tof_driver/vl53l5cx_api.c``
- ``examples/app_matrix_ranger/src/tof_driver/vl53l5cx_buffers.h``

步骤 1：修改 Makefile
---------------------

在仓库根目录的 ``Makefile`` 中进行以下改动。

1) 放宽 ``restrict`` 警告为非错误：

.. code-block:: diff

  - ARCH_CFLAGS += -Wno-stringop-overflow
  + ARCH_CFLAGS += -Wno-stringop-overflow -Wno-error=restrict

2) 增加 ToF 驱动头文件搜索路径：

.. code-block:: diff

  + INCLUDES += -I$(srctree)/examples/app_matrix_ranger/src/tof_driver

3) 切换默认构建目标到 Matrix Ranger App：

.. code-block:: diff

  - objs-y += app_api
  + # objs-y += app_api
  + objs-y += examples/app_matrix_ranger

步骤 2：修改 multiranger.c
---------------------------

编辑 ``src/deck/drivers/src/multiranger.c``，加入宏开关：

.. code-block:: c

  #define MATRIX_RANGER_ENABLE 1

然后将 front/back 相关逻辑做条件编译保护。

1) front/back 设备实例：

.. code-block:: c

  #if MATRIX_RANGER_ENABLE
  #else
  NO_DMA_CCM_SAFE_ZERO_INIT static VL53L1_Dev_t devFront;
  NO_DMA_CCM_SAFE_ZERO_INIT static VL53L1_Dev_t devBack;
  #endif

2) 任务启动阶段，跳过 front/back 重启：

.. code-block:: c

  #if MATRIX_RANGER_ENABLE
  #else
  status = VL53L1_StopMeasurement(&devFront);
  status = VL53L1_StartMeasurement(&devFront);
  status = VL53L1_StopMeasurement(&devBack);
  status = VL53L1_StartMeasurement(&devBack);
  #endif

3) 测距循环阶段，跳过 front/back 上报：

.. code-block:: c

  #if MATRIX_RANGER_ENABLE
  #else
  rangeSet(rangeFront, mrGetMeasurementAndRestart(&devFront) / 1000.0f);
  rangeSet(rangeBack, mrGetMeasurementAndRestart(&devBack) / 1000.0f);
  #endif

4) PCA95 输出脚位配置只保留 up/right/left：

.. code-block:: c

  #if MATRIX_RANGER_ENABLE
  pca95x4ConfigOutput(PCA95X4_DEFAULT_ADDRESS,
                ~(MR_PIN_UP |
                 MR_PIN_RIGHT |
                 MR_PIN_LEFT));

  pca95x4ClearOutput(PCA95X4_DEFAULT_ADDRESS,
               MR_PIN_UP |
               MR_PIN_RIGHT |
               MR_PIN_LEFT);
  #else
  /* 保留原先包含 FRONT/BACK 的配置 */
  #endif

5) 自检阶段，跳过 front/back 初始化：

.. code-block:: c

  #if MATRIX_RANGER_ENABLE
  #else
  isPassed &= mrInitSensor(&devFront, MR_PIN_FRONT, "front");
  isPassed &= mrInitSensor(&devBack, MR_PIN_BACK, "back");
  #endif

步骤 3：编译与烧录
----------------------

在 Crazyflie firmware 仓库执行：

.. code-block:: bash

  make clean
  make -j
  make cload

验证建议
--------

- 启动后确认 up/right/left 三个方向测距正常更新。
- 确认 front/back 不再参与初始化和测距流程（符合 Matrix Ranger 接入预期）。
- 如需恢复标准 multiranger 行为，将 ``MATRIX_RANGER_ENABLE`` 改为 ``0``。

注意事项
--------

- ``vendor/unity`` 子模块在报告中出现 ``-dirty`` 指针变化，此项不是 Matrix Ranger 核心功能改动。
  若不涉及单元测试更新，建议保持主线子模块版本不变。
- 报告中还有脚本权限位变化（``100755 -> 100644``），不影响功能逻辑，可忽略。

