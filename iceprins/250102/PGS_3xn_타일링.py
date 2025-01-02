def solution(n):
    dp = [0] * (n + 1)

    if n % 2 == 1:
        return 0

    for i in range(0, n + 1, 2):
        if i == 2:
            dp[i] = 3
        elif i == 4:
            dp[i] = 11
        else:
            dp[i] += dp[i - 2] * 3
            for j in range(i - 4, 0, -2):
                dp[i] += dp[j] * 2
            dp[i] += 2
        dp[i] %= 1000000007

    return dp[n]

