# 网络传输

## IP 地址

IP 地址就是标识网络中设备的一个地址。

<img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiyp0SqzxyHCVGLjG_4N4ukenHTJg_oIHJ0_F4RCsbxIOTbPye8FQolTR23dhW--21M3j39tO5azNvJlEl24n23dRPjqwQWd9XPNJM93fjy4vg3aSH-Qoba9vFocMGzhVfzTOYG1sYdn3QconwLaNj6k3b5Ua2dKbLscdotRamSCsUb7JLSExicBz8F1g/s960/Slide5.JPG" style="zoom:67%;" />

### IP 地址的表现形式

<img src="https://www.scaleuptech.com/de/wp-content/uploads/2020/11/ipv4-vs-ipv6.png" style="zoom: 90%;" />

IP 地址分为两类： IPv4 和 IPv6

* IPv4 是目前使用的 ip 地址。
* 未来 ip 地址将迁移到 IPv6。

IP 地址的作用是标识网络中唯一的一台设备的，也就是说通过IP地址能够找到网络中某台设备。

### 查看 IP 地址

* Linux 和 mac OS 使用 `ifconfig` 这个命令
* Windows 使用 `ipconfig` 这个命令

查询结果

- inet 和 inet6 是设备在网络中的IP地址
- 127.0.0.1表示本机地址，提示：如果和自己的电脑通信就可以使用该地址。
- 127.0.0.1该地址对应的域名是 localhost**，**域名是 ip 地址的别名，通过域名能解析出一个对应的ip地址。

### 检查网络

* 检查网络是否正常使用 ping 命令

实验命令

* ping 公共网站检查是否能上公网。
* ping 当前局域网的ip地址 检查是否在同一个局域网内。
* ping 127.0.0.1 检查本地网卡是否正常

## 端口和端口号

每运行一个网络程序都会有一个端口，想要给对应的程序发送数据，找到对应的端口即可。

端口是传输数据的通道，是数据传输必经之路。每一个端口都会有一个对应的端口号，想要找到端口通过端口号即可。

![](http://www.itcast.cn/files/image/202108/20210816143323007.png)

操作系统为了统一管理65536个端口，对端口进行了编号，这就是端口号，端口号其实就是一个数字。

### 端口号分类

知名端口号和动态端口号

**知名端口号**

知名端口号是指众所周知的端口号，范围从0到1023。这些端口号一般固定分配给一些服务，如：

* 21端口分配给 FTP（文件传输协议）服务。
* 25端口分配给 SMTP（简单邮件传输协议）服务。
* 80端口分配给 HTTP 服务。

**动态端口号**

一般应用程序使用端口号称为动态端口号，范围是从1024到65535。

* 如果应用程序没有设置端口号，操作系统会在动态端口号这个范围内随机生成一个给开发的应用程序使用。
* 当运行一个程序默认会有一个端口号，当这个程序退出时，所占用的这个端口号就会被释放。

## TCP 的介绍

TCP 的英文全拼(Transmission Control Protocol)简称传输控制协议，它是一种面向连接的、可靠的、基于字节流的传输层通信协议。

<img src="https://assets.website-files.com/5ff66329429d880392f6cba2/627cb3d4fcfd563ee9f2d43d_How%20does%20TCP%20work.jpg" style="zoom:90%;" />