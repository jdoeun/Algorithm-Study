from collections import *

def solution(board):
    answer = 0
    
    n = len(board)
    m = len(board[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    
    q = deque()
    
    dist = [[-1 for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                q.append((i, j, 0))
                dist[i][j] = 0
        if q :
            break
            
    while q:
        x, y, c = q.popleft()
        
        if board[x][y] == 'G':
            return c
        
        for i in range(4):
            nx, ny = x, y
            
            while 0 <= nx + dx[i] < n and 0 <= ny + dy[i] < m and board[nx + dx[i]][ny + dy[i]] != 'D':
                nx += dx[i]
                ny += dy[i]
                
            if dist[nx][ny] == -1:
                dist[nx][ny] = c + 1
                q.append((nx, ny, c + 1))
                
    return -1