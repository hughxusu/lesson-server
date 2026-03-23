# MySQL基础

## 数据类型

数据类型是指在创建表的时候为表中字段指定数据类型，只有数据符合类型要求才能存储起来，使用数据类型的原则是:够用就行，尽量使用取值范围小的，而不用大的，这样可以更多的节省存储空间。

常用数据类型如下：

- 整数：int，bit
- 小数：decimal 表示浮点数，如 decimal(5，2) 表示共存5位数，小数占 2 位。
- 字符串：
  - varchar 表示固定长度的字符串，如char(3)，如果填充'ab'时会补一个空格为'ab '，3表示字符数
  - char 表示可变长度的字符串，如varchar(3)，填充'ab'时就会存储'ab'，3表示字符数
  -  text 表示存储大文本，当字符大于 4000 时推荐使用。
- 日期时间：date, time, datetime
- 枚举类型（enum）

> [!warning]
>
> 对于图片、音频、视频等文件，不存储在数据库中，而是上传到某个服务器上，然后在表中存储这个文件的保存路径。

整数类型

| 类型        | 字节大小 | 有符号范围(Signed)                         | 无符号范围(Unsigned)     |
| :---------- | :------- | :----------------------------------------- | :----------------------- |
| TINYINT     | 1        | -128 ~ 127                                 | 0 ~ 255                  |
| SMALLINT    | 2        | -32768 ~ 32767                             | 0 ~ 65535                |
| MEDIUMINT   | 3        | -8388608 ~ 8388607                         | 0 ~ 16777215             |
| INT/INTEGER | 4        | -2147483648 ~2147483647                    | 0 ~ 4294967295           |
| BIGINT      | 8        | -9223372036854775808 ~ 9223372036854775807 | 0 ~ 18446744073709551615 |

字符串类型

| 类型     | 说明                        | 使用场景                     |
| :------- | :-------------------------- | :--------------------------- |
| CHAR     | 固定长度，小型数据          | 身份证号、手机号、电话、密码 |
| VARCHAR  | 可变长度，小型数据          | 姓名、地址、品牌、型号       |
| TEXT     | 可变长度，字符个数大于 4000 | 存储小型文章或者新闻         |
| LONGTEXT | 可变长度， 极大型文本数据   | 存储极大型文本数据           |

时间类型

| 类型      | 字节大小 | 示例                                                  |
| :-------- | :------- | :---------------------------------------------------- |
| DATE      | 4        | '2020-01-01'                                          |
| TIME      | 3        | '12:29:59'                                            |
| DATETIME  | 8        | '2020-01-01 12:29:59'                                 |
| YEAR      | 1        | '2017'                                                |
| TIMESTAMP | 4        | '1970-01-01 00:00:01' UTC ~ '2038-01-01 00:00:01' UTC |

## 数据约束

约束是指数据在数据类型限定的基础上额外增加的要求：

- 主键 primary key 物理上存储的顺序. MySQL 建议所有表的主键字段都叫 id, 类型为 int unsigned。
- 非空 not null 此字段不允许填写空值.
- 惟一 unique 此字段的值不允许重复.
- 默认 default 当不填写字段对应的值会使用默认值，如果填写时以填写为准.
- 外键 foreign key 对关系字段进行约束, 当为关系字段填写值时, 会到关联的表中查询此值是否存在, 如果存在则填写成功, 如果不存在则填写失败并抛出异常.

## 数据库基础操作

查看数据库是否链接成功

```mysql
select now(); # 显示当前时间
```

### 数据库操作

查看所有数据库

```sql
show databases;
```

创建数据库

```mysql
create database ncut charset=utf8; # ncut 数据库名
```

使用数据库

```mysql
use ncut; # ncut 数据库名
```

查看当前使用的数据库

```mysql
select database();
```

删除数据库

```mysql
drop database ncut; # ncut 数据库名
```

查看创库SQL语句

```mysql
show create database ncut; # ncut 数据库名
```

### 表操作

查看当前数据库中所有表

```mysql
show tables;
```

创建表

```mysql
create table students(
  # 字段名称 数据类型 约束条件
  id int unsigned primary key auto_increment not null,
  name varchar(20) not null,
  age tinyint unsigned default 0,
  height decimal(5, 2),
  gender enum('男', '女')
);
```

添加字段 

```mysql
#							表名				字段名称	 数据类型  约束条件
alter table students add birthday datetime; # students 表名
```

修改字段类型

```mysql
#							表名					 字段名称   数据类型  约束条件
alter table students modify birthday date not null;
```

> [!warning]
>
> modify 只能修改字段类型或者约束，不能修改字段名。

修改字段名和字段类型

```mysql
#							表名					 原名      新名   数据类型  约束条件
alter table students change birthday birth datetime not null;
```

删除字段

```mysql
alter table students drop birth; # birth 删除字段
```

查看创表SQL语句

```mysql
show create table students; # students 表名
```

删除表

```mysql
drop table students; # students 表名
```

### 数据操作

添加数据

```mysql
#            表名             数据值
insert into students values(0, '张三', default, default, '男');

#            表名      列名               数据值
insert into students(name, age) values('张三', 15);

#            表名              多个数据
insert into students values(0, '张三', 55, 1.75, '男'),(0, '李四', 58, 1.85, '男');

#             表名     列名           多个数据
insert into students(name, height) values('张三', 1.75),('李四', 1.6);
```

> [!warning]
>
> 主键列是自动增长。全列插入时需要占位，通常使用空值（0或者null或者default）

修改数据

```sql
#       表名         列名   修改值                    数据条件
update students set age = 18, gender = '女' where id = 1;
```

删除数据

```mysql
#             表名           数据条件 
delete from students where id = 5;
```

查询数据

```mysql
select * from students; # students 表名 查询所有列
#        列名          表名
select id, name from students; # 查询指定列 
```

> [!warning]
>
> 数据删除通常使用逻辑删除
>
> ```mysql
> alter table students add isdelete bit default 0;
> update students set isdelete = 1 where id = 8;
> ```

