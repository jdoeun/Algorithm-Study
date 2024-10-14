def solution(n, s):
    answer = []

    if s < n:
        return [-1]

    q = s // n
    r = s % n

    for i in range(n):
        answer.append(q)

    if r != 0:
        for i in range(n):
            answer[i] += 1
            r -= 1
            if r == 0:
                break

    answer.sort()

    return answer
