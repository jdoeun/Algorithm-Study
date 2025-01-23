from math import gcd


def get_gcd(arr):
    result = arr[0]

    if len(arr) == 1:
        return result

    for i in range(1, len(arr)):
        result = gcd(result, arr[i])

    return result


def check(n, arr):
    if n == 1:
        return False
    for a in arr:
        if a % n == 0:
            return False
    return True


def solution(arrayA, arrayB):
    gcdA = get_gcd(arrayA)
    gcdB = get_gcd(arrayB)

    resultA = gcdA
    resultB = gcdB

    if not check(gcdA, arrayB):
        resultA = 0
    if not check(gcdB, arrayA):
        resultB = 0

    return max(resultA, resultB)

