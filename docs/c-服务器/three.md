# Web 框架

## web 框架概述

![](https://s1.ax1x.com/2023/05/30/p9jj8vn.png)

web框架专门负责处理用户的动态资源请求，这个web框架其实就是一个为web服务器提供服务的应用程序，简称web框架。

静态资源：不需要经常变化的资源，这种资源web服务器可以提前准备好，比如: png/jpg/css/js等文件。

动态资源：根据请求变化动态生成的页面，这种资源web服务器无法提前准备好，需要web框架来帮web服务器进行准备，在这里web服务器可以把.html的资源请求认为是动态资源请求交由web框架进行处理。

WSGI协议：它是web服务器和web框架之间进行协同工作的一个规则，WSGI协议规定web服务器把动态资源的请求信息传给web框架处理，web框架把处理好的结果返回给web服务器。

## 框架开发

接收web服务器的动态资源请求，给web服务器提供处理动态资源请求的服务。

```python
import socket
import threading
import framework


class HttpWebServer(object):
    def __init__(self, port):
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        tcp_server_socket.bind(("", port))
        tcp_server_socket.listen(128)
        self.tcp_server_socket = tcp_server_socket

    @staticmethod
    def handle_client_request(new_socket):
        recv_data = new_socket.recv(4096)
        if len(recv_data) == 0:
            new_socket.close()
            return

        recv_content = recv_data.decode("utf-8")
        print(recv_content)

        request_list = recv_content.split(" ", maxsplit=2)
        request_path = request_list[1]
        print(request_path)

        if request_path == "/":
            request_path = "/index.html"

        if request_path.endswith(".html"):
            env = {
                "request_path": request_path,
            }
            status, headers, response_body = framework.handle_request(env)
            response_line = "HTTP/1.1 %s\r\n" % status
            response_header = ""
            for header in headers:
                response_header += "%s: %s\r\n" % header

            response_data = (response_line +
                             response_header +
                             "\r\n" +
                             response_body).encode("utf-8")

            new_socket.send(response_data)
            new_socket.close()
        else:
            try:
                with open("static" + request_path, "rb") as file:
                    file_data = file.read()
            except Exception as e:
                response_line = "HTTP/1.1 404 Not Found\r\n"
                response_header = "Server: PWS/1.0\r\n"
                with open("static/error.html", "rb") as file:
                    file_data = file.read()
                response_body = file_data
                response = (response_line +
                            response_header +
                            "\r\n").encode("utf-8") + response_body
                new_socket.send(response)
            else:
                response_line = "HTTP/1.1 200 OK\r\n"
                response_header = "Server: PWS/1.0\r\n"
                response_body = file_data
                response = (response_line +
                            response_header +
                            "\r\n").encode("utf-8") + response_body
                new_socket.send(response)
            finally:
                new_socket.close()

    def start(self):
        while True:
            new_socket, ip_port = self.tcp_server_socket.accept()
            sub_thread = threading.Thread(target=self.handle_client_request, args=(new_socket,))
            sub_thread.setDaemon(True)
            sub_thread.start()


def main():
    web_server = HttpWebServer(8000)
    web_server.start()

if __name__ == '__main__':
    main()
```

处理动态请求

```python
import time

def index():
    status = "200 OK"
    response_header = [("Server", "PWS/1.1")]
    data = time.ctime()
    return status, response_header, data

def not_found():
    status = "404 Not Found"
    response_header = [("Server", "PWS/1.1")]
    data = "not found"
    return status, response_header, data

def handle_request(env):
    request_path = env["request_path"]
    print("动态资源请求的地址:", request_path)
    if request_path == "/index.html":
        result = index()
        return result
    else:
        result = not_found()
        return result
```

替换模板数据

```python
def index():
    status = "200 OK"
    response_header = [("Server", "PWS/1.1")]
    with open("template/index.html", "r") as file:
        file_data = file.read()

    data = time.ctime()
    response_body = file_data.replace("{%content%}", data)
    return status, response_header, response_body
```

## 路由开发

路由就是请求的URL到处理函数的映射，也就是说提前把请求的URL和处理函数关联好。

| 请求路径     | 处理函数   |
| :----------- | :--------- |
| /index.html  | index函数  |
| /center.html | center函数 |

增加路由

```python
def center():
    status = "200 OK"
    response_header = [("Server", "PWS/1.1")]
    with open("template/center.html", "r") as file:
        file_data = file.read()
        
    data = time.ctime()
    response_body = file_data.replace("{%content%}", data)
    return status, response_header, response_body

route_list = [
    ("/index.html", index),
    ("/center.html", center),
]

def handle_request(env):
    request_path = env["request_path"]
    print("动态资源请求的地址:", request_path)

    for path, func in route_list:
        if request_path == path:
            result = func()
            return result
    else:
        result = not_found()
        return result
```

带有装饰器的路由

```python
def route(path):
    def decorator(func):
        route_list.append((path, func))
        def inner():
            result = func()
            return result
        return inner
    return decorator

@route("/index.html")  
def index():
    status = "200 OK"
    response_header = [("Server", "PWS/1.1")]
    with open("template/index.html", "r") as file:
        file_data = file.read()

    data = time.ctime()
    response_body = file_data.replace("{%content%}", data)
    return status, response_header, response_body

@route("/center.html")
def center():
    status = "200 OK"
    response_header = [("Server", "PWS/1.1")]
    with open("template/center.html", "r") as file:
        file_data = file.read()

    data = time.ctime()
    response_body = file_data.replace("{%content%}", data)
    return status, response_header, response_body

def not_found():
    status = "404 Not Found"
    response_header = [("Server", "PWS/1.1")]
    data = "not found"
    return status, response_header, data

def handle_request(env):
    request_path = env["request_path"]
    print("动态资源请求的地址:", request_path)

    for path, func in route_list:
        if request_path == path:
            result = func()
            return result
    else:
        result = not_found()
        return result


if __name__ == '__main__':
    print(route_list)
```

## 数据显示

准备数据

```mysql
create database stock_db charset=utf8;
use stock_db;
source stock_db.sql;
```

数据显示

```python
import pymysql

@route("/index.html")
def index():
    status = "200 OK"
    response_header = [("Server", "PWS/1.1")]
    with open("template/index.html", "r") as file:
        file_data = file.read()
    conn = pymysql.connect(host="localhost",
                           port=3306,
                           user="root",
                           password="123456",
                           database="stock_db",
                           charset="utf8")

    cursor = conn.cursor()
    sql = "select * from info;"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    cursor.close()
    conn.close()
    data = ""
    for row in result:
        data += """<tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td><input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="000007"></td>
               </tr>""" % row

    response_body = file_data.replace("{%content%}", data)
    return status, response_header, response_body
```

## 数据接口

```python
import json

@route("/center_data.html")
def center_data():
    conn = pymysql.connect(host="localhost",
                           port=3306,
                           user="root",
                           password="123456",
                           database="stock_db",
                           charset="utf8")
    cursor = conn.cursor()
    sql = '''select i.code, i.short, i.chg, i.turnover, i.price, i.highs, f.note_info 
             from info i inner join focus f 
             on i.id = f.info_id;
          '''
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    center_data_list = [{
                            "code": row[0],
                            "short": row[1],
                            "chg": row[2],
                            "turnover": row[3],
                            "price": str(row[4]),
                            "highs": str(row[5]),
                            "note_info": row[6]
                         } for row in result]
    print(center_data_list)
    json_str = json.dumps(center_data_list, ensure_ascii=False)
    print(json_str)
    print(type(json_str))
    cursor.close()
    conn.close()
    status = "200 OK"
    response_header = [
        ("Server", "PWS/1.1"),
        ("Content-Type", "text/html;charset=utf-8")
    ]
    return status, response_header, json_str
```

