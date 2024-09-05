def solution(tickets):
    answer = []
    visited = [False] * len(tickets)

    def dfs(dest, path):
        if len(path) == len(tickets) + 1:
            answer.append(path)
            return

        for i in range(len(tickets)):
            if tickets[i][0] == dest and not visited[i]:
                visited[i] = True
                dfs(tickets[i][1], path + [tickets[i][1]])
                visited[i] = False

    dfs("ICN", ["ICN"])

    answer.sort()

    return answer[0]
