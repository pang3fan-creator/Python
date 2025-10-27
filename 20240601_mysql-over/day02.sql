-- 约束 ------------------------------------
mysql -uroot -p123456
create database if not exists day02db;
use day02db;

1.主键约束:
  1.1 非空且唯一,作为表中表记录的唯一标识;
  1.2 一般结合自增长属性auto_increment

create table if not exists t1(
    id int primary key auto_increment,
    name varchar(20) not null
);

insert into t1(name) values('颖火虫');
insert into t1(name) values('萤火虫');

insert into t1(id, name) values(8, '迪丽热巴');
insert into t1(id, name) values(null, '迪丽热巴');

2.非空约束:not null
insert into t1(name) values(null);

-- ******唯一约束unique  非空约束not null  默认约束 default 默认值
create table if not exists t3(
    id int primary key auto_increment comment '用户编号',
    name varchar(20) unique comment '用户名',
    age tinyint not null default 0 comment '年龄',
    phone char(11) not null default '10000000000' comment '手机号',
    score decimal(4,1) not null default 0.0 comment '成绩',
    created datetime not null default now() comment '注册时间'
);
desc t2;
2.1 唯一约束
insert into t2(name) values('只手遮天');

将id>=3的数据,age都加5
update t2 set age=age+5 where id>=3;

select * from t1;

-- *****课堂练习***********************
1. 创建用户表 userinfo ,字段如下
    用户编号id: 整型 主键 自增长
    用户名username: 变长20, 不允许为空, 不允许重复
    密码password: 变长80, 不允许为空
    邮箱email: 变长255, 允许为空
    手机号phone: 定长11, 不允许为空
    生日birth: DATE类型,可以为空
    金额balance: 浮点型(7,2), 不允许为空,默认值为0.00
    注册时间created_time: DATETIME, 不允许为空

create table if not exists userinfo(
    id int primary key auto_increment,
    username varchar(20) not null unique,
    password varchar(80) not null,
    email varchar(255),
    phone char(11) not null,
    birth date,
    balance decimal(7,2) not null default 0.00,
    created_time datetime not null
);

2. 查看表结构
desc userinfo;

3. 在表中插入2条表记录(自定义)
insert into userinfo values
    (1,'lala','123456','lala@tedu.cn','12345678901','1990-01-01',8.88,'1997-07-01 00:00:00'),
    (2,'lili','123456','lala@tedu.cn','12345678901','1990-01-01',8.88,'1999-12-20 00:00:00');

4. 查询所有的表记录
select * from userinfo;

5. 将id为2的数据的手机号修改一下,金额+100, 再查询确认
update userinfo set phone='09876543210',balance=balance+100
where id=2;

6. 删除金额大于 20 的表记录
delete from userinfo where balance>=20;

-- ************查询****************
1.基础查询
  1.1 全列查询
      select * from teacher;
  1.2 部分字段查询
      select id,name,age from teacher;

2.where条件：算术运算符
  2.1 查找年龄为偶数的老师信息
    select name,age from teacher where age%2=0;
  2.2 查看年薪高于60000的老师都有谁?
    select name,salary*12 from teacher where salary*12>=60000;

3.where条件：逻辑运算符 and  or  not
  3.1 查看7岁的"大队长"都有谁?列出这些学生的名字,年龄,性别和职位
    select name,age,gender,job from student
    where age=7 and job='大队长';

  3.2 查看所有的大队长和中队长的数据;
    select name,job from student
    where job='大队长' or job='中队长';

  3.3 查看班级编号小于6的所有中队长都有谁?列出名字，年龄，性别，班级编号(class_id)，职位
    select name,age,gender,class_id,job from student
    where class_id<6 and job='中队长';

  3.4 查看所有一级讲师和三级讲师的名字，列出职称和工资
  select title,salary from teacher
  where title='一级讲师' or title='三级讲师';

  3.5 查看所有大队长，中队长和小队长的名字，性别，年龄和职位
  select name,gender,age,job from student
  where job='大队长' or job='中队长' or job='小队长';

  select title,salary from teacher
  where not (title='一级讲师' or title='二级讲师');

  3.6 查看班级编号在6(含)以下的所有大队长和中队长的名字，年龄，性别，班级编号和职位
    select name,age,gender,class_id,job from student
    where class_id<=6 and (job='大队长' or job='中队长');

4.比较运算符: between ... and ..., in not in, is null, is not null;
  4.1 查看所有在3-5层的班级都有哪些？列出班级名称和所在楼层
    select name,floor from class
    where floor between 3 and 5;

  4.2 查看除一级讲师和二级讲师之外的所有老师的名字，职称，工资
    select name,title,salary from teacher
    where title not in('一级讲师','二级讲师');

  4.3 查看除大队长，中队长，小队长的其他学生的名字，职位，性别，年龄
    select name,job,gender,age from student
    where job not in('大队长','中队长','小队长');
-- 练习**********
1. 查看负责课程编号(subject_id)为1的男老师都有谁?
  select name,gender,subject_id from teacher
  where subject_id=1 and gender='男';

2. 查看工资高于5000的女老师都有谁?
  select name,gender,salary from teacher
  where salary>=5000 and gender='女';

3. 查看工资高于5000的男老师或所有女老师的工资？
  select name,salary,gender from teacher
  where (salary>=5000 and gender='男') or gender='女';

4. 查看工资在4000到8000以外的老师及具体工资?
  select name,salary from teacher
  where salary not between 4000 and 8000;

5. 查看7-10岁的男同学的职位都有哪些?
  select name,age,gender,job from student
  where (age between 7 and 10) and gender='男';

6. 查看一级讲师和二级讲师的奖金(comm)是多少?
  select name,title,comm from teacher
  where title in('一级讲师','二级讲师');


-- *****模糊查询 ********************
5.模糊查询,where 字段名 like 表达式
  _:匹配任意一个字符
  %:匹配0到n个字符

  5.1 查询名字以"郭"结尾的学生姓名
    select name from student where name like '%郭';

  5.2 查询9-12岁里是"课代表"的学生信息
    select name,age,job from student
    where (age between 9 and 12) and job like '%课代表%';

  5.3 查询名字第二个字是"苗"的学生信息
    select name from student
    where name like '_苗%';

  5.4 查询姓"邱"的课代表都是谁?
    select name,job from student
    where name like '邱%' and job like '%课代表%';

-- ****别名*****************
  5.5 别名: as 别名
    select name as 姓名, job as 职位 from student
    where name like '邱%' and job like '%课代表%';

    select name 姓名, job 职位 from student s
    where name like '邱%' and job like '%课代表%';

-- ****排序******************
order by 字段名 asc|desc
1.查看老师的工资排名,从高到低
  select name,salary from teacher order by salary desc;

2.查看学生的生日,按照从远到近
  select name,birth from student order by birth asc;

3.查看7-10岁的学生信息,学生按照年龄从大到小排序(同年龄的看生日)
  select name,age,birth from student
  where age between 7 and 10
  order by age desc, birth;

4.查看老师的工资和奖金，首先按照奖金的升序，再按照工资的降序
  select name,salary,comm from teacher
  order by comm asc,salary desc;

-- *************分页查询******************
1. 查询8岁同学中名字含有"苗"的学生信息
  select name,age from student
  where age=8 and name like '%苗%';

2. 查询10岁以上的语文课代表和数学课代表
  select name,age,job from student
  where age>=10 and job in('语文课代表','数学课代表');

3. 查询不教课程编号1的老师信息,按照工资降序排序，显示前5名老师的数据
  select name,subject_id,salary from teacher
  where subject_id!=1
  order by salary desc
  limit 5;

4. 查询所有老师的奖金，并按照奖金降序排序，每页显示5条数据，显示第2页的数据
  select name,comm from teacher
  order by comm desc
  limit 5,5;