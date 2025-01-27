import heapq


def solution(n, paths, gates, summits):
    connected = [[] for _ in range(n + 1)]

    for path in paths:
        connected[path[0]].append((path[1], path[2]))
        connected[path[1]].append((path[0], path[2]))

    is_summit = [False] * (n + 1)

    for summit in summits:
        is_summit[summit] = True

    distance = [float('inf')] * (n + 1)
    q = []

    for gate in gates:
        distance[gate] = 0
        heapq.heappush(q, [0, gate])

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist or is_summit[now]:
            continue
        for j, dd in connected[now]:
            dd = max(distance[now], dd)
            if distance[j] > dd:
                distance[j] = dd
                heapq.heappush(q, [dd, j])

    result = [-1, float('inf')]

    for summit in sorted(summits):
        if distance[summit] < result[1]:
            result[0] = summit
            result[1] = distance[summit]

    return result

