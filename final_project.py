#coding:gbk
"""
程序目标：基于Python和Gelphi的《黎明破晓的街道》人物关系图谱构建
程序作者：孙利娟
"""
import codecs
import jieba 
import os
from jieba import posseg
names = {}
relationship = {}
Names = []
jieba.load_userdict("character.txt")  # 加载人物表
with codecs.open("黎明破晓的街道.txt",'r','gbk')as f:
	lines = f.readlines()
	for line in lines:
		poss = jieba.posseg.cut(line)
		Names.append([])  # 增加人物列表
		for sun in poss:
			if sun.flag != 'nr' or len(sun.word)<2:
				continue
			Names[-1].append(sun.word)
			if names.get(sun.word) is None:  # 判断人物是否在字典中
				names[sun.word] = 0
				relationship[sun.word] = {}
			names[sun.word] += 1
for line in Names:
	for name_1 in line:
		for name_2 in line:
			if name_1 == name_2:
				continue
			if relationship[name_1].get(name_2)is None:
				relationship[name_1][name_2] = 1
			else:
				relationship[name_1][name_2] = relationship[name_1][name_2] + 1
# 生成对应文件
with codecs.open("node.txt",'w','utf-8')as f:
	f.write("ID Label Weight\r\n")
	for name,times in names.items():
		m = ['小姐','老公公','明白','东白乐','平安夜','滑雪','阿姨','宣言','仲西家','威士忌','红茶','阿嬷','封印','道德','温泉','高中生','白发 ','徐缓','藉口','老公','欧吉桑','高圆寺','富豪','时髦','高尔夫球','谢谢','原谅','浅笑','令尊','白发','顾忌','仲西']
		if name in m:
			continue
		if times > 3:
			f.write(name + " " + name + " " + str(times) + "\r\n")
with codecs.open("edge.txt","w","utf-8")as f:
	f.write("Source Target Weight\r\n")
	for name,edges in relationship.items():
		for a,b in edges.items():
			if b > 3:
				f.write(name + " " + a + " "+str(b) + "\r\n")
f1 = open('edge.txt','r',encoding='utf-8')
liness = f1.readlines()
f1.close
S = []
su = ['Source','Target','Weight','秋叶','新谷','黑泽','古琦','渡部','有美子','园美','丽子','野田','芦原','真穗','尾崎','妙子','里村','加岛','绫子','达彦','钉宫真纪子','英惠','绘理','阿俊']
for cha in liness:
	S.append([])
	c = cha.strip('\n').split(' ')
	for d in c:
		S[-1].append(d)
# 除去非人物名词
u = []
for i in range(0,len(S),1):
	if S[i][1] in su:
		if S[i][0] in su:
			u.append(S[i])
			f = open('edge.txt','w')
			for j in range(len(u)):
				s = str(u[j]).replace('[',' ').replace(']',' ')
				s = s.replace("'",' ').replace(',',' ')+'\n'
				f.write(s)
			f.close
	else:
		continue
