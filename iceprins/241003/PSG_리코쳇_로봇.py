from collections import deque


def solution(board):
    row = len(board)
    col = len(board[0])
    rx, ry = 0, 0

    for i in range(row):
        for j in range(col):
            if board[i][j] == "R":
                rx, ry = i, j

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs():
        q = deque()
        q.append((rx, ry))
        visited = [[0] * col for _ in range(row)]
        visited[rx][ry] = 1

        while q:
            x, y = q.popleft()
            if board[x][y] == "G":
                return visited[x][y] - 1
            for i in range(4):
                nx, ny = x, y
                while True:
                    nx += dx[i]
                    ny += dy[i]
                    if 0 <= nx <= row - 1 and 0 <= ny <= col - 1 and board[nx][ny] == "D":
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                    if nx < 0 or nx > row - 1 or ny < 0 or ny > col - 1:
                        nx -= dx[i]
                        ny -= dy[i]
                        break
                if not visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))

        return -1

    answer = bfs()

    return answer
