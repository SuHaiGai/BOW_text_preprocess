#!/usr/bin/env python
#coding=utf-8

"""
INSTRUCTIONS

python convert_to_vec.py --source=<author>

For example:

    python convert_to_vec.py --source=aixiaoke

will convert documents within ./data/collins into respective VECTOR translated
documents

Output:
./data/<auth>_vecInput with vec text files
"""

import gensim
import os, re, sys
import jieba



def get_paths(directory_name):
    return ['./data/{0}/{1}'.format(directory_name, i)
            for i in os.listdir('./data/{0}/'.format(directory_name))
            if i != '.DS_Store']

#先过滤掉文本中的数字,同时保留词间的空格和换行符

def is_ustr(in_str):
    out_str=''
    for i in range(len(in_str)):
        if is_uchar(in_str[i]):
            out_str=out_str+in_str[i]
        # else:
        #     out_str=out_str+' '
    return out_str

def is_uchar(uchar):

    #判断一个unicode是否是汉字
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
            return True
    #判断一个unicode是否是数字,是数字则过滤掉
    if uchar >= u'\u0030' and uchar<=u'\u0039':
            return False
    #判断一个unicode如果是英文字母，则过滤掉
    if (uchar >= u'\u0041' and uchar<=u'\u005a') or (uchar >= u'\u0061' and uchar<=u'\u007a'):
            return False
    if uchar in ('\n', ' '):
            return True
    return False

#去掉词向量文本中的所有"[,]"
def is_ustr_sp(in_str):
    out_str=''
    for i in range(len(in_str)):
        if is_uchar_sp(in_str[i]):
            out_str=out_str+in_str[i]
        else:
            out_str=out_str+' '
    return out_str

def is_uchar_sp(uchar):

    #判断一个unicode是否是“[ ] ,”
    if uchar == '[':
        return False
    else:
        if uchar == ']':
            return False
        else:
            if uchar == ',':
                return False
            else:
                return True

def convert_to_vec(input_directory_name):
    output_directory = './data/{0}_vec'.format(input_directory_name)
    seg_directory = './data/{0}_seg'.format(input_directory_name)
    seg_chins_directory = './data/{0}_seg_chins'.format(input_directory_name)
    vecInput_directory = './data/{0}_vecInput'.format(input_directory_name)
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    if not os.path.exists(seg_directory):
        os.makedirs(seg_directory)
    if not os.path.exists(seg_chins_directory):
        os.makedirs(seg_chins_directory)
    if not os.path.exists(vecInput_directory):
        os.makedirs(vecInput_directory)

    input_paths = get_paths(input_directory_name)
    #统计词向量转换时词典的缺词率
    k=0
    j=0
    for path in input_paths:
        print 'converted {0}'.format(path)
        f = open(path)
        f_seg = open('./data/{0}_seg/{1}'.format(input_directory_name,
                                                 path.split('/')[-1]), 'wb')
        #对原始文本进行分词
        for line in f:
            words = jieba.cut(line)
            for word in words:
                # print word, flag
                f_seg.write(word.encode("utf-8"))
                f_seg.write(" ")
            # if line.strip().split() !="": #去除字符串两端的空格后，判断该行是否还有非空字符内容
            #     li = line.strip().split()
            #     words = pseg.cut(li)
            #     for word, flag in words:
            #         print ('%s %s' % (word, flag))
            #         str = flag + ' '
            #         f_pos.write(str.upper())
        f_seg.flush()
        f_seg.close()
        f.close()
        #分词之后，去掉文本中的非中文字符
        f_seg_chins = open('./data/{0}_seg_chins/{1}'.format(input_directory_name,
                                                 path.split('/')[-1]), 'wb')
        f_segT = open('./data/{0}_seg/{1}'.format(input_directory_name,
                                                 path.split('/')[-1]), 'r')
        for line in f_segT:
            outStr = is_ustr(line.decode('utf-8'))
            f_seg_chins.write(outStr.encode('utf-8'))
        f_segT.close()
        f_seg_chins.close()


        #对文本进行词向量转换
        model = gensim.models.Word2Vec.load("wiki.zh.text.model")
        f_seg_chinsT = open('./data/{0}_seg_chins/{1}'.format(input_directory_name,
                                                 path.split('/')[-1]), 'r')
        vec_file = open('./data/{0}_vec/{1}'.format(input_directory_name,
                                                 path.split('/')[-1]), 'w')
        for line in f_seg_chinsT:
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
        #最后过滤词向量文本中的“[  ]   ,” ，生成下一步 BOW 模型的可接收文本
        vec_file.close()
        f_seg_chinsT.close()

        vec_fileT = open('./data/{0}_vec/{1}'.format(input_directory_name,
                                                 path.split('/')[-1]), 'r')
        with open('./data/{0}_vecInput/{1}'.format(input_directory_name,
                                                 path.split('/')[-1]), 'w') as file_obj:
            for line in vec_fileT:
                outStr = is_ustr_sp(line.decode('utf-8'))
                file_obj.write(outStr.encode('utf-8'))

        vec_fileT.close()


if __name__ == '__main__':
    source = sys.argv[1].replace('--source=', '')
    convert_to_vec(source)








