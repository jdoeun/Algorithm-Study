from collections import Counter


def solution(weights):
    answer = 0

    info = Counter(weights)

    for k, v in info.items():
        if v >= 2:
            answer += v * (v - 1) // 2

    weights = set(weights)

    for weight in weights:
        if weight * 2 / 3 in weights:
            answer += info[weight * 2 / 3] * info[weight]
        if weight * 2 / 4 in weights:
            answer += info[weight * 2 / 4] * info[weight]
        if weight * 3 / 4 in weights:
            answer += info[weight * 3 / 4] * info[weight]

    return answer

