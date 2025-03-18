from collections import Counter


def solution(str1, str2):
    str1 = str1.upper()
    str2 = str2.upper()

    a_set = []
    b_set = []

    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            a_set.append(str1[i] + str1[i + 1])
    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            b_set.append(str2[i] + str2[i + 1])

    if not a_set and not b_set:
        return 65536

    Counter1 = Counter(a_set)
    Counter2 = Counter(b_set)

    intersection = list((Counter1 & Counter2).elements())
    union = list((Counter1 | Counter2).elements())

    return int(len(intersection) / len(union) * 65536)

