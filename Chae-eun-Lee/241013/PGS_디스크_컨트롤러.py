def solution(jobs):
    answer = []
    jobs.sort(key=lambda x: (x[0], x[1]))
    now = 0
    while len(jobs) > 0:
        if now <= jobs[0][0]:
            answer.append(jobs[0][1])
            now = jobs[0][0] + jobs[0][1]
            jobs.pop(0)
        else:
            temp = []
            for i in range(len(jobs)):
                if jobs[i][0] <= now:
                    temp.append(jobs[i][1])  # 소요시간
                else:
                    break
            n = temp.index(min(temp))  # 최댓값 인덱스
            answer.append(now - jobs[n][0] + jobs[n][1])
            now += jobs[n][1]
            jobs.pop(n)

    return (sum(answer) // len(answer))