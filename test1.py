#!/usr/bin/env python
#coding=utf-8

import gensim
import os, re, sys

# model = gensim.models.Word2Vec.load("wiki.zh.text.model")

# result = model.most_similar(u"男人")
j=0
k=0
model = gensim.models.Word2Vec.load("wiki.zh.text.model")

with open("aixiaoke_01_vector.txt", "w") as vec_file:

    for line in open("aixiaoke_01.txt"):
            words = line.split()
            for word in words:
                strWord = word.decode("utf-8")
                if strWord in model.vocab:
                    j = j+1
                    # print word
                    # print model[strWord]
                    strVec = model[strWord].tolist()
                    vec_file.write(str(strVec))
                    vec_file.write('\n')
                else:
                    k = k+1
    print  j, k


# for e in result:
# 	print e[0], e[1]

#输出在向量空间里指定词的向量表示
# word = u"月"
# print word
# vec = model[word]
# print vec

#去掉词向量文本中的所有"[,]"
# def is_ustr_sp(in_str):
#     out_str=''
#     for i in range(len(in_str)):
#         if is_uchar(in_str[i]):
#             out_str=out_str+in_str[i]
#         else:
#             out_str=out_str+' '
#     return out_str

# def is_uchar_sp(uchar):

#     #判断一个unicode是否是“[ ] ,”
#     if uchar == '[':
#         return False
#     else:
#     	if uchar == ']':
#     		return False
#     	else:
#     		if uchar == ',':
#     			return False
#     		else:
#     			return True

# with open('guofang_vecInput.txt', 'w') as file_obj:
# 	for line in file("guofang_vec.txt"):
# 		outStr = is_ustr(line.decode('utf-8'))
# 		file_obj.write(outStr.encode('utf-8'))




# result = model.similarity(u"男人", u"女人")

# print result