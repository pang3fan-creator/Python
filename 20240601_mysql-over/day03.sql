-- ******聚合函数 *******************
avg() max() min() sum() count()

1.查看老师的平均工资是多少?
  select avg(salary) from teacher;

2.统计老师的数量?
  select count(name) total from teacher;

-- *******课堂练习*****************
1. 查看班级编号(class_id)为1的学生有多少人?
  select count(*) total from student where class_id=1;

2. 查看11岁的课代表总共多少人?
  select count(*) total from student
  where age=11 and job like '%课代表%';

3. 工资高于5000的老师中最低工资是多少?
  select min(salary) min_sal from teacher
  where salary>=5000;

4. 老师中"总监"的平均工资是多少?
  select avg(salary) avg_sal from teacher
  where title like '%总监%';

-- ************分组group by***************
*******单字段分组************

1.查看每种职位的老师平均工资是多少?
  select title, avg(salary) avg_sal from teacher
  group by title;

2.查看每个班级各多少人?
  select class_id, count(*) from student
  group by class_id;

3.查看男学生每种职位各多少人,以及最大生日和最小生日?按照职位数量排序,要前3名;
  select job, count(*) total, max(birth), min(birth) from student
  where gender='男'
  group by job
  order by total desc
  limit 0, 3;

*******多字段分组************
1.查看同班级同性别的学生分别多少人?
  1班 男 25人
  1班 女 20人
  2班 男 50人
  2班 女 52人
  select class_id,gender,count(*) from student
  group by class_id, gender;

2.查看每个班每种职位各多少人?
  select class_id, job, count(*) from student
  group by class_id, job;

-- **********having*************
1. 查看每个科目老师的平均工资?但是仅查看平均工资高于6000的那些.

  select subject_id, avg(salary) avg_sal from teacher
  group by subject_id
  having avg_sal>=6000;

2. 查看每个科目女老师的平均工资?但是仅查看平均工资高于6000的那些,排序后前2名;.
  select subject_id, avg(salary) avg_sal from teacher
  where gender='女'
  group by subject_id
  having avg_sal>6000
  order by avg_sal desc
  limit 0,2;

-- *******去重子句distinct***************
1. 查看老师的职称都有哪些?
  select distinct title from teacher;

2. 查看各年龄段的学生都有哪些职位?
  select distinct age,job from student;

-- **********子查询[嵌套查询]********************
1. 查看比范传奇工资高的老师都有谁?
  select name, salary from teacher
  where salary>(select salary from teacher where name='范传奇');

2. 查看哪些老师的工资是高于平均工资的?
  select name, salary from teacher
  where salary>(select avg(salary) from teacher);

3. 查看与"祝雷"和"李费水"在同一个班的学生都有谁?
  -- where id in (1,8)
  select name,class_id from student
  where class_id in(select class_id from student where name in('祝雷','李费水'));


create table u(
    uid int primary key auto_increment,
    uname varchar(20)
);
insert into u values(1,'赵丽颖');

create table o(
    oid int primary key auto_increment,
    state varchar(20),
    uid int,
    constraint ou_fk foreign key(uid) references u(uid)
);

insert into o values(1,'待付款',1);
insert into o values(2,'已付款',8);


1.restrict级联操作[默认]
  1.1 删除主表数据时，从表中如果有相关联的数据则不允许删除；
  1.2 更新主表主键字段时，从表中如果有相关联的数据则不允许更新；
alter table o drop foreign key ou_fk;
alter table o add constraint ou_fk foreign key(uid)
references u(uid) on delete restrict on update restrict;

2.cascade级联更新,级联删除
  2.1 当删除主表数据时，从表中相关联的数据全部删除；
  2.2 当更新主表主键字段时，从表中相关联的数据自动更新；
  alter table o drop foreign key ou_fk;
  alter table o add constraint ou_fk foreign key(uid)
references u(uid) on delete cascade on update cascade;

3.set null设置null值
  3.1 当删除或者更新主表主键字段时，从表中相关联的数据会设置为NULL;
  alter table o drop foreign key ou_fk;
  alter table o add constraint ou_fk foreign key(uid)
references u(uid) on delete set null on update set null;

-- 联合查询---------------------
1. 查看每个老师以及其负责课程科目名?
  select t.name, s.name from teacher t,subject s
  where s.id=t.subject_id;

2.王克晶是哪个班的班主任?列出:班级名称，楼层，老师名称，工资
  2.1 确定数据表 teacher class;
  2.2 确定连接条件 t.id=c.teacher_id;
  2.3 确定过滤条件 t.name='王克晶';
  select c.name,c.floor,t.name,t.salary from teacher t,class c
  where t.id=c.teacher_id
    and t.name='王克晶';

3. 查看三年级的班级班主任都是谁?要列出班级名称，所在楼层，班主任名字和工资
  3.1 确定数据表
  3.2 确定连接条件
  3.3 确定过滤条件
  select c.name,c.floor,t.name,t.salary from teacher t, class c
  where t.id=c.teacher_id
    and c.name like '%3年级%';

4. 查看来自南京的学生都有谁?要列出城市名字，学生名字，年龄，性别
  4.1 确定数据表
  4.2 确定连接条件
  4.3 确定过滤条件
  select l.name,s.name,s.age,s.gender from location l, student s
  where l.id=s.location_id
    and l.name='南京';

5. 查看5年级的中队长都有谁?要列出学生名字，年龄，性别，职位和所在班级的名字以及楼层
  select s.name,s.age,s.gender,s.job,c.name from class c,student s
  where c.id=s.class_id
    and c.name like '%5年级%'
    and s.job='中队长';

-- N张表连接-------------------
1. 查看"范传奇"所带班级的学生都有谁?要列出:学生名字，年龄，班级名称，老师名字
  select s.name,s.age,c.name,t.name from student s,class c,teacher t
  where c.id=s.class_id
    and t.id=c.teacher_id
    and t.name='范传奇';

2. 3年级的所有班主任都教哪些课程?
  select c.name,t.name,s.name from class c,teacher t,subject s
  where t.id=c.teacher_id
    and s.id=t.subject_id
    and c.name like '%3年级%';

3. 查看范传奇所带班级的学生共多少人?
  select count(*) from student s,class c,teacher t
  where c.id=s.class_id
    and t.id=c.teacher_id
    and t.name='范传奇';

4. 查看教每门课老师的平均工资是多少(GROUP BY)?列出平均工资和科目名称
  语文 8000
  英语 9000
  体育 5000
  select s.name,avg(t.salary) from subject s, teacher t
  where s.id=t.subject_id
  group by s.name;

5. 查看教每门课男老师的平均工资是多少(GROUP BY),
   只要平均工资高于4000的,按照工资排名,取出前三名,列出平均工资和科目名称;
  select s.name,avg(t.salary) avg_sal from subject s, teacher t
  where s.id=t.subject_id
    and t.gender='男'
  group by s.name
  having avg_sal>4000
  order by avg_sal desc
  limit 0,3;





