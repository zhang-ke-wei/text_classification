import jieba
import os
import numpy as np


def tjcp(pathname, items):
    txt = open(pathname, "r", encoding='utf-8').read()
    words = jieba.lcut(txt)
    counts = {}
    for word in words:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word, 0) + 1
    items += list(counts.items())
    # items.sort(key=lambda x: x[1], reverse=True)
    # print(items)
    # for i in range(len(items)):
    #     word, count = items[i]
    # print(i, ":", word, "      ", count)
    # print("{0:<10}{1:>5}".format(word, count))
    return items


filePath = 'F:\\BaiduNetdiskDownload\\文本分类数据集\\THUCNews\\THUCNews\\财经'
for root, dirs, files in os.walk(filePath):
    print(root, dirs, files)

i = 0
li = []
for file in files:
    tjcp('F:\\BaiduNetdiskDownload\\文本分类数据集\\THUCNews\\THUCNews\\财经\\' + file, li)
    i += 1
    if i > 1:
        break
    print("{:.3f}%".format((i / len(files))) * 100)
li.sort(key=lambda x: x[1], reverse=True)
fb = open("jieguo.txt", "w", encoding="utf-8")
fb.write(str(li))
print(li)
# #  n维度向量夹角余弦计算
# AB = [1, 3, 4, 5]
# AC = [2, 4, 5, 9]
# a = np.array(AB)
# b = np.array(AC)
# print(a, b, a * b)
# print(np.sum(a * b))
# print(np.sqrt(np.sum(a * a)))
# print(np.sqrt(np.sum(b * b)))
# print(np.sqrt(np.sum(a * a)) * np.sqrt(np.sum(b * b)))
# print(np.sum(a * b) / (np.sqrt(np.sum(a * a)) * np.sqrt(np.sum(b * b))))
print("{:}")
