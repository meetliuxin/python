#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: "liuxin"
# Date: 2018-5-16
#practice redis



#用python连接数据库
from redis import StrictRedis, ConnectionPool

# redis = StrictRedis(host='localhost',port=6379,db=0)
# redis.set('name','Bob')
# print(redis.get('name'))

#url = 'redis://password@host:port/db'
url = 'redis://@localhost:6379/0'  
pool = ConnectionPool.from_url(url)
redis = StrictRedis(connection_pool=pool)
redis.set('name','liuxin')
print(redis.get('name'))



基本操作:
打开服务端redis-server再开一个窗口打开客户端redis-cli 输入ping 返回pong则表示连接成功；
远程连接：redis-cli -h host -p port -a password
切换到db2数据库：select 2
清除当前数据库数据：flushdb

String（字符串）:
    set name 'liuxin'
    get name 
Hash（哈希）:
	hmset myhash field1 'hello' field2 'world'
	hget myhash field1
	hget myhash field2
List（列表）Redis 列表是简单的字符串列表:
	lpush mylist first
	lpush mylist second
	lpush mylist third
	lrange mylist 0 2
Set（集合）Redis的Set是string类型的无序集合。
集合是通过哈希表实现的，所以添加，删除，查找的复杂度都是O(1):
	(sadd key member)
	sadd myset v1
	sadd myset v2
	sadd myset v3
	sadd myset v4
	smembers myset
zset(sorted set：有序集合)
每个元素都会关联一个double类型的分数。redis正是通过分数来为集合中的成员进行从小到大的排序。
zset的成员是唯一的,但分数(score)却可以重复:
	(zadd key score member )
	zadd myzset 0 v0
	zadd myzset 1 v1
	zadd myzset 2 v2
	zadd myzset 3 v3
	zrangebyscore 0 3
五种数据结构更多操作参考　http://www.runoob.com/redis/redis-tutorial.html

Redis 键(key)   Redis 键命令用于管理 redis 的键:
	语法：COMMAND KEY_NAME
	set mykey liuxin
	get mykey
	更多命令参考　http://www.runoob.com/redis/redis-keys.html
	


	
	
	

	

















# Redis 是完全开源免费的，遵守BSD协议，是一个高性能的key-value数据库。
# Redis 与其他 key - value 缓存产品有以下三个特点：
# Redis支持数据的持久化，可以将内存中的数据保存在磁盘中，重启的时候可以再次加载进行使用。
# Redis不仅仅支持简单的key-value类型的数据，同时还提供list，set，zset，hash等数据结构的存储。
# Redis支持数据的备份，即master-slave模式的数据备份。

# 支持的数据结构:
# String: 字符串
# Hash: 散列
# List: 列表
# Set: 集合
# Sorted Set: 有序集合

# Redis配置文件中下面的参数来控制数据库总数：/etc/redis/redis.conf 文件中，有个配置项 databases = 16 //默认有16个数据库





#http://www.runoob.com/redis/redis-tutorial.html
