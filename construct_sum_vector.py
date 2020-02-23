import os

counter = 0
vector_dimensions = set()
directory = "classification_vector_dimension"
for filename in os.listdir(directory):
    fd = open(directory + "/" + filename, "r", encoding="utf-8")
    keys = fd.readlines()
    for key in keys:
        vector_dimensions.add(key[0:-1])
        counter += 1
    fd.close()
print(vector_dimensions)

fp = open("sun_vector/sum_vector.txt", "w", encoding="utf-8")
for dimension in vector_dimensions:
    fp.write(dimension + "\n")
    print(dimension)
fp.close()
# print(len(vector_dimensions))
# print(counter)
