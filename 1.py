# -*- coding: UTF-8 -*-
data_lines = open(u'unicode.txt',encoding='gbk').readlines()
query_dict = {}

for line in data_lines[7:]: # 去掉头部无用信息
    l = line.strip().split()
    unicode_mark =chr(int(l[4],16))
    print(l[4],16)
    print(unicode_mark)
    print(line)
    bihua = l[6]
    query_dict[unicode_mark] = bihua

print(u'收录汉字个数:', len(data_lines))
for s in u'你好世界！':
    print(s, query_dict.get(s, -1))
