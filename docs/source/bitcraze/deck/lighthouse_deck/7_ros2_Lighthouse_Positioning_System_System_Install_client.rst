ROS2与Lighthouse定位系统-客户端安装
============================
说明
--------------------------------
    cfclient是crazyflie的客户端，主要用来控制Crazyflie、刷新固件、设置参数和记录日志
    通过cfclient客户端的固件会同时烧录无人机的固件，lighthouse甲板固件，NRF固件
    Crazyflie无人机集群套件 `采购地址 <https://item.taobao.com/item.htm?ft=t&id=858112103307&spm=a21dvs.23580594.0.0.52de2c1bg17fUu>`_
安装cfclient
--------------------------------
    
安装依赖
^^^^^^^^^^^^^^

.. code-block:: bash
   sudo apt-get install python3 python3-pip python3-pyqt5 qt5-default pyqt5-dev pyqt5-dev-tools
    
下载源码
^^^^^^^^^^^^^^

.. code-block:: bash

   git clone https://github.com/bitcraze/crazyflie-clients-python.git
    
    
安装cfclient
^^^^^^^^^^^^^^

.. code-block:: bash

    cd  crazyflie-clients-python
    pip3 install -e .
    
运行客户端cfclient
^^^^^^^^^^^^^^

.. code-block:: bash

    cfclient

CrazyRadio(PA)设置udev权限
^^^^^^^^^^^^^^

.. code-block:: bash

    sudo groupadd plugdev
    sudo usermod -a -G plugdev $USER  

建一个名为的文件/etc/udev/rules.d/99-crazyradio.rules并添加以下内容：
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: bash

    sudo vim /etc/udev/rules.d/99-crazyradio.rules
   
    #在文件中添加如下内容
    # Crazyradio (normal operation)
    SUBSYSTEM=="usb", ATTRS{idVendor}=="1915", ATTRS{idProduct}=="7777", MODE="0664", GROUP="plugdev"
    # Bootloader
    SUBSYSTEM=="usb", ATTRS{idVendor}=="1915", ATTRS{idProduct}=="0101", MODE="0664", GROUP="plugdev"
 
要通过USB连接Crazyflie 2.0，请创建文件名/etc/udev/rules.d/99-crazyflie.rules并添加以下内容：
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: bash

   sudo vim /etc/udev/rules.d/99-crazyflie.rules
   #文件中添加如下内容
   SUBSYSTEM=="usb", ATTRS{idVendor}=="0483", ATTRS{idProduct}=="5740", MODE="0664", GROUP="plugdev"
    
重新加载udev-rules
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: bash

    sudo udevadm control --reload-rules
    sudo udevadm trigger

参考：
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

    https://github.com/bitcraze/crazyflie-clients-python/tree/develop
    https://github.com/bitcraze/crazyflie-lib-python#setting-udev-permissions
