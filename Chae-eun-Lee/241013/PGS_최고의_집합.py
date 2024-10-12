import math

def solution(n, s):
    answer = []
    if s < n:
        return [-1]
    for i in range(n-1):
        c = math.ceil(s/(n-i))
        answer.append(c)
        s -= c
    answer.append(s)
    answer.sort()
    return answer