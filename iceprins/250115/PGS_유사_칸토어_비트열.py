def is_one(n):
    while n >= 5:
        if (n - 2) % 5 == 0:
            return False
        n //= 5

    return n != 2


def solution(n, l, r):
    answer = 0
    for l in range(l - 1, r):
        if is_one(l):
            answer += 1

    return answer

