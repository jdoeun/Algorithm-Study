def solution(target):
    dp = [[0, 0] for _ in range(max(70, target) + 1)]

    for i in range(1, 21):
        dp[i] = [1, 1]
    for i in range(21, 41):
        dp[i] = [1, 0]
    for i in (23, 25, 29, 31, 35, 37):
        dp[i] = [2, 2]
    for i in range(41, 50):
        dp[i] = [2, 1]
    dp[50] = [1, 1]
    for i in range(52, 71):
        dp[i] = [2, 2]
    for i in range(42, 61, 3):
        dp[i] = [1, 0]

    for i in range(71, target + 1):
        first = i - 60
        second = i - 50
        check = False

        if dp[first][0] < dp[second][0]:
            check = True
        elif dp[first][0] == dp[second][0]:
            if dp[second][1] < dp[first][1]:
                check = True

        if check:
            dp[i] = [dp[first][0] + 1, dp[first][1]]
        else:
            dp[i] = [dp[second][0] + 1, dp[second][1] + 1]

    return dp[target]
