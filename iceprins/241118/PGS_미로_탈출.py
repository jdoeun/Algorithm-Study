from collections import deque


def bfs(maps, dx, dy, sx, sy, ex, ey, r, c):
    q = deque()
    q.append((sx, sy))
    visited = [[-1] * c for _ in range(r)]
    visited[sx][sy] = 0

    while q:
        x, y = q.popleft()

        if x == ex and y == ey:
            return visited[ex][ey]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > r - 1 or ny < 0 or ny > c - 1:
                continue
            if maps[nx][ny] == "X":
                continue
            if visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))

    return -1


def solution(maps):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    S_x, S_y = -1, -1
    E_x, E_y = -1, -1
    L_x, L_y = -1, -1

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                S_x, S_y = i, j
            elif maps[i][j] == "E":
                E_x, E_y = i, j
            elif maps[i][j] == "L":
                L_x, L_y = i, j

    result_1 = bfs(maps, dx, dy, S_x, S_y, L_x, L_y, len(maps), len(maps[0]))

    if result_1 == -1:
        return -1

    result_2 = bfs(maps, dx, dy, L_x, L_y, E_x, E_y, len(maps), len(maps[0]))

    if result_2 == -1:
        return -1

    return result_1 + result_2

