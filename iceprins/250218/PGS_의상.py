from collections import defaultdict


def solution(clothes):
    answer = 1
    info = defaultdict(list)

    for c in clothes:
        info[c[1]].append(c[0])

    for v in info.values():
        answer *= (len(v) + 1)

    return answer - 1

