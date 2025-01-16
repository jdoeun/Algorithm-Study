from collections import deque


def solution(board):
    n = len(board)

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    def bfs(x, y, cost, d):
        q = deque()
        q.append((x, y, cost, d))
        visited = [[float('inf') for _ in range(n)] for _ in range(n)]
        while q:
            x, y, cost, d = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx > n - 1 or ny < 0 or ny > n - 1:
                    continue
                if board[nx][ny] == 1:
                    continue

                if i == d:
                    ncost = cost + 100
                else:
                    ncost = cost + 600

                if ncost < visited[nx][ny]:
                    visited[nx][ny] = ncost
                    q.append((nx, ny, ncost, i))

        return visited[-1][-1]

    return min(bfs(0, 0, 0, 0), bfs(0, 0, 0, 1))

