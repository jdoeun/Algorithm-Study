from collections import deque

def solution(board):
    n = len(board)
    # 상, 하, 좌, 우
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    cost = [[[float('inf')] * 4 for _ in range(n)] for _ in range(n)]
    
    # 1. 탐색 시작 노드 -> 큐 삽입 -> 방문처리
    queue = deque()
    for i in range(4):
        cost[0][0][i] = 0 # 출발점의 초기 비용 설정
        queue.append((0, 0, 0, i)) # (x, y, 비용, 방향)
        
    # 2. 큐에서 노드 꺼내고 인접 노드 탐색
    while queue:
        x, y, cur_cost, direction = queue.popleft()
        
        for i, (dx, dy) in enumerate(directions):
            nx, ny = x + dx, y + dy # 새로운 좌표 계산
            
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0: # 이동 가능한 칸인지 확인
                new_cost = cur_cost + 100 if direction == i else cur_cost + 600
            
                if new_cost < cost[nx][ny][i]: # 기존 비용보다 적으면 갱신
                    cost[nx][ny][i] = new_cost
                    queue.append((nx, ny, new_cost, i)) # 큐에 삽입
    return min(cost[n - 1][n - 1])