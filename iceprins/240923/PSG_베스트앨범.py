from collections import defaultdict


def solution(genres, plays):
    answer = []
    tot_info = []
    info = defaultdict(int)

    for i in range(len(genres)):
        tot_info.append((i, genres[i], plays[i]))

    tot_info.sort(key=lambda x: x[2], reverse=True)

    for i in range(len(genres)):
        info[genres[i]] += plays[i]

    info = sorted(info.items(), key=lambda x: x[1], reverse=True)

    for i in range(len(info)):
        target = info[i][0]
        cnt = 0
        tmp = []
        for j in range(len(tot_info)):
            if tot_info[j][1] == target:
                if cnt >= 2:
                    break
                cnt += 1
                tmp.append(tot_info[j][0])
        answer.extend(tmp)

    return answer
