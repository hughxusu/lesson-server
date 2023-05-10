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

### HTTP 响应报文