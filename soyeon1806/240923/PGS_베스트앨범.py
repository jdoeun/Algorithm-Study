def solution(genres, plays):
    answer = []

    tmp = [[genres[i], plays[i], i] for i in range(len(genres))]
    tmp = sorted(tmp, key = lambda x: (x[0], -x[1], x[2]))

    result = {}

    for i in tmp:
        if i[0] not in result:
            result[i[0]] = i[1]
        else:
            result[i[0]] += i[1]

    result = sorted(result.items(), key = lambda x: -x[1])

    for i in result:
        cnt = 0
        for j in tmp:
            if i[0] == j[0]:
                cnt += 1
                if cnt > 2:
                    break
                else:
                    answer.append(j[2])

    return answer