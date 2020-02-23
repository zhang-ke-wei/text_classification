import jieba
from construct_classification_feature_vector import construct_classification_feature_vector


def construct_text_feature_vector(file_path):
    counts = {}
    keys = []
    values = []
    word_sum = 0
    counter = 0
    fd = open(file_path, "r", encoding="utf8")
    txt = fd.read()
    words = jieba.lcut(txt)
    for word in words:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word, 0) + 1
    fd.close()
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)  # 词频排序
    # print(len(items))
    for i in items:
        word_sum += i[1]
    for i in items:
        # print(i[0], i[1], counter)
        keys.append(i[0])
        values.append(i[1] / word_sum)
        counter += 1
        if counter >= len(items) // 2:
            break
    feature_vector_dict = construct_classification_feature_vector(keys, values)
    # print(values)
    return feature_vector_dict


if __name__ == '__main__':
    li = construct_text_feature_vector("F:/BaiduNetdiskDownload/文本分类数据集/THUCNews/THUCNews/财经/798990.txt")
# for i in li:
#     temp = i[0:-1].split(",")
#     keys.append(temp[0][1:-1])
#     sum_ += int(temp[1])
#     counter += 1
#     if counter >= 50000:
#         break
# counter = 0
# for i in li:
#     temp = i[0:-1].split(",")
#     values.append(int(temp[1]) / sum_)
#     counter += 1
#     if counter >= 50000:
#         break
