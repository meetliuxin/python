
print(json_str,data2)

#对文件操作
#写入json数据
with open('data.json','w') as f:
	json.dump(data,f)

#读取数据
with open('data.json','r') as f:
	data=json.load(f)
	



