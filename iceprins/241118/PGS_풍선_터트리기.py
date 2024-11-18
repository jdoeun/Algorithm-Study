from copy import deepcopy


def solution(a):
    answer = 2

    left_min = deepcopy(a)
    right_min = deepcopy(a)

    for i in range(1, len(a)):
        left_min[i] = min(left_min[i - 1], a[i])

    for i in range(len(a) - 2, 0, -1):
        right_min[i] = min(right_min[i + 1], a[i])

    for i in range(1, len(a) - 1):
        if left_min[i - 1] < a[i] and right_min[i + 1] < a[i]:
            continue
        answer += 1

    return answer

