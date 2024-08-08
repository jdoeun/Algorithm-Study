import copy


def calculate(arr):
    for i in range(1, len(arr)):
        arr[i] = max(arr[i], arr[i] + arr[i - 1])


def solution(sequence):
    a = copy.deepcopy(sequence)
    b = copy.deepcopy(sequence)

    for i in range(len(sequence)):
        a[i] *= (-1) ** i
        b[i] *= (-1) ** (i + 1)

    calculate(a)
    calculate(b)

    return max(max(a), max(b))
