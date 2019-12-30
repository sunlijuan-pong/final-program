#coding:gbk
"""
����Ŀ�꣺����Python��Gelphi�ġ����������Ľֵ��������ϵͼ�׹���
�������ߣ�������
"""
import codecs
import jieba 
import os
from jieba import posseg
names = {}
relationship = {}
Names = []
jieba.load_userdict("character.txt")  # ���������
with codecs.open("���������Ľֵ�.txt",'r','gbk')as f:
	lines = f.readlines()
	for line in lines:
		poss = jieba.posseg.cut(line)
		Names.append([])  # ���������б�
		for sun in poss:
			if sun.flag != 'nr' or len(sun.word)<2:
				continue
			Names[-1].append(sun.word)
			if names.get(sun.word) is None:  # �ж������Ƿ����ֵ���
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
# ���ɶ�Ӧ�ļ�
with codecs.open("node.txt",'w','utf-8')as f:
	f.write("ID Label Weight\r\n")
	for name,times in names.items():
		m = ['С��','�Ϲ���','����','������','ƽ��ҹ','��ѩ','����','����','������','��ʿ��','���','����','��ӡ','����','��Ȫ','������','�׷� ','�컺','���','�Ϲ�','ŷ��ɣ','��Բ��','����','ʱ��','�߶�����','лл','ԭ��','ǳЦ','����','�׷�','�˼�','����']
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
su = ['Source','Target','Weight','��Ҷ','�¹�','����','����','�ɲ�','������','԰��','����','Ұ��','«ԭ','����','β��','����','���','�ӵ�','���','����','���������','Ӣ��','����','����']
for cha in liness:
	S.append([])
	c = cha.strip('\n').split(' ')
	for d in c:
		S[-1].append(d)
# ��ȥ����������
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
