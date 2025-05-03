Template for the Read the Docs tutorial
=======================================

This GitHub template includes fictional Python library
with some basic Sphinx docs.

Read the tutorial here:

https://docs.readthedocs.io/en/stable/tutorial/


html文件
---------

    .\docs\make.bat html

    查看index.html文件, 效果是否可以

    ./docs/build/html/index.html

git推送问题
------------

### 检查GitHub的ping的通否

测试是否能访问目标仓库域名（如 github.com）

    ping github.com

测试特定端口是否开放（HTTP/HTTPS 默认 80/443，SSH 默认 22）

    curl -vI https://github.com  # 检查 HTTPS 连通性
    nc -zv github.com 443        # 检查端口连通性

- 若超时或无响应
- 检查防火墙、VPN 或路由器设置。
- 尝试切换网络（如手机热点）。

如果ping不通，修改C:\Windows\System32\drivers\etc下的hosts文件，添加如下两行：

140.82.114.4 github.com

151.101.1.194 github.global.ssl.fastly.net

前面的ip地址去https://www.ipaddress.com/查看

然后就可以ping的通

如果git push执行之后已经可以上传下载，下面就不用执行了

配置git环境
------------

在git bash下输入如下两个命令就可以了。

git config --global http.proxy http://127.0.0.1:1080

git config --global https.proxy http://127.0.0.1:1080

构建GitHub密钥
---------------

C:\Users\sb\.ssh下面生成id_rsa.pub，复制到GitHub中

这一步的意义是让你当前使用的设备可以免密访问你的GitHub账号

push和pull的时候使用SSH连接即可
-------------------------------

git push git@github.com:xxx/git-demo.git master

然后输入yes回车，即上传成功
