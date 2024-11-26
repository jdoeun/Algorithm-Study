import math


def solution(progresses, speeds):
    ans = []
    tmp = []
    
    for i in range(len(progresses)):
        rest = 100 - progresses[i]
        tmp.append(math.ceil(rest / speeds[i]))

    front = 0
    
    for i in range(len(tmp)):
        if tmp[i] > tmp[front]:
            ans.append(i - front)
            front = i
    ans.append(len(tmp) - front)

    return ans

