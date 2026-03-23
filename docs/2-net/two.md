# HTTP协议和静态Web服务器

## HTTP协议

HTTP 协议（HyperText Transfer Protocol）超文本传输协议。设计HTTP 协议目最初的是传输网页数据的，现在允许传输任意类型的数据。传输 HTTP 协议格式的数据是基于 TCP 传输协议的，发送数据之前需要先建立连接。

HTTP 协议规定了浏览器和 Web 服务器通信数据的格式，也就是说浏览器和web服务器通信需要使用http协议。

<img src="https://s1.ax1x.com/2023/05/14/p9c10BD.jpg" style="zoom:67%;" />

### URL

URL（Uniform Resoure Locator）统一资源定位符，即网络资源的地址，也就是通常说的网址。

https://news.163.com/18/1122/10/E178J2O4000189FH.html

URL的组成：

1. 协议部分：https://、http://、ftp://
2. 域名部分：news.163.com
3. 资源路径部分：/18/1122/10/E178J2O4000189FH.html

域名：域名就是IP地址的别名，使用域名目的就是方便的记住某台主机IP地址。

URL的扩展：

https://news.163.com/hello.html?page=1&count=10

查询参数部分：?page=1&count=10

说明：? 后面的 page 表示第一个参数，后面的参数都使用 & 进行连接

### HTTP 请求报文

HTTP最常见的请求报文有两种：

* `GET` 方式的请求报文，获取 Web 服务器数据。
* `POST` 方式的请求报文，向 Web 服务器提交数据。
* 每项数据之间使用 `\r\n` 分割。

#### `GET` 请求说明

<img src="https://www.guru99.com/images/2/032020_0831_GETvsPOSTKe1.png" style="zoom:80%;" />

| 名称            | 说明                               |
| --------------- | ---------------------------------- |
| GET             | 请求方式                           |
| Host            | 服务器的主机地址和端口号，默认是80 |
| Connection      | 和服务端连接方式                   |
| User-Agent      | 用户代理，也就是客户端的名称       |
| Accept          | 可接受的数据类型                   |
| Accept-Encoding | 可接受的压缩格式                   |
| Accept-Language | 可接受的语言                       |
| Cookie          | 登录用户的身份标识                 |

#### `POST` 请求说明

<img src="https://www.guru99.com/images/2/032020_0831_GETvsPOSTKe2.png" style="zoom:80%;" />

| 名称 | 说明     |
| ---- | -------- |
| POST | 请求方式 |

> [!warning]
>
> POST 方式的请求报文可以有请求行、请求头、空行、请求体四部分组成。POST 方式可以允许没有请求体。

### HTTP 响应报文

![](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/images/HTTP_ResponseMessageExample.png)



| 名称         | 说明             |
| ------------ | ---------------- |
| Server       | 服务器名称       |
| Content-Type | 内容类型         |
| Connection   | 和服务端连接方式 |

> [!warning]
>
> 每项数据之间使用 `\r\n` 分割，响应头信息后面还有一个单独的 `\r\n` 不能省略。

## 静态Web服务器

可以为发出请求的浏览器提供静态文档的程序。

### 搭建 python 自带的静态服务器

在指定静态文件的目录下使用命令

```shell
python -m http.server 9000
```

`-m`  运行包里面的模块

### 搭建静态Web服务器

#### 返回固定页面数据

实现步骤：

1. 创建一个TCP服务端程序。
2. 获取浏览器发送的 http 请求报文数据。
3. 读取固定页面数据。
4. 把页面数据组装成 http 响应报文数据发送给浏览器。
5. 关闭服务于客户端的套接字。

```python
import socket

# 判断是否是主模块的代码
if __name__ == '__main__':
    # 1. 创建一个TCP服务端程序
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(("", 9090))
    tcp_server_socket.listen(128)
    
    while True:
        # 2. 获取浏览器发送的 http 请求报文数据
        new_socket, ip_port = tcp_server_socket.accept()
        recv_data = new_socket.recv(4096)
        print(recv_data)

        # 3. 读取固定页面数据，
        with open("static/index.html", "r") as file:
            file_data = file.read()

        # 4. 把页面数据组装成 http 响应报文数据发送给浏览器
        response_line = "HTTP/1.1 200 OK\r\n"
        response_header = "Server: PWS/1.0\r\n"
        response_body = file_data
        response = response_line + response_header + "\r\n" + response_body
        response_data = response.encode("utf-8")
        new_socket.send(response_data)
        
        # 5. 关闭服务于客户端的套接字
        new_socket.close()
```

#### 返回指定页面数据

1. 创建一个TCP服务端程序。
2. 获取浏览器发送的 http 请求报文数据，解析请求资源路径。
3. 读取指定文件的数据。
4. 把页面数据组装成 http 响应报文数据发送给浏览器。
5. 关闭服务于客户端的套接字。

```python
import socket
import os


def main():
    # 1. 创建一个TCP服务端程序。
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(("", 9090))
    tcp_server_socket.listen(128)
    
    while True:
      	# 2. 获取浏览器发送的 http 请求报文数据，解析请求资源路径。
        new_socket, ip_port = tcp_server_socket.accept()
        recv_data = new_socket.recv(4096)
        if len(recv_data) == 0:
          	print("关闭浏览器了")
            new_socket.close()
            return

        recv_content = recv_data.decode("utf-8")
        print(recv_content)
        request_list = recv_content.split(" ", maxsplit=2)
        request_path = request_list[1]
        print(request_path)

        # 3. 读取指定文件的数据。
        if request_path == "/":
            request_path = "/index.html"
            
        with open("static" + request_path, "rb") as file:  
            file_data = file.read()
				
        # 4. 把页面数据组装成 http 响应报文数据发送给浏览器
        response_line = "HTTP/1.1 200 OK\r\n"
        response_header = "Server: PWS/1.0\r\n"
        response_body = file_data
        response = (response_line + response_header + "\r\n").encode("utf-8") + response_body
        new_socket.send(response)

        # 5. 关闭服务于客户端的套接字。
        new_socket.close()

if __name__ == '__main__':
    main()
```

#### 返回错误页面面

判断请求的文件在服务端不存在，组装404状态的响应报文，发送给浏览器。

```python
import socket

def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(("", 9090))
    tcp_server_socket.listen(128)
    
    while True:
        new_socket, ip_port = tcp_server_socket.accept()
        recv_data = new_socket.recv(4096)
        if len(recv_data) == 0:
          	print("关闭浏览器了")
            new_socket.close()
            return

        recv_content = recv_data.decode("utf-8")
        print(recv_content)

        request_list = recv_content.split(" ", maxsplit=2)
        request_path = request_list[1]
        print(request_path)

        if request_path == "/":
            request_path = "/index.html"


        try: # 1. 打开资源文件
            with open("static" + request_path, "rb") as file: 
                file_data = file.read()
        except Exception as e: # 2. 资源打开错误返回错误页面
            response_line = "HTTP/1.1 404 Not Found\r\n"
            response_header = "Server: PWS/1.0\r\n"
            with open("static/error.html", "rb") as file:
                file_data = file.read()
                
            response_body = file_data
            response = (response_line +
                        response_header +
                        "\r\n").encode("utf-8") + response_body
            new_socket.send(response)
        else: # 3. 打开成功返回响应资源
            response_line = "HTTP/1.1 200 OK\r\n"
            response_header = "Server: PWS/1.0\r\n"
            response_body = file_data
            response = (response_line +
                        response_header +
                        "\r\n").encode("utf-8") + response_body
            new_socket.send(response)
        finally: # 4. 关闭服务于客户端的套接字
            new_socket.close()


# 判断是否是主模块的代码
if __name__ == '__main__':
    main()
```

#### 多线程版静态服务器

```python
import socket
import threading


def handle_client_request(new_socket):
    recv_client_data = new_socket.recv(4096)
    if len(recv_client_data) == 0:
        print("关闭浏览器了")
        new_socket.close()
        return

    recv_client_content = recv_client_data.decode("utf-8")
    print(recv_client_content)
    request_list = recv_client_content.split(" ", maxsplit=2)

    request_path = request_list[1]
    print(request_path)

    if request_path == "/":
        request_path = "/index.html"

    try:
        with open("static" + request_path, "rb") as file:
            file_data = file.read()
    except Exception as e:
        response_line = "HTTP/1.1 404 Not Found\r\n"
        response_header = "Server: PWS1.0\r\n"
        with open("static/error.html", "rb") as file:
            file_data = file.read()
        response_body = file_data
        response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body
        new_socket.send(response_data)
    else:
        response_line = "HTTP/1.1 200 OK\r\n"
        response_header = "Server: PWS1.0\r\n"
        response_body = file_data
        response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body
        new_socket.send(response_data)
    finally:
        new_socket.close()


def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    tcp_server_socket.bind(("", 9090))
    tcp_server_socket.listen(128)

    while True:
        new_socket, ip_port = tcp_server_socket.accept()
        # 多线程静态请求
        sub_thread = threading.Thread(target=handle_client_request, args=(new_socket,))
        sub_thread.setDaemon(True)
        sub_thread.start()


if __name__ == '__main__':
    main()
```

#### 面向对象版静态服务器

```python
import socket
import threading


# 定义web服务器类
class HttpWebServer(object):
    def __init__(self): # 初始化化服务器
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        tcp_server_socket.bind(("", 9090))
        tcp_server_socket.listen(128)
        self.tcp_server_socket = tcp_server_socket

    @staticmethod
    def handle_client_request(new_socket): # 处理请求方法
        recv_client_data = new_socket.recv(4096)
        if len(recv_client_data) == 0:
            print("关闭浏览器了")
            new_socket.close()
            return

        recv_client_content = recv_client_data.decode("utf-8")
        print(recv_client_content)
        request_list = recv_client_content.split(" ", maxsplit=2)

        request_path = request_list[1]
        print(request_path)

        if request_path == "/":
            request_path = "/index.html"

        try:
            with open("static" + request_path, "rb") as file:
                file_data = file.read()
        except Exception as e:
            response_line = "HTTP/1.1 404 Not Found\r\n"
            response_header = "Server: PWS1.0\r\n"
            with open("static/error.html", "rb") as file:
                file_data = file.read()
            response_body = file_data

            response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body
            new_socket.send(response_data)
        else:
            response_line = "HTTP/1.1 200 OK\r\n"
            response_header = "Server: PWS1.0\r\n"
            response_body = file_data
            response_data = (response_line + response_header + "\r\n").encode("utf-8") + response_body
            new_socket.send(response_data)
        finally:
            new_socket.close()

    def start(self): # 启动服务器
        while True:
            new_socket, ip_port = self.tcp_server_socket.accept()
            sub_thread = threading.Thread(target=self.handle_client_request, args=(new_socket,))
            sub_thread.setDaemon(True)
            sub_thread.start()


def main():
    web_server = HttpWebServer()
    web_server.start()


if __name__ == '__main__':
    main()
```

#### 增加控制命令行

```python
def main():
    print(sys.argv)
    if len(sys.argv) != 2:
        print("执行命令如下: python3 xxx.py 8000")
        return

    if not sys.argv[1].isdigit():
        print("执行命令如下: python3 xxx.py 8000")
        return

    port = int(sys.argv[1])
    web_server = HttpWebServer(port)
    web_server.start()


if __name__ == '__main__':
    main()
```

