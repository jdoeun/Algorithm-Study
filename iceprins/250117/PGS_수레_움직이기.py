from collections import deque
from copy import deepcopy


def solution(maze):
    n, m = len(maze), len(maze[0])
    board = [[0 for _ in range(m)] for _ in range(n)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                rsx = i
                rsy = j
            elif maze[i][j] == 2:
                bsx = i
                bsy = j
            elif maze[i][j] == 3:
                rex = i
                rey = j
            elif maze[i][j] == 4:
                bex = i
                bey = j
            elif maze[i][j] == 5:
                board[i][j] = 1

    visited_r = [[0 for _ in range(m)] for _ in range(n)]
    visited_b = [[0 for _ in range(m)] for _ in range(n)]
    visited_r[rsx][rsy] = 1
    visited_b[bsx][bsy] = 1

    def bfs(rx, ry, bx, by, rcount, bcount, visited_r, visited_b):
        q = deque()
        q.append((rx, ry, bx, by, rcount, bcount, visited_r, visited_b))

        while q:
            rx, ry, bx, by, rcount, bcount, visited_r, visited_b = q.popleft()

            if rx == rex and ry == rey and bx == bex and by == bey:
                return max(rcount, bcount)

            if rx == rex and ry == rey:
                for i in range(4):
                    nbx, nby = bx + dx[i], by + dy[i]
                    if nbx < 0 or nbx > n - 1 or nby < 0 or nby > m - 1:
                        continue
                    if board[nbx][nby] == 1:
                        continue
                    if visited_b[nbx][nby] != 0:
                        continue
                    if not (nbx == rx and nby == ry):
                        visited_b[nbx][nby] = 1
                        q.append((rx, ry, nbx, nby, rcount, bcount + 1, visited_r, visited_b))
            elif bx == bex and by == bey:
                for i in range(4):
                    nrx, nry = rx + dx[i], ry + dy[i]
                    if nrx < 0 or nrx > n - 1 or nry < 0 or nry > m - 1:
                        continue
                    if board[nrx][nry] == 1:
                        continue
                    if visited_r[nrx][nry] != 0:
                        continue
                    if not (nrx == bx and nry == by):
                        visited_r[nrx][nry] = 1
                        q.append((nrx, nry, bx, by, rcount + 1, bcount, visited_r, visited_b))
            else:
                for i in range(4):
                    nrx, nry = rx + dx[i], ry + dy[i]
                    visited_r_copy = deepcopy(visited_r)
                    visited_b_copy = deepcopy(visited_b)
                    if nrx < 0 or nrx > n - 1 or nry < 0 or nry > m - 1:
                        continue
                    if board[nrx][nry] == 1:
                        continue
                    if visited_r_copy[nrx][nry] != 0:
                        continue
                    for j in range(4):
                        nbx, nby = bx + dx[j], by + dy[j]
                        if nbx < 0 or nbx > n - 1 or nby < 0 or nby > m - 1:
                            continue
                        if board[nbx][nby] == 1:
                            continue
                        if visited_b_copy[nbx][nby] != 0:
                            continue
                        if not (nrx == nbx and nry == nby) and not (
                                nrx == bx and nry == by and nbx == rx and nby == ry):
                            visited_r_copy[nrx][nry] = 1
                            visited_b_copy[nbx][nby] = 1
                            q.append((nrx, nry, nbx, nby, rcount + 1, bcount + 1, visited_r_copy, visited_b_copy))

        return 0

    return bfs(rsx, rsy, bsx, bsy, 0, 0, visited_r, visited_b)

