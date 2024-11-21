from collections import deque


def bfs(x, y, n):
    q = deque()
    q.append(x)
    visited = [0] * 1000001
    visited[x] = 1

    while q:
        x = q.popleft()
        for nx in (x + n, x * 2, x * 3):
            if nx > y:
                continue
            if visited[nx] == 0:
                visited[nx] = visited[x] + 1
                q.append(nx)

    return visited[y] - 1


def solution(x, y, n):
    answer = bfs(x, y, n)

    return answer

