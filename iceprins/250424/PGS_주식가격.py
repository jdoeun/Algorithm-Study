from collections import deque


def solution(prices):
    answer = []
    q = deque(prices)

    while q:
        price = q.popleft()
        time = 0
        for p in q:
            time += 1
            if price > p:
                break
        answer.append(time)

    return answer

