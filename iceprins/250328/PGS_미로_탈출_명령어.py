import sys

sys.setrecursionlimit(10 ** 6)
answer = "z"


def solution(n, m, x, y, r, c, k):
    def find(sx, sy, d, cnt):
        global answer

        if k < cnt + abs(sx - r + 1) + abs(sy - c + 1):
            return

        if cnt == k:
            if sx == r - 1 and sy == c - 1:
                answer = d
            return

        if 0 <= sx + 1 <= n - 1 and d < answer:
            find(sx + 1, sy, d + "d", cnt + 1)
        if 0 <= sy - 1 <= m - 1 and d < answer:
            find(sx, sy - 1, d + "l", cnt + 1)
        if 0 <= sy + 1 <= m - 1 and d < answer:
            find(sx, sy + 1, d + "r", cnt + 1)
        if 0 <= sx - 1 <= n - 1 and d < answer:
            find(sx - 1, sy, d + "u", cnt + 1)

    dist = abs(x - r) + abs(y - c)

    if dist > k or (k - dist) % 2 == 1:
        return "impossible"

    find(x - 1, y - 1, "", 0)

    return answer

