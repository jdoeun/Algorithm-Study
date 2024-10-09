from collections import defaultdict


def solution(want, number, discount):
    answer = 0

    buy = dict()

    for i in range(len(want)):
        buy[want[i]] = number[i]

    for i in range(len(discount) - 9):
        info = defaultdict(int)
        flag = True
        for j in range(i, i + 10):
            info[discount[j]] += 1

        for fruit in buy:
            if buy[fruit] > info[fruit]:
                flag = False
                break
        if not flag:
            continue
        else:
            answer += 1

    return answer
