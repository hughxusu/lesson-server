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

TCP 通信步骤：

1. 创建连接
2. 传输数据
3. 关闭连接

**TCP 的特点** 

1. 面向连接
   - 通信双方必须先建立好连接才能进行数据的传输，数据传输完成后，双方必须断开此连接，以释放系统资源。
2. 可靠传输
   - TCP 采用发送应答机制
   - 超时重传
   - 错误校验
   - 流量控制和阻塞管理

TCP 是一个稳定、可靠的传输协议，常用于对数据进行准确无误的传输，比如: 文件下载，浏览器上网。

## socket 的介绍

socket (简称 套接字) 是进程之间通信一个工具，里面封装 TCP 服务协议。

<img src="https://s1.ax1x.com/2023/05/08/p90npEF.png" style="zoom:80%;" />

## TCP 网络应用程序开发

### 开发流程

TCP 网络应用程序开发分为：TCP 客户端程序开发和 TCP 服务端程序开发

### 

![](https://book.itheima.net/uploads/course/python/images/PythonSenior/2.3.2.2/clip_image001.jpg)

**TCP 客户端程序开发流程**

1. 创建客户端套接字对象
2. 和服务端套接字建立连接
3. 发送数据
4. 接收数据
5. 关闭客户端套接字

**TCP 服务端程序开发流程**

1. 创建服务端端套接字对象
2. 绑定端口号
3. 设置监听
4. 等待接受客户端的连接请求
5. 接收数据
6. 发送数据
7. 关闭套接字

### TCP 客户端程序开发

```python
import socket


if __name__ == '__main__':

    # 1. 创建tcp客户端套接字
    # AF_INET: ipv4地址类型
    # SOCK_STREAM： tcp传输协议类型
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 2. 和服务端套接字建立连接
    client.connect(("127.0.0.1", 9090))

    # 3. 发送数据到服务端
    send = "hello, socket"
    row = send.encode("utf-8")
    client.send(row)
    
    # 4. 接收服务端的数据
    accept = client.recv(1024)
    result = accept.decode("utf-8")
    print("接收服务端的数据为:", result)
    
    # 5. 关闭套接字
    client.close()
```

### TCP服务端程序开发

```python
import socket

if __name__ == '__main__':
    # 1. 创建tcp服务端套接字
    # AF_INET: ipv4 , AF_INET6: ipv6
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True) # 设置端口号复用
    
    # 2. 绑定端口号
    server.bind(("", 9090))
    
    # 3. 设置监听
    server.listen(128)
    
    # 4. 等待接受客户端的连接请求
    client, ip_port = server.accept()
    print("客户端的ip和端口号为:", ip_port)
    
    # 5. 接收客户端的数据
    accept = client.recv(1024)
    result = accept.decode("utf-8")
    print("接收客户端的数据为:", result)


    # 6. 发送数据到客户端
    send_content = "问题正在处理中..."
    send_data = send_content.encode("utf-8")
    client.send(send_data)
    client.close()
    
    # 7. 关闭服务端套接字， 表示服务端以后不再等待接受客户端的连接请求
    server.close()
```

### 多任务开发

```python
import socket
import threading


def serve_client(port, client):
    print("客户端的ip和端口号为:", port)
    while True:
        accept = client.recv(1024)
        if accept:
            print("接收的数据长度是:", len(accept))
            result = accept.decode("utf-8")
            print("接收客户端的数据为:", result, port)

            send_content = "问题正在处理中..."
            send_data = send_content.encode("utf-8")
            client.send(send_data)
        else:
            print("客户端下线了:", port)
            break
    client.close()


if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    server.bind(("", 9090))
    server.listen(128)

    while True:
        client, ip_port = server.accept()
        sub_thread = threading.Thread(target=serve_client, args=(ip_port, client))
        sub_thread.setDaemon(True)
        sub_thread.start()
```

## socket 原理

当创建一个TCP socket对象的时候会有一个发送缓冲区和一个接收缓冲区，这个发送和接收缓冲区指的就是内存中的一片空间。

**发送数据**

数据必须得通过网卡发送，应用程序是无法直接通过网卡发送数据的，它需要调用操作系统接口。应用程序把发送的数据先写入到发送缓冲区，再由操作系统控制网卡把发送缓冲区的数据发送给服务端网卡 。

**接收数据**

操作系统通过网卡接收数据，把接收的数据写入到接收缓冲区，应用程序再从接收缓存区获取客户端发送的数据。

![](https://s1.ax1x.com/2023/05/08/p90QDFU.png)