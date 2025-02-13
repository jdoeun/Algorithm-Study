import heapq


def dijkstra(v, n, graph):
    q = []
    heapq.heappush(q, (0, v))
    distance = [float('inf')] * (n + 1)
    distance[v] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (dist + i[1], i[0]))

    return distance


def solution(N, road, K):
    answer = 0

    graph = [[] for _ in range(N + 1)]

    for r in road:
        a, b, c = r
        graph[a].append((b, c))
        graph[b].append((a, c))

    result = dijkstra(1, N, graph)

    for c in result:
        if c <= K:
            answer += 1

    return answer

