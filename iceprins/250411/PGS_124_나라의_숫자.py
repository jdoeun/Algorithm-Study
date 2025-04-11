def solution(n):
    answer = []
    while n:
        r = n % 3
        if r == 0:
            r = 4
            n -= 1
        answer.append(str(r))
        n //= 3
    return ''.join(answer[::-1])

