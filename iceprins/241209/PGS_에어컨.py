def solution(temperature, t1, t2, a, b, onboard):
    temperature += 10
    t1 += 10
    t2 += 10

    dp = [[100000] * 51 for _ in range(len(onboard))]
    dp[0][temperature] = 0

    def check(idx, tmp):
        return not (onboard[idx] and not t1 <= tmp <= t2)

    for i in range(len(onboard) - 1):
        for j in range(51):
            if dp[i][j] == 100000:
                continue

            if j < temperature:
                temp = j + 1
            elif j > temperature:
                temp = j - 1
            else:
                temp = j

            if check(i + 1, temp):
                dp[i + 1][temp] = min(dp[i + 1][temp], dp[i][j])

            for temp, cost in [(j + 1, a), (j - 1, a), (j, b)]:
                if not check(i + 1, temp) or not -1 < temp < 51:
                    continue
                dp[i + 1][temp] = min(dp[i + 1][temp], dp[i][j] + cost)

    return min(dp[-1])

