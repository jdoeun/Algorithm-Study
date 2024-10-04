def solution(n, costs):
    answer = 0

    costs.sort(key=lambda x: x[2])
    parents = [i for i in range(n)]

    def union(x, y):
        nonlocal parents
        x = find(x)
        y = find(y)

        if x < y:
            parents[y] = x
        else:
            parents[x] = y

    def find(x):
        nonlocal parents
        if x != parents[x]:
            parents[x] = find(parents[x])

        return parents[x]

    for i in range(len(costs)):
        a, b, cost = costs[i]
        if find(a) == find(b):
            continue
        union(a, b)
        answer += cost

    return answer
