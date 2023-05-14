# HTTP协议和静态Web服务器

## HTTP协议

HTTP 协议（HyperText Transfer Protocol）超文本传输协议。设计HTTP 协议目最初的是传输网页数据的，现在允许传输任意类型的数据。传输 HTTP 协议格式的数据是基于 TCP 传输协议的，发送数据之前需要先建立连接。

HTTP 协议规定了浏览器和 Web 服务器通信数据的格式，也就是说浏览器和web服务器通信需要使用http协议。

<img src="https://s2.51cto.com/images/blog/202108/08/34f4b49b82ef45932304e56fb5e283f2.png?x-oss-process=image/watermark,size_16,text_QDUxQ1RP5Y2a5a6i,color_FFFFFF,t_30,g_se,x_10,y_10,shadow_20,type_ZmFuZ3poZW5naGVpdGk=/format,webp/resize,m_fixed,w_1184" style="zoom:67%;" />

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

