-- day01 --
-- 库操作
1.查看所有库
show databases;

2.创建库
  2.1 mysql5.7默认字符集：latin1
  2.2 mysql8.0默认字符集：utf8
  2.3 手动设置其他字符集: charset=gbk
create database if not exists mydb1 charset=utf8;

3.切换库
use mydb1;

4.查看创建库的语句
show create database mydb1;

5.删除库
drop database if exists mydb1;

-- **************练习***************--
1. 删除数据库mydb1和mydb2，如果不存在则不做任何操作
drop database if exists mydb1;
drop database if exists mydb2;

2. 创建 mydb1和 mydb2 数据库 字符集分别为 UTF8 和 GBK
create database if not exists mydb1 charset=utf8;
create database if not exists mydb2 charset=gbk;

3. 查询所有库
show databases;

4. 查看 mydb1和 mydb2 库的字符集是否正确(查看创建时的SQL)
show create database mydb1;
show create database mydb2;

5. 先使用 mydb2库，再使用 mydb1库
use mydb2;
use mydb1;

6. 删除这两个数据库
drop database if exists mydb1;
drop database if exists mydb2;

-- ******表的相关操作**************************
create database if not exists mydb;
use mydb;
1.查看当前库所有的表
show tables;

2.创建表
create table if not exists user(
    id int,
    username varchar(20),
    password varchar(20),
    nickname varchar(20)
);

3.查看创建表的语句
show create table user;

4.查看表结构
desc user;

5.删除表
drop table user;

-- *******练习******************
1. 创建数据库 mydb3 字符集UTF8
2. 使用数据库 mydb3
3. 创建英雄表 hero, 有名字和年龄两个字段
4. 查看当前库中所有的表
5. 查看创建表hero的语句[字符集]
6. 查看hero的表结构

create database if not exists mydb3 charset=utf8;
use mydb3;
create table if not exists hero(
    name varchar(20),
    age int
);
show tables;
show create table hero;
desc hero;

-- *********表字段操作 **********************
alter table 表名 字段操作
1.添加字段
alter table hero add id int first;
alter table hero add gender varchar(1) after name;
alter table hero add attack int;

2.删除字段
alter table hero drop attack;

3.修改数据类型
alter table hero modify gender varchar(20);

-- *****课堂练习*********************
1. 创建数据库mydb4 字符集UTF8
create database if not exists mydb4 charset=utf8;

2. 切换到该库
use mydb4;

3. 创建teacher表 有名字(name)字段
create table if not exists teacher(
    name varchar(20)
);

4. 添加表字段: 最后添加age 最前面添加id(int型) , age前面添加salary工资(int型)
alter table teacher add age int;
alter table teacher add id int first;
alter table teacher add salary int after name;

5. 删除age字段
alter table teacher drop age;

6. 删除表teacher
drop table teacher;

7. 删除数据库mydb4
drop database if exists mydb4;

-- *********表记录的操作***********************
use mydb;
show tables;
1.插入数据(insert)
1.1 单条数据全字段插入
insert into user values(1,'花千骨','123456','小骨');

1.2 多条数据全字段插入
insert into user values
    (2, '薛杉杉','123456','杉杉来了'),
    (3, '楚乔传','123456','楚乔');

1.3 部分字段数据插入
insert into user(id,username) values(4, '知否知否');

1.4 关于默认值
create table if not exists user(
    id int,
    username varchar(20) default '无名',
    password varchar(20) default '123456',
    nickname varchar(20) default '佚名'
);
alter table user modify nickname varchar(20) default '佚名';

insert into user(id,username,password)
values(5, '超哥哥', '123456');

-- ***********更新数据*******************
语法：update 表名 set 字段名=新值,字段名=新值 where 过滤条件;
1.id为4的数据，密码修改为654321
update user set password='654321' where id=4;

2.修改花千骨用户的密码为 111111, 昵称修改为:杀阡陌
update user set password='111111',nickname='杀阡陌'
where username='花千骨';

-- *****删除语句***************************
命令语法：delete from 表名 where 条件;
1.删除id>=4的所有数据;
delete from user where id>=4;

select * from user;

-- 课堂练习 ------------
1. 创建数据库mydb5 字符集UTF8 并使用
create database if not exists mydb5 charset=utf8;

2. 创建hero表, 有name字段,字符集UTF8
use mydb5;
create table if not exists hero(
    name varchar(20)
);

3. 最后面添加价格字段money(整数类型), 最前面添加id字段(整数类型), name后面添加 age字段(整
数类型)
alter table hero add money int;
alter table hero add id int first;
alter table hero add age int after name;

4. 表中添加以下数据:
1,李白,50,6888
2,赵云,30,13888
3,刘备,25,6888
insert into hero values
    (1,'李白',50,6888),
    (2,'赵云',30,13888),
    (3,'刘备',25,6888);

5. 修改刘备年龄为52岁
update hero set age=52 where name='刘备';

6. 修改年龄小于等于50岁的价格为5000
update hero set money=5000 where age<=50;

7. 删除价格为5000的信息
delete from hero where money=5000;

8. 删除表和库
drop table if exists hero;
drop database if exists mydb5;

-- 数据类型 *******************
use mydb;
create table if not exists userinfo(
    id int,
    username varchar(20),
    password char(32),
    age tinyint,
    gender char(1),
    birthday date,
    comment text,
    created_time datetime default now()
);

1.方式1
insert into userinfo values
    (1,'Liying','123456',37,'F','1987-10-16','Beautiful','2024-06-28 00:00:00');

2.方式2
insert into userinfo values
    (2,'ying','123456',37,'F','19871016','Beautiful','20240627000000');

3.方式3
insert into userinfo values
    (3,'lili','123456',37,'F','19871016','Beautiful',now());

select * from userinfo\G;

-- ******约束*****************
1.主键约束:非空且唯一
create table if not exists t2(
    id int,
    name varchar(15),
    primary key(id)
);
insert into t1 values(1, '亚瑟');














