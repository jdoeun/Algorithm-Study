def solution(info, edges):
    answer = []
    visited = [False] * len(info)

    def back(s, w):
        if s <= w:
            return
        answer.append(s)
        for p, c in edges:
            if visited[p] and not visited[c]:
                visited[c] = True
                if info[c] == 0:
                    back(s + 1, w)
                else:
                    back(s, w + 1)
                visited[c] = False

    visited[0] = True
    back(1, 0)

    return max(answer)

