ROS2与Lighthouse定位系统-更新固件
============================
说明
--------------------------------

介绍如何刷新固件
固件github地址
Crazyflie无人机集群套件，采购地址
更新固件
点击下载固件地址，选择cf2版本（cf2是Crazyflie 2.X），选择zip文件，其中包含Crazyflie 2.0的nRF51和STM32F405的固件。

进入BOOTLOADER模式

确保Crazyflie与客户端断开连接并关闭电源
菜单connect-> Bootloader
对于Crazyflie 2.0，将其打开时按住按钮约3秒钟，直到蓝色LED M2开始闪烁以进入引导加载程序模式。如果刷错固件，必须从未通电状态开始。然后按住按钮并接通电源。
点击Initiate bootloader cold boot
刷新固件

点击选择按钮，在电脑上找到下载的zip固件包。
点击program
点击Restart in firmware mode
连接crazyflie后，在Tabs->Console中查看固件版本