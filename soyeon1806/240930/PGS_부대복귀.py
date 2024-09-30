from collections import deque

def solution(n, roads, sources, destination):
    answer = []
    
    graph = [[] for _ in range(n + 1)]
    cost = [-1 for _ in range(n + 1)]
    cost[destination] = 0
    queue = deque([destination])
    
    for n1, n2 in roads:
        graph[n1].append(n2)
        graph[n2].append(n1)
    
    while queue:
        x = queue.popleft()
        for node in graph[x]:
            if cost[node] == -1:
                queue.append(node)
                cost[node] = cost[x] + 1
                
    for s in sources:
        answer.append(cost[s])
    
    return answer