import jieba
import os


def word_frequency_statistics(text_type):
    filePath = 'F:/BaiduNetdiskDownload/文本分类数据集/THUCNews/THUCNews/' + text_type
    files = os.listdir(filePath)
    i = 0
    counts = {}
    for file in files:
        prefix_file_name = filePath
        txt = open(prefix_file_name + '/' + file, "r", encoding='utf-8').read()
        words = jieba.lcut(txt)
        for word in words:
            if len(word) == 1:
                continue
            else:
                counts[word] = counts.get(word, 0) + 1
        # items.sort(key=lambda x: x[1], reverse=True)
        # print(items)
        # for i in range(len(items)):
        #     word, count = items[i]
        # print(i, ":", word, "      ", count)
        # print("{0:<10}{1:>5}".format(word, count))

        i += 1
        # if i > 400:
        #     break

        print("\r{}词频统计:{:.5f}%".format(text_type, (i / len(files))) * 100, end="")  # 进度条
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)  # 词频排序
    fb = open("word_frequency_statistics_results/" + text_type + ".txt", "w", encoding="utf-8")
    for it in items:
        fb.write(str(it)[1:-1] + "\n")
        # print(it)
    print("")


if __name__ == '__main__':
    fp = 'F:/BaiduNetdiskDownload/文本分类数据集/THUCNews/THUCNews'
    print(os.listdir(fp))
    for i in os.listdir(fp):
        word_frequency_statistics(i)
