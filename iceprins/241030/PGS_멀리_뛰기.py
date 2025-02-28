def solution(n):
    dp = [0] * 2001

    for i in range(1, n + 1):
        if i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] = 2
        else:
            dp[i] = (dp[i - 2] + dp[i - 1]) % 1234567

    return dp[n]

