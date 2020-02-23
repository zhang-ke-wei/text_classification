import os

# fd = open("word_frequency_statistics_results\体育.txt", "r", encoding="utf-8")
#
# key = []
# value = []
# li = fd.readlines()
# for i in li:
#     temp = i[0:-1].split(",")
#     key.append(temp[0][1:-1])
#     value.append(int(temp[1]))
# print(key)
# print(value)
#
# fd.close()

# a = {"a": 1, "b": 2}
# b = {"c": 3, "d": 4}
# print({**a, **b})
# a.update(b)
# print(a)

# dictionary = {}
# for i in range(len(key)):
#     dictionary[key[i]] = 0
# dictionary["qqqqqq"] = 123
# print(dictionary.get("qqqqqq") == None)
# print(len(dictionary), key[10000], value[10000])

path = "word_frequency_statistics_results"
for file_txt in os.listdir("word_frequency_statistics_results"):
    path_txt = path + "/" + file_txt
    txt = open(path_txt, "r", encoding="utf-8")
    li = txt.readlines()
    fp_txt = open("classification_vector_dimension" + "/" + file_txt[0:-4] + "vector_dimension.txt", "w",
                  encoding="utf-8")
    lines = 0
    for i in li:
        temp = i[0:-1].split(",")
        # fp_txt.write(temp[1])
        fp_txt.write(temp[0][1:-1] + "\n")  # key.append(temp[0][1:-1])
        lines += 1
        if lines >= 50000:
            break
        # value.append(int(temp[1]))
    # print(key)
    # print(value)
    fp_txt.close()
    txt.close()
