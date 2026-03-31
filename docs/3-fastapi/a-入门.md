# FastAPI 入门

安装fast api

`uv add fastapi uvicorn`

安装uvicorn

`pip install uvicorn`

在终端运行

`uvicorn main:app --reload`

* **`--reload`**: 热重载模式。当你修改代码并保存时，服务器会自动重启。这在开发阶段非常高效。

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

