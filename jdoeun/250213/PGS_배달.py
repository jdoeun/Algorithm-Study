import heapq


# 다익스트라 활용
def solution(N, road, K):
    # 그래프 초기화 (인접 리스트)
    graph = {i: [] for i in range(1, N + 1)}

    # 도로 정보 입력 (양방향 그래프)
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))

    # 최단 거리 테이블 (무한대 초기화)
    INF = float('inf')
    distances = {i: INF for i in range(1, N + 1)}
    distances[1] = 0  # 1번 마을은 시작점이므로 거리 0

    # 다익스트라 알고리즘 (우선순위 큐 사용)
    pq = [(0, 1)]  # (거리, 노드)

    while pq:
        # 가장 짧은 거리 노드 선택
        current_dist, current_node = heapq.heappop(pq)

        # 현재 거리보다 이미 저장된 최단 거리가 작다면 무시
        if current_dist > distances[current_node]:
            continue

        # 현재 노드의 이웃 노드 확인
        # 현재 노드(current_node)에서 이동 가능한 neighbor 확인
        # 기존 거리(current_dist)에 weight를 더해 new_distance 계산
        for neighbor, weight in graph[current_node]:
            new_distance = current_dist + weight

            # 더 짧은 거리로 갱신되면 업데이트 후 큐에 추가
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(pq, (new_distance, neighbor))

    # K 이하의 시간에 도달 가능한 마을 개수 반환
    return sum(1 for dist in distances.values() if dist <= K)