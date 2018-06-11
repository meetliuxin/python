#Json简介：Json，全名 JavaScript Object Notation，是一种轻量级的数据交换格式。
#Json最广泛的应用是作为AJAX中web服务器和客户端的通讯的数据格式。现在也常用于http请求中，所以对json的各种学习，是自然而然的事情。
#Python的官网网址：https://docs.python.org/2/library/json.html?highlight=json#module-json

#python中json常用方法：dumps loads 对字符串，dump load 对文件
#dump对python对象编码成json格式　　　load对json解码成python对象

import json
#对字符串操作
data={'a':1,'b':2,'c':3}
json_str=json.dumps(data)
data2=json.loads(json_str)
print(json_str,data2)

#对文件操作
#写入json数据
with open('data.json','w') as f:
	json.dump(data,f)

#读取数据
with open('data.json','r') as f:
	data=json.load(f)
	



