import re


#match()方法会尝试从字符串的起始位置匹配正则表达式，如果匹配，就返回匹配成功的结果；如果不匹配，就返回None
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^Hello\s(\d+)\sWorld', content)
print(result)
print(result.group())
print(result.group(1))
print(result.span())



#贪婪非贪婪
content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*(\d+).*Demo$', content)
print(result)
print(result.group(1))　　#结果：７

content = 'Hello 1234567 World_This is a Regex Demo'
result = re.match('^He.*?(\d+).*Demo$', content)
print(result)
print(result.group(1))　　#结果：1234567


#修饰符
#re.I 使匹配对大小写不敏感
#re.S 使.匹配包括换行在内的所有字符

content = '''Hello 1234567 World_This
is a Regex Demo
'''
result = re.match('^He.*?(\d+).*?Demo$', content，re.S)#因为\.匹配的是除换行符之外的任意字符，当遇到换行符时，.*?就不能匹配了
print(result.group(1))  #result是一个正则对象，group()方法取得其中的字符串




#search()，它在匹配时会扫描整个字符串，然后返回第一个成功匹配的结果。也就是说，正则表达式可以是字符串的一部分.返回的是一个正则对象．

#findall()　该方法会搜索整个字符串，然后返回匹配正则表达式的所有内容。返回的列表中的每个元素都是元组类型，我们用对应的索引依次取出即可

#sub 想要把一串文本中的所有数字都去掉，如果只用字符串的replace()方法，那就太烦琐了，这时可以借助sub()方法
content = '54aK54yr5oiR54ix5L2g'
content = re.sub('\d+', '', content)
print(content)

#compile 这个方法可以将正则字符串编译成正则表达式对象，以便在后面的匹配中复用。compile()还可以传入修饰符
content1 = '2016-12-15 12:00'
content2 = '2016-12-17 12:55'
content3 = '2016-12-22 13:21'
pattern = re.compile('\d{2}:\d{2}')
result1 = re.sub(pattern, '', content1)
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)
print(result1, result2, result3)
















#http://www.runoob.com/regexp/regexp-syntax.html

#http://www.runoob.com/python/python-reg-expressions.html


#https://cuiqingcai.com/5530.html
