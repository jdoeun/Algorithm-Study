import math


def transform(num, p):
    tmp = ""
    while num:
        tmp = str(num % p) + tmp
        num //= p
    return tmp


def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def solution(n, k):
    n = transform(n, k)
    answer = 0

    n = n.split("0")

    for x in n:
        if len(x) == 0:
            continue
        if int(x) < 2:
            continue
        if is_prime(int(x)):
            answer += 1

    return answer

