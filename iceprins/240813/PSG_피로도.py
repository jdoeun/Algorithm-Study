def backtrack(k, dungeons, visited, cnt, answer, depth):
    if depth == len(dungeons):
        return cnt

    tmp = 0

    for i in range(len(dungeons)):
        if not visited[i]:
            visited[i] = True
            if k >= dungeons[i][0]:
                tmp = backtrack(k - dungeons[i][1], dungeons, visited, cnt + 1, answer, depth + 1)
            else:
                tmp = backtrack(k, dungeons, visited, cnt, answer, depth + 1)
            visited[i] = False

            answer = max(answer, tmp)

    return answer


def solution(k, dungeons):
    answer = -1
    visited = [False] * len(dungeons)

    ans = backtrack(k, dungeons, visited, 0, answer, 0)

    return ans
