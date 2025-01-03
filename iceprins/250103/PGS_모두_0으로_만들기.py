import sys

sys.setrecursionlimit(10 ** 6)


def solution(a, edges):
    result = 0

    if sum(a) != 0:
        return -1

    connected = [[] for _ in range(len(a))]

    for edge in edges:
        connected[edge[0]].append(edge[1])
        connected[edge[1]].append(edge[0])

    def dfs(child, parent, graph, a):
        nonlocal result
        for c in graph[child]:
            if c != parent:
                dfs(c, child, graph, a)
        a[parent] += a[child]
        result += abs(a[child])

    dfs(0, 0, connected, a)

    return result

