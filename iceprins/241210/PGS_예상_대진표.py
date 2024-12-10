def solution(n, a, b):
    answer = 0

    while True:
        answer += 1

        if abs(a - b) == 1 and min(a, b) % 2 == 1:
            break

        if a % 2 == 0:
            a //= 2
        else:
            a = (a + 1) // 2

        if b % 2 == 0:
            b //= 2
        else:
            b = (b + 1) // 2

    return answer

