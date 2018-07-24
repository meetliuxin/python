#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: "liuxin"
# Date: 2018-6-16

#mysql笔记

#参考：http://www.runoob.com/mysql/mysql-tutorial.html



ubuntu下service mysql start开启服务端另开一个窗口mysql -u root -p 输入密码开始:
show databases;
show tables;
use db_name;
#创建数据库：
	create database mytest;
#使用数据库：	
	use mytest;
#创建表：	
	create table student (id int(10) primary key, name char(40) not null)engine=innodb,charset=utf8;
#删除数据库：
	drop database mytest;
#插入数据:
	INSERT INTO table_name ( field1, field2,...fieldN )
                       VALUES
                       ( value1, value2,...valueN ),
				    	(value1, value2,...valueN);
	可以一次插入多条　
	只插一条也可:insert into student values (1,'liuxin');
#查询数据：
		SELECT column_name,column_name
		FROM table_name
		[WHERE Clause]
		[LIMIT N][ OFFSET M]
		select * from student where id=2;
#更新数据：
	UPDATE table_name SET field1=new-value1, field2=new-value2
	[WHERE Clause]
#删除数据：
	DELETE FROM table_name [WHERE Clause]
#like:
	SELECT field1, field2,...fieldN 
	FROM table_name
	WHERE field1 LIKE condition1 [AND [OR]] filed2 = 'somevalue'
	
	select * from student where name like '%xin';
#union:
	MySQL UNION 操作符用于连接两个以上的 SELECT 语句的结果组合到一个结果集合中。多个 SELECT 语句会删除重复的数据.类似Ｐｙｔｈｏｎ的ｓｅｔ(集合）
	SELECT expression1, expression2, ... expression_n
	FROM tables
	[WHERE conditions]
	UNION [ALL | DISTINCT]
	SELECT expression1, expression2, ... expression_n
	FROM tables
	[WHERE conditions];
	ALL: 可选，返回所有结果集，包含重复数据
#排序：
	SELECT field1, field2,...fieldN table_name1, table_name2...
	ORDER BY field1, [field2...] [ASC [DESC]]
		
	select * from student order by id asc;
	asc升序,desc降序
#分组：
	SELECT column_name, function(column_name)
	FROM table_name
	WHERE column_name operator value
	GROUP BY column_name;

	+----+--------+---------------------+--------+
| id | name   | date                | singin |
+----+--------+---------------------+--------+
|  1 | 小明 | 2016-04-22 15:25:33 |      1 |
|  2 | 小王 | 2016-04-20 15:25:47 |      3 |
|  3 | 小丽 | 2016-04-19 15:26:02 |      2 |
|  4 | 小王 | 2016-04-07 15:26:14 |      4 |
|  5 | 小明 | 2016-04-11 15:26:40 |      4 |
|  6 | 小明 | 2016-04-04 15:26:54 |      2 |
+----+--------+---------------------+--------+
SELECT name, COUNT(*) FROM   employee_tbl GROUP BY name;
+--------+----------+
| name   | COUNT(*) |
+--------+----------+
| 小丽 |        1 |
| 小明 |        3 |
| 小王 |        2 |
+--------+----------+
使用 WITH ROLLUP
WITH ROLLUP 可以实现在分组统计数据基础上再进行相同的统计（SUM,AVG,COUNT…）。
SELECT name, SUM(singin) as singin_count FROM  employee_tbl GROUP BY name WITH ROLLUP;
+--------+--------------+
| name   | singin_count |
+--------+--------------+
| 小丽 |            2 |
| 小明 |            7 |
| 小王 |            7 |
| NULL   |           16 |
+--------+--------------+
我们可以使用 coalesce 来设置一个可以取代 NUll 的名称，coalesce 语法：

select coalesce(a,b,c);
参数说明：如果a==null,则选择b；如果b==null,则选择c；如果a!=null,则选择a；如果a b c 都为null ，则返回为null（没意义）
SELECT coalesce(name, '总数'), SUM(singin) as singin_count FROM  employee_tbl GROUP BY name WITH ROLLUP;
+--------------------------+--------------+
| coalesce(name, '总数') | singin_count |
+--------------------------+--------------+
| 小丽                   |            2 |
| 小明                   |            7 |
| 小王                   |            7 |
| 总数                   |           16 |
+--------------------------+--------------+

连接查询join:
	INNER JOIN（内连接,或等值连接）：获取两个表中字段匹配关系的记录。
	LEFT JOIN（左连接）：获取左表所有记录，即使右表没有对应匹配的记录。
	RIGHT JOIN（右连接）： 与 LEFT JOIN 相反，用于获取右表所有记录，即使左表没有对应匹配的记录。
	

	SELECT a.runoob_id, a.runoob_author, b.runoob_count FROM runoob_tbl a INNER JOIN tcount_tbl b ON a.runoob_author = b.runoob_author;
	SELECT a.runoob_id, a.runoob_author, b.runoob_count FROM runoob_tbl a, tcount_tbl b WHERE a.runoob_author = b.runoob_author;

NULL 值处理:
	MySQL 使用 SQL SELECT 命令及 WHERE 子句来读取数据表中的数据,但是当提供的查询条件字段为 NULL 时，该命令可能就无法正常工作。
	MySQL提供了三大运算符:
	IS NULL: 当列的值是 NULL,此运算符返回 true。
	IS NOT NULL: 当列的值不为 NULL, 运算符返回 true。
	<=>: 比较操作符（不同于=运算符），当比较的的两个值为 NULL 时返回 true。
	SELECT * FROM runoob_test_tbl WHERE runoob_count IS NULL;
	SELECT * from runoob_test_tbl WHERE runoob_count IS NOT NULL;



MySQL ALTER命令:
	删除，添加或修改表字段
	alter table runoob_tbl drop i;  删除i字段
	ALTER TABLE testalter_tbl ADD i INT;　添加字段
	
	ALTER TABLE testalter_tbl MODIFY c CHAR(10);把字段 c 的类型从 CHAR(1) 改为 CHAR(10)
	使用 CHANGE 子句, 语法有很大的不同。 在 CHANGE 关键字之后，紧跟着的是你要修改的字段名，然后指定新字段名及类型
	ALTER TABLE testalter_tbl CHANGE i j BIGINT;
	ALTER TABLE testalter_tbl CHANGE j j INT;

	当你修改字段时，你可以指定是否包含值或者是否设置默认值。以下实例，指定字段 j 为 NOT NULL 且默认值为100 。
	 ALTER TABLE testalter_tbl MODIFY j BIGINT NOT NULL DEFAULT 100;
	ALTER TABLE testalter_tbl ALTER i SET DEFAULT 1000; 设置默认值

	ALTER TABLE testalter_tbl ALTER i DROP DEFAULT;使用 ALTER 命令及 DROP子句来删除字段的默认值
	ALTER TABLE testalter_tbl RENAME TO alter_tbl；修改表名
































MySQL 事务:
	在 MySQL 中只有使用了 Innodb 数据库引擎的数据库或表才支持事务。
事务处理可以用来维护数据库的完整性，保证成批的 SQL 语句要么全部执行，要么全部不执行。
事务用来管理 insert,update,delete 语句
一般来说，事务是必须满足4个条件（ACID）：：原子性（Atomicity，或称不可分割性）、一致性（Consistency）、隔离性（Isolation，又称独立性）、持久性（Durability）。

原子性：一个事务（transaction）中的所有操作，要么全部完成，要么全部不完成，不会结束在中间某个环节。事务在执行过程中发生错误，会被回滚（Rollback）到事务开始前的状态，就像这个事务从来没有执行过一样。

一致性：在事务开始之前和事务结束以后，数据库的完整性没有被破坏。这表示写入的资料必须完全符合所有的预设规则，这包含资料的精确度、串联性以及后续数据库可以自发性地完成预定的工作。

隔离性：数据库允许多个并发事务同时对其数据进行读写和修改的能力，隔离性可以防止多个事务并发执行时由于交叉执行而导致数据的不一致。事务隔离分为不同级别，包括读未提交（Read uncommitted）、读提交（read committed）、可重复读（repeatable read）和串行化（Serializable）。

持久性：事务处理结束后，对数据的修改就是永久的，即便系统故障也不会丢失。


在 MySQL 命令行的默认设置下，事务都是自动提交的，即执行 SQL 语句后就会马上执行 COMMIT 操作。因此要显式地开启一个事务务须使用命令 BEGIN 或 START TRANSACTION，或者执行命令 SET AUTOCOMMIT=0，用来禁止使用当前会话的自动提交。




MySQL有多种存储引擎，每种存储引擎有各自的优缺点，可以择优选择使用：MyISAM、InnoDB、MERGE、MEMORY(HEAP)、BDB(BerkeleyDB)、EXAMPLE、FEDERATED、ARCHIVE、CSV、BLACKHOLE。
虽然MySQL里的存储引擎不只是MyISAM与InnoDB这两个，但常用的就是两个。

1. 区别：

（1）事务处理：

MyISAM是非事务安全型的，而InnoDB是事务安全型的（支持事务处理等高级处理）；

（2）锁机制不同：

MyISAM是表级锁，而InnoDB是行级锁；

（3）select ,update ,insert ,delete 操作：

MyISAM：如果执行大量的SELECT，MyISAM是更好的选择
InnoDB：如果你的数据执行大量的INSERT或UPDATE，出于性能方面的考虑，应该使用InnoDB表
（4）查询表的行数不同：

MyISAM：select count(*) from table,MyISAM只要简单的读出保存好的行数，注意的是，当count(*)语句包含   where条件时，两种表的操作是一样的
InnoDB ： InnoDB 中不保存表的具体行数，也就是说，执行select count(*) from table时，InnoDB要扫描一遍整个表来计算有多少行
（5）外键支持：
mysiam表不支持外键，而InnoDB支持
2. 为什么MyISAM会比Innodb 的查询速度快。

INNODB在做SELECT的时候，要维护的东西比MYISAM引擎多很多；
1）数据块，INNODB要缓存，MYISAM只缓存索引块，  这中间还有换进换出的减少； 
2）innodb寻址要映射到块，再到行，MYISAM 记录的直接是文件的OFFSET，定位比INNODB要快
3）INNODB还需要维护MVCC一致；虽然你的场景没有，但他还是需要去检查和维护
MVCC ( Multi-Version Concurrency Control )多版本并发控制 
3. 应用场景
MyISAM适合：(1)做很多count 的计算；(2)插入不频繁，查询非常频繁；(3)没有事务。

InnoDB适合：(1)可靠性要求比较高，或者要求事务；(2)表更新和查询都相当的频繁，并且行锁定的机会比较大的情况。

