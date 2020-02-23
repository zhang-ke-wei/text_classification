import os
from construct_text_feature_vector import construct_text_feature_vector
from construct_classification_feature_vector import get_feature_vector_of_text_type
from cosine_of_vector import cosineOfVector

text_type_feature_vector_list = []
cos_type_list = {}


def text_classification(file_path):
    text_type = ""
    max_cos = -1
    types = os.listdir('F:/BaiduNetdiskDownload/文本分类数据集/THUCNews/THUCNews/')
    # print(cos_type_list)
    text_feature_vector = construct_text_feature_vector(file_path)
    # print(len(text_feature_vector))
    # print(len(text_type_feature_vector_list[0]))
    # open("123.txt","w", encoding="utf8").write(str(text_type_feature_vector_list[0]))
    i = 0
    for vector in text_type_feature_vector_list:
        cos = cosineOfVector(list(vector), list(text_feature_vector.values()))
        cos_type_list[types[i]] = cos
        i += 1
    # print(cos_type_list)
    for i in cos_type_list.keys():
        if cos_type_list[i] > max_cos:
            max_cos = cos_type_list[i]
            text_type = i
        # max_cos = max(max_cos, cos_type_list[i])
    # print("max=", max_cos)
    cos_type_list.clear()
    return text_type
    # print(list(feature_vector.values()))


if __name__ == '__main__':
    misjudgement_num_of_type = []
    errorRate_list = []
    for i in os.listdir('F:/BaiduNetdiskDownload/文本分类数据集/THUCNews/THUCNews/'):
        print(i)
        feature_vector = get_feature_vector_of_text_type(i)
        text_type_feature_vector_list.append(feature_vector.values())
    # for i in os.listdir("F:/BaiduNetdiskDownload/文本分类数据集/THUCNews/THUCNews/娱乐/"):
    #     text_t = text_classification("F:/BaiduNetdiskDownload/文本分类数据集/THUCNews/THUCNews/娱乐/"+i)
    #     print(text_t)
    #     # print(cosineOfVector([1, 0], [0, 1]))
    dirs = "F:/BaiduNetdiskDownload/文本分类数据集/THUCNews/THUCNews/"
    for dir in os.listdir(dirs):
        print(dir)
        files = os.listdir(dirs + "/" + dir)
        print(dir)
        print("len({})={}".format(dir, len(files)))

        counter = 0
        misjudgement_num = 0
        for file in files:
            text_t = text_classification("F:/BaiduNetdiskDownload/文本分类数据集/THUCNews/THUCNews/" + dir + "/" + file)
            print(dir + "/" + file, "reality_type=", dir, " ", "test_type=", text_t, "isRight=", dir == text_t)
            if dir == text_t:
                pass
            else:
                misjudgement_num += 1
            counter += 1
            print("\r{:.3f}%".format((counter / 100) * 100), end="")  # 进度条
            if counter >= 100:
                break
        misjudgement_num_of_type.append(misjudgement_num)
    print(misjudgement_num_of_type)
