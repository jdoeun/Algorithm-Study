from collections import deque

def solution(maps):
    answer = []
    
    n, m = len(maps), len(maps[0])
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited = [[False] * m for _ in range(n)]
    
    def bfs(x, y):
        visited[x][y] = True
        queue = deque()
        queue.append((x, y))
        days = int(maps[x][y])
        
        while queue:
            x, y = queue.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n  and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != 'X':
                    queue.append((nx, ny))
                    days += int(maps[nx][ny])
                    visited[nx][ny] = True
        return days
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and not visited[i][j]:
                answer.append(bfs(i, j))
                
    if len(answer) == 0:
        return [-1]
    else:
        return sorted(answer)