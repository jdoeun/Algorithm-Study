from collections import deque


def solution(priorities, location):
    q = deque()

    for i in range(len(priorities)):
        q.append((i, priorities[i]))

    priorities.sort()
    cnt = 1

    while True:
        now = q.popleft()
        if now[1] == priorities[-1]:
            priorities.pop()
            if now[0] == location:
                return cnt
            cnt += 1
        else:
            q.append(now)

