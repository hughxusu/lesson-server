# Python链接MySQL

使用 python 操作数据库

```shell
pip install pymysql
```

pymysql的使用步骤：

1. 导入 pymysql 包
2. 创建连接对象 `conn=connect()`
   * 参数host：连接的mysql主机，如果本机是'localhost'
   * 参数port：连接的mysql主机的端口，默认是3306
   * 参数user：连接的用户名
   * 参数password：连接的密码
   * 参数database：数据库的名称
   * 参数charset：通信采用的编码方式，推荐使用utf8
3. 获取游标对象 `cur =conn.cursor()`
   * 使用游标执行SQL语句: execute(operation [parameters ]) 执行SQL语句，返回受影响的行数，主要用于执行insert、update、delete、select等语句
   * 获取查询结果集中的一条数据:cur.fetchone()返回一个元组, 如 (1,'张三')
   * 获取查询结果集中的所有数据: cur.fetchall()返回一个元组,如((1,'张三'),(2,'李四'))
   * 关闭游标: cur.close(),表示和数据库操作完成

```python
import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='ncut', charset='utf8')

cursor = conn.cursor()
sql = "select * from students;"
row_count = cursor.execute(sql)

print("SQL 语句执行影响的行数%d" % row_count)

for line in cursor.fetchall():
    print(line)

cursor.close()
conn.close()
```

pymysql 操作数据库

```python
import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='ncut', charset='utf8')
cursor = conn.cursor()

try:
    # 添加 SQL 语句
    sql = "insert into students(name) values('刘璐'), ('王美丽');"
    # 删除 SQL 语句
    sql = "delete from students where id = 5;"
    # 修改 SQL 语句
    sql = "update students set name = '王铁蛋' where id = 4;"
    # 执行 SQL 语句
    row_count = cursor.execute(sql)
    conn.commit()
except Exception as e:
    conn.rollback()

cursor.close()
conn.close()
```

## SQL 注入

用户提交带有恶意的数据与SQL语句进行字符串方式的拼接，从而影响了SQL语句的语义，最终产生数据泄露的现象。

```python
import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='ncut', charset='utf8')
cursor = conn.cursor()

try:
    sql = "select * from students where name = '%s';" % "李四' or 1 = 1 or '"
    row_count = cursor.execute(sql)
    result = cursor.fetchall()
    print(result)
    conn.commit()
except Exception as e:
    conn.rollback()

cursor.close()
conn.close()
```

防止 SQL 注入，SQL语句参数化：

* SQL语言中的参数使用%s来占位，此处不是python中的字符串格式化操作
* 将SQL语句中%s占位所需要的参数存在一个列表中，把参数列表传递给execute方法中第二个参数

```python
import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='ncut', charset='utf8')
cursor = conn.cursor()

try:
    sql = "select * from students where name = %s;"
    row_count = cursor.execute(sql, ('李四',))
    result = cursor.fetchall()
    print(result)
    conn.commit()
except Exception as e:
    conn.rollback()

cursor.close()
conn.close()
```





