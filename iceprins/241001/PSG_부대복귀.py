from collections import deque


def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n + 1)]

    for road in roads:
        graph[road[0]].append(road[1])
        graph[road[1]].append(road[0])

    q = deque()
    q.append(destination)
    visited = [-1] * (n + 1)
    visited[destination] = 0

    while q:
        current = q.popleft()
        for next_vertex in graph[current]:
            if visited[next_vertex] == -1:
                visited[next_vertex] = visited[current] + 1
                q.append(next_vertex)

    return [visited[i] for i in sources]
