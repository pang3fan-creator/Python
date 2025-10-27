-- ********多对多查询*************
1.查看学习语文的学生都有谁，列出学生姓名、科目名称、学生成绩?
  select s.name,su.name,sc.score from student s, subject su, t_stu_subject_score sc
  where s.id=sc.stu_id
    and su.id=sc.subject_id
    and su.name='语文';

2. 查看1年级1班所有同学的语文成绩是多少?
  select c.name,s.name,sc.score from class c, student s, t_stu_subject_score sc, subject su
  where c.id=s.class_id
    and s.id=sc.stu_id
    and su.id=sc.subject_id
    and c.name='1年级1班'
    and su.name='语文';

3. 统计6年级的英语成绩的平均值?
   round(浮点数,小数位位数) : 保留n位小数位;
  select round(avg(sc.score),2) from class c, student s, t_stu_subject_score sc, subject su
  where c.id=s.class_id
    and s.id=sc.stu_id
    and su.id=sc.subject_id
    and c.name like '%6年级%'
    and su.name='英语';


-- **********连接查询******************
1.查看1年级1班的学生信息?列出学生名字,年龄,所在班级
  select s.name,s.age,c.name from class c
      join student s on c.id=s.class_id
  where c.name='1年级1班';

2.查看1年级1班所有同学的语文成绩是多少?
  select c.name,s.name,su.name,sc.score from class c
  join student s on c.id=s.class_id
  join t_stu_subject_score sc on s.id=sc.stu_id
  join subject su on su.id=sc.subject_id
  where c.name='1年级1班'
    and su.name='语文';

-- ****索引创建********************
create database if not exists day04db charset=utf8;
use day04db;
create table user(
    id int primary key auto_increment,
    username varchar(20),
    password varchar(20),
    nickname varchar(20),
    index nickIndex(nickname),
    unique userIndex(username)
);





