from collections import defaultdict


def solution(n, wires):
    answer = float('inf')

    def union(x, y):
        x = find(x)
        y = find(y)

        if x < y:
            parent[y] = x
        else:
            parent[x] = y

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    for i in range(n - 1):
        parent = [x for x in range(n + 1)]
        tmp = wires[:i] + wires[i + 1:]
        for j in range(n - 2):
            a, b = tmp[j]
            if find(a) != find(b):
                union(a, b)

        stats = defaultdict(int)

        for j in range(1, n + 1):
            stats[find(parent[j])] += 1

        print(stats)
        info = list(stats.values())

        answer = min(answer, abs(info[0] - info[1]))

    return answer

