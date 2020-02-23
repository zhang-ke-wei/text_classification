import numpy as np


#  n维向量夹角余弦计算
def cosineOfVector(vectorA, vectorB):
    a = np.array(vectorA)
    b = np.array(vectorB)
    t1 = np.sum(a * b)
    t2 = np.sqrt(np.sum(a * a))
    t3 = np.sqrt(np.sum(b * b))
    cosine = t1 / (t2 * t3)
    return cosine


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
if __name__ == '__main__':
    AB = [1, 3, 4, 5]
    AC = [2, 4, 5, 9]
    print(cosineOfVector(AB, AC))
