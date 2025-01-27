import heapq
from math import inf

# 다익스트라 알고리즘 이용

def solution(n, paths, gates, summits):
    # 간선 정리 (양방향)
    graph = [[] for _ in range(n+1)]

    for i, j, w in paths:
        graph[i].append([j,w])
        graph[j].append([i,w])

    # 산봉우리 판별
    is_summit = [False] * (n+1)

    for summit in summits:
        is_summit[summit] = True

    # gates 모두 시작 위치
    # 각 노드의 intensity 저장하는 리스트 distance
    distance = [inf] * (n+1)
    queue = []
    for gate in gates:
        distance[gate] = 0 # gate는 intensity 모두 0으로 시작
        heapq.heappush(queue, [0,gate]) # 우선순위 큐에 삽입

    # 다익스트라
    while queue:
        w, i = heapq.heappop(queue)

        # 산봉우리일 경우 바로 continue
        # i의 intensity가 더 작을 경우 -> 이미 더 작은 intensity로 노드 i를 방문한 경로가 존재하면, 현재 경로를 무시하고 탐색하지 않겠다
        if distance[i] < w or is_summit[i]:
            continue
        for j, w in graph[i]:
            intensity = max(distance[i], w) # 현재까지의 가중치와 새로 갱신된 가중치 중 더 큰 값으로 intensity를 설정
            if distance[j] > intensity: # j까지 올 때 기존 intnsity와 새로 바뀐 intenstiy 비교해서 더 작으면 new로 변경
                distance[j] = intensity
                heapq.heappush(queue, [intensity, j])

    # 거리가 같으면 산봉우리의 번호가 작은 것을 출력해야 함
    result = [-1, inf]
    for summit in sorted(summits): # 오름차순으로 산봉우리 정렬
        if distance[summit] < result[1]: # 가장 작은 값으로 반복 갱신
            result[0] = summit
            result[1] = distance[summit]

    return result