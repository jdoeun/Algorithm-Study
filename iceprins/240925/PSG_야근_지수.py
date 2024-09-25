import heapq


def solution(n, works):
    answer = 0

    if sum(works) <= n:
        return 0

    q = []

    for i in range(len(works)):
        heapq.heappush(q, -works[i])

    for _ in range(n):
        amount = heapq.heappop(q)
        amount += 1
        heapq.heappush(q, amount)

    for work in q:
        answer += (work ** 2)

    return answer
