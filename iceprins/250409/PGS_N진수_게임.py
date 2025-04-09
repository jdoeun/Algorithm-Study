def transform(num, k):
    result = ""
    while num != 0:
        tmp = num % k
        if tmp == 10:
            result += "A"
        elif tmp == 11:
            result += "B"
        elif tmp == 12:
            result += "C"
        elif tmp == 13:
            result += "D"
        elif tmp == 14:
            result += "E"
        elif tmp == 15:
            result += "F"
        else:
            result += str(num % k)
        num //= k
    return result[::-1]


def solution(n, t, m, p):
    answer = ''
    cand = "0"

    for i in range(t * m):
        cand += transform(i, n)

    cand = list(cand)

    while t > 0:
        answer += cand[p - 1]
        p += m
        t -= 1

    return answer

