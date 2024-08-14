# DP 풀이
from collections import deque, defaultdict

W = [
    [1, 7, 6, 7, 5, 4, 5, 3, 2, 3],
    [7, 1, 2, 4, 2, 3, 5, 4, 5, 6],
    [6, 2, 1, 2, 3, 2, 3, 5, 4, 5],
    [7, 4, 2, 1, 5, 3, 2, 6, 5, 4],
    [5, 2, 3, 5, 1, 2, 4, 2, 3, 5],
    [4, 3, 2, 3, 2, 1, 2, 3, 2, 3],
    [5, 5, 3, 2, 4, 2, 1, 5, 3, 2],
    [3, 4, 5, 6, 2, 3, 5, 1, 2, 4],
    [2, 5, 4, 5, 3, 2, 3, 2, 1, 2],
    [3, 6, 5, 4, 5, 3, 2, 4, 2, 1],
]


def solution(numbers):
    numbers = list(map(int, numbers))
    n = len(numbers)
    dp = defaultdict(lambda: float('inf'))
    dp[(4, 6, 0)] = 0

    q = deque([(4, 6, 0)])

    while q:
        left, right, idx = q.popleft()

        if idx == n:
            continue

        next_num = numbers[idx]

        if next_num != right:
            new_cost = dp[(left, right, idx)] + W[left][next_num]
            if new_cost < dp[(next_num, right, idx + 1)]:
                dp[(next_num, right, idx + 1)] = new_cost
                q.append((next_num, right, idx + 1))

        if next_num != left:
            new_cost = dp[(left, right, idx)] + W[right][next_num]
            if new_cost < dp[(left, next_num, idx + 1)]:
                dp[(left, next_num, idx + 1)] = new_cost
                q.append((left, next_num, idx + 1))

    return min(dp[(left, right, n)] for left in range(10) for right in range(10))


# 재귀 풀이
import sys, math
from collections import defaultdict

sys.setrecursionlimit(10 ** 6)

W = [
    [1, 7, 6, 7, 5, 4, 5, 3, 2, 3],
    [7, 1, 2, 4, 2, 3, 5, 4, 5, 6],
    [6, 2, 1, 2, 3, 2, 3, 5, 4, 5],
    [7, 4, 2, 1, 5, 3, 2, 6, 5, 4],
    [5, 2, 3, 5, 1, 2, 4, 2, 3, 5],
    [4, 3, 2, 3, 2, 1, 2, 3, 2, 3],
    [5, 5, 3, 2, 4, 2, 1, 5, 3, 2],
    [3, 4, 5, 6, 2, 3, 5, 1, 2, 4],
    [2, 5, 4, 5, 3, 2, 3, 2, 1, 2],
    [3, 6, 5, 4, 5, 3, 2, 4, 2, 1],
]


def solve(numbers, cache, i, left, right):
    if i == len(numbers):
        return 0

    if (left, right) in cache[i]:
        return cache[i][(left, right)]

    w = math.inf
    num = numbers[i]

    if num != left:
        w = min(w, solve(numbers, cache, i + 1, num, left) + W[right][num])
    if num != right:
        w = min(w, solve(numbers, cache, i + 1, num, right) + W[left][num])

    cache[i][(left, right)] = w

    return w


def solution(numbers):
    cache = defaultdict(dict)
    numbers = list(int(x) for x in numbers)

    return solve(numbers, cache, 0, 4, 6)
