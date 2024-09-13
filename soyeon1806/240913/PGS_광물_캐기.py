def solution(picks, minerals):

    answer = 0
    sum = 0

    # 곡괭이 수    
    for i in picks:
        sum += i
    
    # 캘 수 있는 광물 수
    available = sum * 5

    if len(minerals) > available:
        minerals = minerals[:available]

    list_minerals = [[0, 0, 0] for _ in range ((len(minerals) // 5))]
    for i in range (len(minerals)):
        if minerals[i] == 'diamond':
            list_minerals[i // 5][0] += 1
        elif minerals[i] == 'iron':
            list_minerals[i // 5][1] += 1
        elif minerals[i] == 'stone':
            list_minerals[i // 5][2] += 1

    list_minerals.sort(key = lambda x : (-x[0], -x[1], -x[2]))

    for i in list_minerals:
        dia, iron, stone = i
        for j in range(len(picks)):
            if picks[j] > 0 and j == 0:
                picks[j] -= 1
                answer += dia + iron + stone
                break
            elif picks[j] > 0 and j == 1:
                picks[j] -= 1
                answer += (5 * dia) + iron + stone
                break
            elif picks[j] > 0 and j == 2:
                picks[j] -= 1
                answer += (25 * dia) + (5 * iron) + stone
                break

    return answer