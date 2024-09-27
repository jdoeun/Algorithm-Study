# 기존 풀이
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(maps):
    answer = []

    for i in range(len(maps)):
        maps[i] = list(maps[i])

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'X':
                maps[i][j] = 0
            else:
                maps[i][j] = int(maps[i][j])

    s = 0

    for row in maps:
        s += sum(row)

    if s == 0:
        return [-1]

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        visited[x][y] = True
        cnt = maps[x][y]

        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx > len(maps) - 1 or ny < 0 or ny > len(maps[0]) - 1:
                    continue
                if not visited[nx][ny] and maps[nx][ny] != 0:
                    visited[nx][ny] = True
                    cnt += maps[nx][ny]
                    q.append((nx, ny))

        return cnt

    visited = [[False] * len(maps[0]) for _ in range(len(maps))]

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 0 and not visited[i][j]:
                result = bfs(i, j)
                answer.append(result)

    answer.sort()

    return answer


# 개선한 풀이
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(maps):
    answer = []

    def bfs(x, y):
        q = deque()
        q.append((x, y))
        visited[x][y] = True
        cnt = int(maps[x][y])

        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx > len(maps) - 1 or ny < 0 or ny > len(maps[0]) - 1:
                    continue
                if not visited[nx][ny] and maps[nx][ny] != "X":
                    visited[nx][ny] = True
                    cnt += int(maps[nx][ny])
                    q.append((nx, ny))

        return cnt

    visited = [[False] * len(maps[0]) for _ in range(len(maps))]

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != "X" and not visited[i][j]:
                result = bfs(i, j)
                answer.append(result)

    answer.sort()

    if not answer:
        return [-1]

    return answer
