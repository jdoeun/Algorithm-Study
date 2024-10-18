from collections import deque


def solution(n, edge):
    answer = 0

    graph = [[] for _ in range(n + 1)]
    visited = [-1] * (n + 1)

    for x in edge:
        graph[x[0]].append(x[1])
        graph[x[1]].append(x[0])

    def bfs():
        q = deque()
        q.append(1)
        visited[1] = 0

        while q:
            node = q.popleft()
            for next_node in graph[node]:
                if visited[next_node] == -1:
                    visited[next_node] = visited[node] + 1
                    q.append(next_node)

    bfs()

    dist = max(visited)

    for x in visited:
        if x == dist:
            answer += 1

    return answer
