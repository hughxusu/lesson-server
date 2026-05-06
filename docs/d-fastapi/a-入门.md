# FastAPI 入门

## 搭建开发环境

[uv](https://uv.oaix.tech/)是一个用 Rust 编写的极速Python包和项目管理工具，主要用于工程项目管理。

* uv可以管理虚拟环境和安装包。
* 与Conda环境互补
  * conda管理Python 版本和复杂科学计算环境。
  * uv主要用于工程项目的管理。
* 使用uv管理项目，每初始化新一个项目就创建一个虚拟虚拟环境。

> [!alert]
>
> uv和conda都包含了虚拟环境的管理，所以二者只能选用一个，如果需要使用uv管理项目要关闭conda虚拟环境。

配置uv的镜像源

1. 在`~/.config`目录下创建`uv`目录。
2. 在`uv`目录中创建`uv.toml`文件。
3. 在`uv.toml`文件中可以添加中科大镜像源。

```shell
# PyPI 镜像源配置（加速包下载）
[[index]]
url = "https://mirrors.ustc.edu.cn/pypi/web/simple"
default = true

# Python 解释器下载镜像（加速 uv python install）
python-install-mirror = "https://mirrors.ustc.edu.cn/github-release/astral-sh/python-build-standalone/"
```

### UV的使用

初始化项目

```shell
uv init --python 3.13

uv sync
```

## Fast API安装

安装fast api和uvicorn

`uv add fastapi uvicorn`

安装uvicorn

在终端运行

`uvicorn main:app --reload`

* `--reload`：热重载模式。当你修改代码并保存时，服务器会自动重启。这在开发阶段非常高效。

```python
@app.get("/sync")
def func_sync():
  start = time.time()
  for i in range(10):
  time.sleep(1)
  end = time.time()
  return {"time": f'{end-start:.2f}s'}


@app.get("/async")
async def func_async():
  start = time.time()
  tasks = [asyncio.sleep(1) for i in range(10)]
  await asyncio.gather(*tasks)
  end = time.time()
  return {"time": f'{end-start:.2f}s'}
```

安装数据库

```shell
# 安装orm
uv add fastapi sqlmodel

# 安装数据库管理
uv add alembic

# 初始化数据库管理工具
alembic init -t async alembic # 异步
alembic init alembic # 同步
```

