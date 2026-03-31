# UV

[uv](https://uv.oaix.tech/)是一个用 Rust 编写的极速Python包和项目管理工具，主要用于工程项目管理。

* uv可以管理虚拟环境和安装包。
* 与Conda环境互补
  * conda管理Python 版本和复杂科学计算环境。
  * uv主要用于工程项目的管理。
* 使用uv管理项目，每初始化新一个项目就创建一个虚拟虚拟环境。

> [!alert]
>
> uv和conda都包含了虚拟环境的管理，所以二者只能选用一个，如果需要使用uv管理项目要关闭conda虚拟环境。

## UV的使用

初始化项目

```shell
uv init --python 3.13
```





