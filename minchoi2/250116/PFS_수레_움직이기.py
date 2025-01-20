from collections import deque

def solution(maze):
    n, m = len(maze), len(maze[0])
    
    # 시작점과 도착점 찾기
    red_start = blue_start = red_end = blue_end = None
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1: red_start = (i, j)
            elif maze[i][j] == 2: blue_start = (i, j)
            elif maze[i][j] == 3: red_end = (i, j)
            elif maze[i][j] == 4: blue_end = (i, j)
    
    # 1. 탐색 시작 노드 -> 큐 삽입 => 방문처리
    q = deque()
    visited = set()
    
    # state = (빨간위치, 파란위치, 이동수)
    q.append((red_start, blue_start, {red_start}, {blue_start}, 0))
    visited.add((red_start, blue_start))
    
    # 방향 정의 (상하좌우)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    # 2. 큐에서 노드를 꺼내서 방문하지 않은 인접 노드 확인
    while q:
        red_pos, blue_pos, red_visited, blue_visited, count = q.popleft()
        
        # 도착 확인
        if red_pos == red_end and blue_pos == blue_end:
            return count
            
        red_finished = red_pos == red_end
        blue_finished = blue_pos == blue_end
        
        # 수레별로 이동 가능한 방향 결정
        for rx, ry in [(0,0)] if red_finished else zip(dx, dy):
            # 빨간 수레 다음 위치 계산
            nrx = red_pos[0] + rx
            nry = red_pos[1] + ry
            new_red = (nrx, nry)
            
            # 빨간 수레 이동 가능 여부 확인
            if not red_finished:
                if not (0 <= nrx < n and 0 <= nry < m):  # 범위 체크
                    continue
                if maze[nrx][nry] == 5:  # 벽 체크
                    continue
                if new_red in red_visited:  # 방문 체크
                    continue
            
            for bx, by in [(0,0)] if blue_finished else zip(dx, dy):
                # 파란 수레 다음 위치 계산
                nbx = blue_pos[0] + bx
                nby = blue_pos[1] + by
                new_blue = (nbx, nby)
                
                # 파란 수레 이동 가능 여부 확인
                if not blue_finished:
                    if not (0 <= nbx < n and 0 <= nby < m):  # 범위 체크
                        continue
                    if maze[nbx][nby] == 5:  # 벽 체크
                        continue
                    if new_blue in blue_visited:  # 방문 체크
                        continue
                
                # 두 수레가 같은 칸으로 이동하거나 서로 교차하는 경우 제외
                if new_red == new_blue:
                    continue
                if new_red == blue_pos and new_blue == red_pos:
                    continue
                
                # 방문하지 않은 조합인 경우에만 큐에 추가
                if (new_red, new_blue) not in visited:
                    visited.add((new_red, new_blue))
                    # 새로운 방문 기록은 기존 set을 복사하고 새 위치 추가
                    new_red_visited = red_visited if red_finished else set(red_visited) | {new_red}
                    new_blue_visited = blue_visited if blue_finished else set(blue_visited) | {new_blue}
                    q.append((new_red, new_blue, new_red_visited, new_blue_visited, count + 1))
    
    # 3. 큐가 빌 때까지 못 찾으면 불가능
    return 0