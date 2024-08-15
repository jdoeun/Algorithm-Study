import sys
from collections import defaultdict

answer = sys.maxsize


def check(s1, s2):
    cnt = 0

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            cnt += 1

    if cnt == 1:
        return True

    return False


def dfs(now, target, words, visited):
    global answer

    if now == target:
        answer = min(answer, visited[now])
        return

    for word in words:
        if check(word, now):
            if visited[word] != 0 and visited[word] <= visited[now] + 1:
                continue
            visited[word] = visited[now] + 1
            dfs(word, target, words, visited)


def solution(begin, target, words):
    global answer
    visited = defaultdict(int)

    if target not in words:
        return 0
    else:
        dfs(begin, target, words, visited)
        return answer
