
create table books(
  id INT UNSIGNED NOT NULL KEY AUTO_INCREMENT,
  bookname VARCHAR(20) NOT NULL,
  category VARCHAR(20) NOT NULL
);

INSERT books(bookname,category) VALUES('A','计算机');
INSERT books(bookname,category) VALUES('B','历史');
INSERT books(bookname,category) VALUES('C','计算机');
INSERT books(bookname,category) VALUES('D','记传');
INSERT books(bookname,category) VALUES('E','传记');
INSERT books(bookname,category) VALUES('F','计算机');
INSERT books(bookname,category) VALUES('G','历史');
INSERT books(bookname,category) VALUES('H','计算机');
INSERT books(bookname,category) VALUES('I','历史');
INSERT books(bookname,category) VALUES('J','计算机');

-- books数据表中的category字段冗余,缺少外键数据表，

-- 1.创建外键数据表

---- 方法1:通过CREATE TABLE ... SELECT 方法同时创建数据表并且数据写入

CREATE TABLE category1(id SMALLINT UNSIGNED NOT NULL KEY AUTO_INCREMENT) SELECT category FROM books GROUP BY category;

---- 方法2:先通过CREATE TABLE创建数据表，再通过INSERT...SELECT进行记录插入

CREATE TABLE category2(
	id SMALLINT UNSIGNED NOT NULL KEY AUTO_INCREMENT,
	name VARCHAR(20) NOT NULL
);

INSERT category2(name) SELECT category FROM books GROUP BY category;


-- 2.通过参照分类表(category1或category2)来更新图书表(books)


UPDATE books AS b  INNER JOIN category1 AS c ON b.category = c.category 

SET b.category = c.id;


-- 3.修改books数据表category字段的名称及数据类型

ALTER TABLE books CHANGE category category_id SMALLINT UNSIGNED NOT NULL;



-- 面试题:删除test1数据表名name相同的记录，保留ID号较小的记录

CREATE TABLE test1(
	 id SMALLINT UNSIGNED NOT NULL KEY AUTO_INCREMENT,
	 name VARCHAR(10)
);

INSERT test1(name) VALUES('a');
INSERT test1(name) VALUES('b');
INSERT test1(name) VALUES('a');
INSERT test1(name) VALUES('c');
INSERT test1(name) VALUES('e');
INSERT test1(name) VALUES('c');
INSERT test1(name) VALUES('e');
INSERT test1(name) VALUES('b');
INSERT test1(name) VALUES('a');
INSERT test1(name) VALUES('a');