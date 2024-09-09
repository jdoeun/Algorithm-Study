def solution(picks, minerals):
    answer = 0

    if len(minerals) > sum(picks):
        minerals = minerals[:sum(picks) * 5]

    mineral_info = [[0, 0, 0] for _ in range(10)]

    for i in range(len(minerals)):
        if minerals[i] == "diamond":
            mineral_info[i // 5][0] += 1
        elif minerals[i] == "iron":
            mineral_info[i // 5][1] += 1
        else:
            mineral_info[i // 5][2] += 1

    mineral_info.sort(key=lambda x: (-x[0], -x[1], -x[2]))

    for d in mineral_info:
        dia, iron, stone = d
        for i in range(len(picks)):
            if i == 0 and picks[i] > 0:
                picks[i] -= 1
                answer += (dia + iron + stone)
                break
            if i == 1 and picks[i] > 0:
                picks[i] -= 1
                answer += (5 * dia + iron + stone)
                break
            if i == 2 and picks[i] > 0:
                picks[i] -= 1
                answer += (25 * dia + 5 * iron + stone)
                break

    return answer
