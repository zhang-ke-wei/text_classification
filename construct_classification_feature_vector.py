def get_dimension_and_frequency(file_path):
    fd = open(file_path, "r", encoding="utf-8")
    values = []
    keys = []
    sum_ = 0
    counter = 0
    li = fd.readlines()
    for i in li:
        temp = i[0:-1].split(",")
        keys.append(temp[0][1:-1])
        sum_ += int(temp[1])
        counter += 1
        if counter >= 50000:
            break
    counter = 0
    for i in li:
        temp = i[0:-1].split(",")
        values.append(int(temp[1]) / sum_)
        counter += 1
        if counter >= 50000:
            break
    # print(sum_)
    # open("123","w").write(str(values))
    return keys, values


def get_sun_vector_dimension():
    empty_vector_dict = {}
    path = "sun_vector/sum_vector.txt"
    fd = open(path, "r", encoding="utf8")
    dimensions = fd.readlines()
    for dimension in dimensions:
        empty_vector_dict[dimension[0:-1]] = empty_vector_dict.get(dimension[0:-1], 0)
    # print(empty_vector_dict)
    fd.close()
    return empty_vector_dict


def construct_classification_feature_vector(keys, values):
    vector = get_sun_vector_dimension()
    for i in range(len(keys)):
        if keys[i] in vector.keys():
            vector[keys[i]] = values[i]
    # print(vector)
    return vector


def get_feature_vector_of_text_type(text_type):
    file_path = "word_frequency_statistics_results/" + text_type + ".txt"
    keys, values = get_dimension_and_frequency(file_path)
    feature_vector = construct_classification_feature_vector(keys, values)
    return feature_vector


if __name__ == '__main__':
    print(get_feature_vector_of_text_type("体育"))
