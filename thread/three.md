# 线程

线程是 cpu 调度的基本单位，也是进程中执行代码的一个分支，每个进程至少都有一个线程（即主线程）。

> [!note]
>
> 程序启动后会有一个默认的主线程，可以人为创建子线程，多线程可以完成多任务。

![](https://www.xinbaoku.com/uploads/allimg/181102/2-1Q1021I11WX.gif)



## 多线程的使用

线程是Python程序中实现多任务的另外一种方式，线程的执行需要cpu调度来完成。

### 使用线程

`import threading` 线程包

Thread([group [, target [, name [, args [, kwargs]]]]])

- group: 线程组，目前只能使用None
- target: 执行的目标任务名
- args: 以元组的方式给执行任务传参
- kwargs: 以字典方式给执行任务传参
- name: 线程名，一般不用设置

Thread 创建的实例对象的常用方法：

* start()：启动子进程实例（创建子进程）。
* join()：等待子进程执行结束。

```python
import threading
import time

def sing():
    current_thread = threading.current_thread()
    print("sing:", current_thread)

    for i in range(5):
        print("唱歌中...")
        time.sleep(0.2)


def dance():
    current_thread = threading.current_thread()
    print("dance:", current_thread)

    for i in range(5):
        print("跳舞中...")
        time.sleep(0.2)


if __name__ == '__main__':

    # 获取当前线程
    current_thread = threading.current_thread()
    print("main_thread:", current_thread)

    # 创建子线程
    sing_thread = threading.Thread(target=sing, name="sing_thread")
    dance_thread = threading.Thread(target=dance, name="dance_thread")
    # 启动子线程执行对应的任务
    sing_thread.start()
    sing_thread.terminate()
    dance_thread.start()
```

## 使用带有参数的任务

如果进程执行的任务带有参数，可以通过 Thread 类执行任务并给任务传参数：

* `args` 表示以元组方式给执行任务传参
* `kwargs` 表示以字典方式给执行任务传参

```python
import threading

def show_info(name, age):
    print("name: %s age: %d" % (name, age))
```

`args` 参数的使用

```python
if __name__ == '__main__':
    sub_thread = threading.Thread(target=show_info, args=("tom", 20))
    sub_thread.start()
```

`kwargs` 参数的使用

```python
if __name__ == '__main__':
    sub_thread = threading.Thread(target=show_info, kwargs={"name": "tom", "age": 18})
    sub_thread.start()
```

## 线程的特点

**线程执行是无序的**

线程的调度由 cpu 控制，无法人为干预。

```python
import threading
import time

def task():
    time.sleep(0.5)
    print(threading.current_thread())

if __name__ == '__main__':
    for i in range(10):
        sub_thread = threading.Thread(target=task)
        sub_thread.start()
```

**主线程会等待所有的子线程执行结束再结束**

```python
import threading
import time

def task():
    for i in range(6):
        print("任务执行中...")
        time.sleep(0.5)

if __name__ == '__main__':
    sub_thread = threading.Thread(target=task)
    sub_thread.start()
    
    time.sleep(1)
    print("over")
```

守护主线程：守护主线程就是主线程退出子线程销毁不再执行

1. 直接将线程设置为守护主线程

```python
if __name__ == '__main__':
   	sub_thread = threading.Thread(target=task, daemon=True)
    sub_thread.start()
    
    time.sleep(1)
    print("over")
```

2. 创建线程后将线程设置为守护主线程

```python
if __name__ == '__main__':
    sub_thread = threading.Thread(target=task)
    sub_thread.setDaemon(True)
    sub_thread.start()
    
    time.sleep(1)
    print("over")
```

**线程之间共享全局变量**

```python
import threading
import time

g_list = []

def add_data():
    for i in range(5):
        g_list.append(i)
        print("add:", i)
        time.sleep(0.2)

    print("添加数据完成:", g_list)

def read_data():
    print("read:", g_list)

if __name__ == '__main__':
    add_thread = threading.Thread(target=add_data)
    read_thread = threading.Thread(target=read_data)

    add_thread.start()
    add_thread.join()
    read_thread.start()
```

## 互斥锁

共享数据的同步问题

```python
import threading

g_num = 0

def task1():
    for i in range(1000000): # 循环100万次
        global g_num
        g_num = g_num + 1

    print("task1:", g_num)

def task2():
    for i in range(1000000):
        global g_num
        g_num = g_num + 1

    print("task2:", g_num)

if __name__ == '__main__':
    first_thread = threading.Thread(target=task1)
    second_thread = threading.Thread(target=task2)

    first_thread.start()
    # first_thread.join()
    second_thread.start()
```

> [!warning]
>
> 循环计算的结果小于两百万次，原因是多线程程序对 g_num 数据可能发生同时读写。
>
> 解决数据同步问题的办法是
>
> 1. 线程等待
> 2. 互斥锁

互斥锁：对共享数据进行锁定，保证同一时刻只能有一个线程去操作。

互斥锁的执行过程：多个线程一起去抢，抢到锁的线程先执行，没有抢到锁的线程需要等待，等互斥锁使用完释放后，其它等待的线程再去抢这个锁。

### 互斥锁的使用

互斥锁使用步骤：

1. `mutex = threading.Lock()` 创建锁
2. `mutex.acquire()` 上锁
3. `mutex.release()` 释放锁

```python
import threading

g_num = 0
lock = threading.Lock()

def task1():
    lock.acquire()
    for i in range(1000000):
        global g_num
        g_num = g_num + 1

    print("task1:", g_num)
    lock.release()

def task2():
    lock.acquire()
    for i in range(1000000):
        global g_num
        g_num = g_num + 1

    print("task2:", g_num)
    lock.release()

if __name__ == '__main__':
    first_thread = threading.Thread(target=task1)
    second_thread = threading.Thread(target=task2)

    first_thread.start()
    second_thread.start()
```

> [!attention]
>
> 如果互斥锁没有正常释放，会产生死锁现象。死锁会一直等待对方释放锁。死锁会造成应用程序的停止响应，不能再处理其它任务了。