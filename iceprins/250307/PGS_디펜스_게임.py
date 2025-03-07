import heapq


def solution(n, k, enemy):
    answer, s = 0, 0
    heap = []

    for e in enemy:
        heapq.heappush(heap, -e)
        s += e
        if s > n:
            if k == 0:
                break
            s += heapq.heappop(heap)
            k -= 1
        answer += 1

    return answer

