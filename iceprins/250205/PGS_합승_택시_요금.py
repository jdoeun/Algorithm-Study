import heapq

INF = float('inf')


def dijkstra(start, graph):
    q = []
    distance = [INF] * (len(graph))
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            if dist + i[1] < distance[i[0]]:
                distance[i[0]] = dist + i[1]
                heapq.heappush(q, (dist + i[1], i[0]))

    return distance


def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]

    for fare in fares:
        v1, v2, cost = fare
        graph[v1].append((v2, cost))
        graph[v2].append((v1, cost))

    result_A, result_B = INF, INF

    arr_A = dijkstra(s, graph)
    result_A = arr_A[a] + arr_A[b]

    for v in range(1, n + 1):
        arr_B = dijkstra(v, graph)

        result_B = min(result_B, arr_A[v] + arr_B[a] + arr_B[b])

    return min(result_A, result_B)

