import math


def solution(brown, yellow):
    answer = []
    cand = []

    for n in range(1, math.floor(math.sqrt(yellow)) + 1):
        if yellow % n == 0:
            q = yellow // n
            cand.append((n, q))

    for pair in cand:
        tmp = 2 * (sum(pair)) + 4
        if tmp == brown:
            answer.append(pair[0] + 2)
            answer.append(pair[1] + 2)
            break

    answer.sort(reverse=True)

    return answer
