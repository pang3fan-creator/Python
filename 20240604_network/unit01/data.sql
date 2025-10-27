CREATE DATABASE IF NOT EXISTS words;

USE words;

CREATE TABLE words(
	id INT UNSIGNED NOT NULL KEY AUTO_INCREMENT,
	apiname VARCHAR(50) NOT NULL,
	description MEDIUMTEXT NOT NULL
);

INSERT words(apiname,description) VALUES('print','功能:打印信息;语法:print(message)');
INSERT words(apiname,description) VALUES('str','功能:转换为字符串;语法:str(data)');
INSERT words(apiname,description) VALUES('len','功能:获取字符串的长度或列表成员的数量;语法:len(str|list)');
INSERT words(apiname,description) VALUES('int','功能:转换为整数;语法:int(data)');
INSERT words(apiname,description) VALUE('list','功能:转换为列表;语法:list(data)');

INSERT words(apiname,description) VALUE
('dict','功能:转换为字典;语法:dict(data)'),
('range','功能:产生指定的数值迭代器;语法:range(data)');


create table authors(id int unsigned not null primary key auto_increment,
name varchar(50) not null);

create table category(
id int unsigned not null primary key auto_increment,
name varchar(50) not null unique key);

create table article(
id int unsigned not null primary key auto_increment comment '文章id',
subject varchar(50) not null comment '文章标题',
context MEDIUMTEXT not null comment '文章内容',
author_id int unsigned not null comment '外键作者id',
category_id int unsigned not null comment '外键分类id'
is_delete boolean not null default 0 comment '逻辑删除',
);