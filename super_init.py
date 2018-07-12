#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: "liuxin"
# Date: 2018-7-12


#1、单继承时super()和__init__()实现的功能是类似的
#使用super()继承时不用显式引用基类
class Parent():
	def __init__(self):
		print('Parent creat')

class ChildA(Parent):
	def __init__(self):
		print('ChildA creat')
		Parent.__init__(self)

class ChildB(Parent):
	def __init__(self):
		print('ChildB creat')
		super(ChildB,self).__init__()


p = Parent()
a = ChildA()
b = ChildB()
print('***************************')



#2、super()只能用于新式类中
#3、super不是父类，而是继承顺序的下一个类
#4、super()可以避免重复调用
#https://my.oschina.net/jhao104/blog/682322



