from collections import Counter, defaultdict


def solution(s):
    answer = []
    s = s[2:len(s) - 2].split("},{")

    for x in s:
        x = list(map(int, x.split(",")))
        answer.append(x)

    answer.sort(key=lambda x: len(x))

    info = defaultdict(int)

    for a in answer:
        c = Counter(a)
        for k in c:
            info[k] = max(info[k], c[k])

    result = []

    for k in info:
        result.append(k)

    return result

