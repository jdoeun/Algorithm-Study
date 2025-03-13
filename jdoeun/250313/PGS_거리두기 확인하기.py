from collections import deque


def bfs(p):
    start = []

    for i in range(5):
        for j in range(5):
            if p[i][j] == "P":
                start.append([i, j])

    for s in start:
        queue = deque([s])
        visited = [s]  # 방문 처리 리스트
        dist = [[0] * 5 for _ in range(5)]  # 거리 리스트

        while queue:
            node = queue.popleft()
            y, x = node  # 현재 위치

            # 이동 방향 (상, 하, 좌, 우)
            move_x = [0, 0, -1, 1]
            move_y = [-1, 1, 0, 0]

            for i in range(4):
                new_x = y + move_y[i]
                new_y = x + move_x[i]

                # 격자 내 범위 체크 및 방문 여부 확인
                if 0 <= new_x < 5 and 0 <= new_y < 5 and [new_x, new_y] not in visited:
                    if p[new_x][new_y] == 'P' and dist[y][x] <= 1:
                        return 0  # 거리두기 위반 (상하좌우 체크)

                    elif p[new_x][new_y] == 'O':  # 빈 테이블인 경우 BFS 확장
                        dist[new_x][new_y] = dist[y][x] + 1
                        visited.append([new_x, new_y])
                        queue.append([new_x, new_y])

    return 1  # 모든 'P' 탐색 후 거리두기 준수


def solution(places):
    answer = []
    for place in places:
        answer.append(bfs(place))

    return answer